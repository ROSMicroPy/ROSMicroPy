
#include "mp_uros_type_support.h"
#include "mp_uros_dataTypeParser.h"
#include "uros_mesg_func.h"
#include "py/objstr.h"
#include <stdlib.h>
//#include "rosidl_runtime_c/message_type_support_struct.h"

#include "std_msgs/std_msgs/msg/detail/byte__struct.h"
#include "std_msgs/std_msgs/msg/detail/int16__struct.h"
#include "std_msgs/std_msgs/msg/detail/int32__struct.h"
#include "std_msgs/std_msgs/msg/detail/float32__struct.h"
#include "std_msgs/std_msgs/msg/detail/float64__struct.h"

bool mpy_uros_typesupport_cdr_serialize(int slot, const void *untyped_ros_message, ucdrBuffer *cdr);
bool mpy_uros_typesupport_cdr_deserialize(int slot, ucdrBuffer *cdr, void *untyped_ros_message);
size_t mpy_uros_typesupport_get_serialized_size(int slot, const void *mp_obj, size_t current_alignment);
uint32_t mpy_uros_typesupport_get_initial_serialized_size(int slot, const void *mp_obj);
size_t mpy_uros_typesupport_get_max_serialized_size(int slot, bool *full_bounded, size_t current_alignment);

#define mpy_uros_type_support_slots 20
dxc_cb_t *g_typeSupportCtrlBlks[mpy_uros_type_support_slots];

#define MPY_UROS_DEFAULT_STRING_CAPACITY 256
#define MPY_UROS_DEFAULT_SEQUENCE_CAPACITY 64

static bool dxi_is_array_or_sequence(const dxi_t *inst) {
  return inst->isSequence || inst->isArray;
}

static size_t dxi_capacity_or_default(const dxi_t *inst, size_t fallback) {
  return inst->capicity > 0 ? (size_t)inst->capicity : fallback;
}

static size_t dxi_scalar_size(const dxi_t *inst) {
  switch (inst->kind) {
    case DXI_KIND_BOOL:
    case DXI_KIND_BYTE:
    case DXI_KIND_CHAR:
    case DXI_KIND_INT8:
    case DXI_KIND_UINT8:
      return 1;
    case DXI_KIND_INT16:
    case DXI_KIND_UINT16:
      return 2;
    case DXI_KIND_INT32:
    case DXI_KIND_UINT32:
    case DXI_KIND_FLOAT32:
      return 4;
    case DXI_KIND_INT64:
    case DXI_KIND_UINT64:
    case DXI_KIND_FLOAT64:
      return 8;
    default:
      return 0;
  }
}

static size_t dxi_add_aligned_size(size_t current_alignment, size_t item_size) {
  return ucdr_alignment(current_alignment, item_size) + item_size;
}

static size_t dxi_string_serialized_size(size_t current_alignment, size_t len) {
  size_t initial_alignment = current_alignment;
  current_alignment += ucdr_alignment(current_alignment, MICROXRCEDDS_PADDING) + MICROXRCEDDS_PADDING;
  current_alignment += len + 1;
  return current_alignment - initial_alignment;
}

static size_t dxi_sequence_length_size(size_t current_alignment) {
  return dxi_add_aligned_size(current_alignment, sizeof(uint32_t));
}

static size_t dxi_value_serialized_size(mp_obj_t value, dxi_t *inst, size_t current_alignment) {
  const size_t initial_alignment = current_alignment;

  if (inst->isSequence) {
    current_alignment += dxi_sequence_length_size(current_alignment);
  }

  if (dxi_is_array_or_sequence(inst)) {
    size_t len = 0;
    mp_obj_t *items = NULL;
    mp_buffer_info_t bufinfo;
    if ((inst->kind == DXI_KIND_BYTE || inst->kind == DXI_KIND_UINT8 || inst->kind == DXI_KIND_INT8)
        && mp_get_buffer(value, &bufinfo, MP_BUFFER_READ)) {
      len = bufinfo.len;
    } else {
      mp_obj_get_array(value, &len, &items);
    }

    for (size_t i = 0; i < len; i++) {
      if (inst->kind == DXI_KIND_STRING) {
        size_t str_len = 0;
        mp_obj_str_get_data(items[i], &str_len);
        current_alignment += dxi_string_serialized_size(current_alignment, str_len);
      } else {
        size_t item_size = dxi_scalar_size(inst);
        current_alignment += dxi_add_aligned_size(current_alignment, item_size);
      }
    }
    return current_alignment - initial_alignment;
  }

  if (inst->kind == DXI_KIND_STRING) {
    size_t len = 0;
    mp_obj_str_get_data(value, &len);
    current_alignment += dxi_string_serialized_size(current_alignment, len);
  } else {
    current_alignment += dxi_add_aligned_size(current_alignment, dxi_scalar_size(inst));
  }

  return current_alignment - initial_alignment;
}

static bool dxi_get_array_items(mp_obj_t value, dxi_t *inst, size_t *len, mp_obj_t **items) {
  mp_obj_get_array(value, len, items);

  if (inst->isSequence) {
    if (inst->capicity > 0 && *len > (size_t)inst->capicity) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds sequence capacity"), inst->name);
      return false;
    }
  } else if (inst->isArray) {
    if (inst->capicity <= 0) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array requires capicity"), inst->name);
      return false;
    }
    if (*len != (size_t)inst->capicity) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array length mismatch"), inst->name);
      return false;
    }
  }

  return true;
}

static bool serialize_instruction_range(dxil_t *dxil, int start, int end, mp_map_t *current_map, ucdrBuffer *cdr);
static size_t serialized_size_instruction_range(dxil_t *dxil, int start, int end, mp_map_t *current_map, size_t current_alignment);
static bool deserialize_instruction_range(dxil_t *dxil, int start, int end, mp_obj_t parent_obj, ucdrBuffer *cdr);
static size_t max_serialized_size_instruction_range(dxil_t *dxil, int start, int end, bool *full_bounded, size_t current_alignment);

static bool serialize_ros_type_value(dxil_t *dxil, dxi_t *inst, mp_obj_t value, ucdrBuffer *cdr) {
  if (dxi_is_array_or_sequence(inst)) {
    size_t len = 0;
    mp_obj_t *items = NULL;
    if (!dxi_get_array_items(value, inst, &len, &items)) {
      return false;
    }
    if (inst->isSequence) {
      ucdr_serialize_uint32_t(cdr, (uint32_t)len);
    }
    for (size_t i = 0; i < len; i++) {
      if (!mp_obj_is_type(items[i], &mp_type_dict)) {
        mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("ROS field '%s' sequence item must be a dict"), inst->name);
        return false;
      }
      if (!serialize_instruction_range(dxil, inst + 1 - dxil->instructionList, inst->instructionEnd, mp_obj_dict_get_map(items[i]), cdr)) {
        return false;
      }
    }
    return true;
  }

  if (!mp_obj_is_type(value, &mp_type_dict)) {
    mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("ROS field '%s' must be a dict"), inst->name);
    return false;
  }
  return serialize_instruction_range(dxil, inst + 1 - dxil->instructionList, inst->instructionEnd, mp_obj_dict_get_map(value), cdr);
}

static bool serialize_instruction_range(dxil_t *dxil, int start, int end, mp_map_t *current_map, ucdrBuffer *cdr) {
  for (int x = start; x <= end; x++) {
    dxi_t *inst = &dxil->instructionList[x];
    mp_map_elem_t *element = mp_map_lookup(current_map, inst->name_obj, MP_MAP_LOOKUP);
    if (element == NULL) {
      mp_raise_msg_varg(&mp_type_KeyError, MP_ERROR_TEXT("missing ROS field '%s'"), inst->name);
      return false;
    }

    if (inst->isROSType) {
      if (!serialize_ros_type_value(dxil, inst, element->value, cdr)) {
        return false;
      }
      x = inst->instructionEnd;
    } else {
      inst->serialize(cdr, element->value, inst);
    }
  }
  return true;
}

static size_t serialized_size_ros_type_value(dxil_t *dxil, dxi_t *inst, mp_obj_t value, size_t current_alignment) {
  if (dxi_is_array_or_sequence(inst)) {
    const size_t initial_alignment = current_alignment;
    size_t len = 0;
    mp_obj_t *items = NULL;
    if (!dxi_get_array_items(value, inst, &len, &items)) {
      return 0;
    }
    if (inst->isSequence) {
      current_alignment += dxi_sequence_length_size(current_alignment);
    }
    for (size_t i = 0; i < len; i++) {
      if (!mp_obj_is_type(items[i], &mp_type_dict)) {
        return 0;
      }
      current_alignment += serialized_size_instruction_range(
        dxil,
        inst + 1 - dxil->instructionList,
        inst->instructionEnd,
        mp_obj_dict_get_map(items[i]),
        current_alignment);
    }
    return current_alignment - initial_alignment;
  }

  if (!mp_obj_is_type(value, &mp_type_dict)) {
    return 0;
  }
  return serialized_size_instruction_range(
    dxil,
    inst + 1 - dxil->instructionList,
    inst->instructionEnd,
    mp_obj_dict_get_map(value),
    current_alignment);
}

static size_t serialized_size_instruction_range(dxil_t *dxil, int start, int end, mp_map_t *current_map, size_t current_alignment) {
  const size_t initial_alignment = current_alignment;
  for (int x = start; x <= end; x++) {
    dxi_t *inst = &dxil->instructionList[x];
    mp_map_elem_t *element = mp_map_lookup(current_map, inst->name_obj, MP_MAP_LOOKUP);
    if (element == NULL) {
      return 0;
    }

    if (inst->isROSType) {
      current_alignment += serialized_size_ros_type_value(dxil, inst, element->value, current_alignment);
      x = inst->instructionEnd;
    } else {
      current_alignment += dxi_value_serialized_size(element->value, inst, current_alignment);
    }
  }
  return current_alignment - initial_alignment;
}

static bool deserialize_ros_type_value(dxil_t *dxil, dxi_t *inst, mp_obj_t parent_obj, ucdrBuffer *cdr) {
  if (dxi_is_array_or_sequence(inst)) {
    uint32_t len = 0;
    if (inst->isSequence) {
      ucdr_deserialize_uint32_t(cdr, &len);
      if (inst->capicity > 0 && len > (uint32_t)inst->capicity) {
        mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds sequence capacity"), inst->name);
        return false;
      }
    } else {
      if (inst->capicity <= 0) {
        mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array requires capicity"), inst->name);
        return false;
      }
      len = (uint32_t)inst->capicity;
    }

    mp_obj_t list = mp_obj_new_list(0, NULL);
    for (uint32_t i = 0; i < len; i++) {
      mp_obj_t child = mp_obj_new_dict(inst->shallowComponentCount);
      if (!deserialize_instruction_range(dxil, inst + 1 - dxil->instructionList, inst->instructionEnd, child, cdr)) {
        return false;
      }
      mp_obj_list_append(list, child);
    }
    mp_obj_dict_store(parent_obj, inst->name_obj, list);
    return true;
  }

  mp_obj_t child = mp_obj_new_dict(inst->shallowComponentCount);
  mp_obj_dict_store(parent_obj, inst->name_obj, child);
  return deserialize_instruction_range(dxil, inst + 1 - dxil->instructionList, inst->instructionEnd, child, cdr);
}

static bool deserialize_instruction_range(dxil_t *dxil, int start, int end, mp_obj_t parent_obj, ucdrBuffer *cdr) {
  mp_obj_stk_t obj_stack;
  obj_stack.objects[0] = parent_obj;
  obj_stack.stkPtr = 1;

  for (int x = start; x <= end; x++) {
    dxi_t *inst = &dxil->instructionList[x];
    if (inst->isROSType) {
      if (!deserialize_ros_type_value(dxil, inst, parent_obj, cdr)) {
        return false;
      }
      x = inst->instructionEnd;
    } else {
      inst->deserialize(cdr, inst, &obj_stack);
    }
  }
  return true;
}

static size_t max_serialized_size_ros_type(dxil_t *dxil, dxi_t *inst, bool *full_bounded, size_t current_alignment) {
  const size_t initial_alignment = current_alignment;
  size_t count = 1;

  if (inst->isSequence) {
    current_alignment += dxi_sequence_length_size(current_alignment);
    if (inst->capicity <= 0) {
      *full_bounded = false;
      count = MPY_UROS_DEFAULT_SEQUENCE_CAPACITY;
    } else {
      count = (size_t)inst->capicity;
    }
  } else if (inst->isArray) {
    count = dxi_capacity_or_default(inst, 0);
  }

  for (size_t i = 0; i < count; i++) {
    current_alignment += max_serialized_size_instruction_range(
      dxil,
      inst + 1 - dxil->instructionList,
      inst->instructionEnd,
      full_bounded,
      current_alignment);
  }

  return current_alignment - initial_alignment;
}

static size_t max_serialized_size_instruction_range(dxil_t *dxil, int start, int end, bool *full_bounded, size_t current_alignment) {
  const size_t initial_alignment = current_alignment;

  for (int x = start; x <= end; x++) {
    dxi_t *inst = &dxil->instructionList[x];
    if (inst->isROSType) {
      current_alignment += max_serialized_size_ros_type(dxil, inst, full_bounded, current_alignment);
      x = inst->instructionEnd;
      continue;
    }

    size_t count = 1;
    if (inst->isSequence) {
      current_alignment += dxi_sequence_length_size(current_alignment);
      if (inst->capicity <= 0) {
        *full_bounded = false;
        count = MPY_UROS_DEFAULT_SEQUENCE_CAPACITY;
      } else {
        count = (size_t)inst->capicity;
      }
    } else if (inst->isArray) {
      count = dxi_capacity_or_default(inst, 0);
    }

    for (size_t i = 0; i < count; i++) {
      if (inst->kind == DXI_KIND_STRING) {
        if (inst->capicity <= 0) {
          *full_bounded = false;
        }
        current_alignment += dxi_string_serialized_size(
          current_alignment,
          dxi_capacity_or_default(inst, MPY_UROS_DEFAULT_STRING_CAPACITY));
      } else {
        current_alignment += dxi_add_aligned_size(current_alignment, dxi_scalar_size(inst));
      }
    }
  }

  return current_alignment - initial_alignment;
}

/**
 * This specialized #define macro utilizes a feature in GCC where you can define functions in a function.
 * We will use this to define the Type Support functions but append a number that corresponds to an entry
 * in the typeSupport array entry. The functions defined call the real function and passes along a
 * slot number allowing the type support functions to have access to the schema data needed to process
 * data from Micropython to ROS
 */
#define typeSupportFunc(n)                                                                      \
  bool mpy_uros_ts##n##_serialize(const void *untyped_ros_message, ucdrBuffer *cdr)             \
  {                                                                                             \
    return mpy_uros_typesupport_cdr_serialize(n, untyped_ros_message, cdr);                     \
  }                                                                                             \
  bool mpy_uros_ts##n##_deserialize(ucdrBuffer *cdr, void *untyped_ros_message)                 \
  {                                                                                             \
    return mpy_uros_typesupport_cdr_deserialize(n, cdr, untyped_ros_message);                   \
  }                                                                                             \
  size_t mpy_uros_ts##n##_get_serialized_size(const void *mp_obj, size_t current_alignment)     \
  {                                                                                             \
    return mpy_uros_typesupport_get_serialized_size(n, mp_obj, current_alignment);              \
  }                                                                                             \
  uint32_t mpy_uros_ts##n##_get_initial_serialized_size(const void *mp_obj)                     \
  {                                                                                             \
    return mpy_uros_typesupport_get_initial_serialized_size(n, mp_obj);                         \
  }                                                                                             \
  size_t mpy_uros_ts##n##_get_max_serialized_size(bool *full_bounded, size_t current_alignment) \
  {                                                                                             \
    return mpy_uros_typesupport_get_max_serialized_size(n, full_bounded, current_alignment);    \
  }

/**************************************************************************************/
bool mpy_uros_ts0_serialize(const void *untyped_ros_message, ucdrBuffer *cdr)
{
  return mpy_uros_typesupport_cdr_serialize(0, untyped_ros_message, cdr);
}
bool mpy_uros_ts0_deserialize(ucdrBuffer *cdr, void *untyped_ros_message)
{
  return mpy_uros_typesupport_cdr_deserialize(0, cdr, untyped_ros_message);
}
size_t mpy_uros_ts0_get_serialized_size(const void *mp_obj, size_t current_alignment)
{
  return mpy_uros_typesupport_get_serialized_size(0, mp_obj, current_alignment);
}
uint32_t mpy_uros_ts0_get_initial_serialized_size(const void *mp_obj)
{
  return mpy_uros_typesupport_get_initial_serialized_size(0, mp_obj);
}
size_t mpy_uros_ts0_get_max_serialized_size(bool *full_bounded, size_t current_alignment)
{
  return mpy_uros_typesupport_get_max_serialized_size(0, full_bounded, current_alignment);
}

/***********************************************************************************************/

#define typeSupportEntry(n)                                                                                                            \
                                                                                                                                       \
  dxc_cb_t *typeSupportCtrlBlk_##n = malloc(sizeof(dxc_cb_t));                                                                         \
                                                                                                                                       \
  typeSupportCtrlBlk_##n->ros_mesg_type_support = malloc(sizeof(rosidl_message_type_support_t));                                       \
  /* The DXIL will be allocated when a type is registered */                                                                           \
      message_type_support_callbacks_t *mpy_uros_ts##n##_cb = malloc(sizeof(message_type_support_callbacks_t));                        \
                                                                                                                                       \
  mpy_uros_ts##n##_cb->cdr_serialize = mpy_uros_ts##n##_serialize;                                                                     \
  mpy_uros_ts##n##_cb->cdr_deserialize = mpy_uros_ts##n##_deserialize;                                                                 \
  mpy_uros_ts##n##_cb->get_serialized_size = mpy_uros_ts##n##_get_initial_serialized_size;                                             \
  mpy_uros_ts##n##_cb->get_serialized_size_with_initial_alignment = mpy_uros_ts##n##_get_serialized_size;                              \
  mpy_uros_ts##n##_cb->max_serialized_size = mpy_uros_ts##n##_get_max_serialized_size;                                                 \
                                                                                                                                       \
  typeSupportCtrlBlk_##n->ros_mesg_type_support->typesupport_identifier = strdup(ROSIDL_TYPESUPPORT_MICROXRCEDDS_C__IDENTIFIER_VALUE); \
  typeSupportCtrlBlk_##n->ros_mesg_type_support->data = mpy_uros_ts##n##_cb;                                                           \
  typeSupportCtrlBlk_##n->ros_mesg_type_support->func = get_message_typesupport_handle_function;                                       \
  g_typeSupportCtrlBlks[n] = typeSupportCtrlBlk_##n;

// typeSupportFunc(0);
typeSupportFunc(1);
typeSupportFunc(2);
typeSupportFunc(3);
typeSupportFunc(4);
typeSupportFunc(5);
typeSupportFunc(6);
typeSupportFunc(7);
typeSupportFunc(8);
typeSupportFunc(9);
typeSupportFunc(10);
typeSupportFunc(11);
typeSupportFunc(12);
typeSupportFunc(13);
typeSupportFunc(14);
typeSupportFunc(15);
typeSupportFunc(16);
typeSupportFunc(17);
typeSupportFunc(18);
typeSupportFunc(19);

/*
* Initialize the Type Support
*/
void init_mpy_ROS_TypeSupport(void)
{

  //    g_typeSupportCtrlBlks=malloc( (sizeof(dxc_cb_t) +4) * mpy_uros_type_support_slots);

  typeSupportEntry(0);
  typeSupportEntry(1);
  typeSupportEntry(2);
  typeSupportEntry(3);
  typeSupportEntry(4);
  typeSupportEntry(5);
  typeSupportEntry(6);
  typeSupportEntry(7);
  typeSupportEntry(8);
  typeSupportEntry(9);
  typeSupportEntry(10);
  typeSupportEntry(11);
  typeSupportEntry(12);
  typeSupportEntry(13);
  typeSupportEntry(14);
  typeSupportEntry(15);
  typeSupportEntry(16);
  typeSupportEntry(17);
  typeSupportEntry(18);
  typeSupportEntry(19);

  for (int x = 0; x < mpy_uros_type_support_slots; x++)
  {
    g_typeSupportCtrlBlks[x]->type = NULL;
    g_typeSupportCtrlBlks[x]->dxil = NULL;

    g_typeSupportCtrlBlks[x]->componentCount = 0;
    g_typeSupportCtrlBlks[x]->index = 0;
  }
}

/**
*
*
*/
dxc_cb_t *findTypeByName(const char *type)
{

  for (int x = 0; x < mpy_uros_type_support_slots; x++)
  {

    if (type == NULL)
      return NULL;
    if (strlen(type) == 0)
      return NULL;

    // See if we hit the end of the allocated blocks
    if (g_typeSupportCtrlBlks[x]->type == NULL)
      return NULL;

    if (strcmp(g_typeSupportCtrlBlks[x]->dxil->type, type) == 0)
      return g_typeSupportCtrlBlks[x];
  }

  return NULL;
}

dxc_cb_t *findAvailTypeSlot()
{

  for (int x = 0; x < mpy_uros_type_support_slots; x++)
  {
    if (g_typeSupportCtrlBlks[x]->type == NULL)
      return g_typeSupportCtrlBlks[x];
  }

  return NULL;
}

/**
 *
 *
 */
bool mpy_uros_typesupport_cdr_serialize(int slot, const void *untyped_ros_message, ucdrBuffer *cdr)
{
  (void)cdr;

  if (!untyped_ros_message)
  {
    return false;
  }

  dxc_cb_t *dataTypeCtrlBlk = g_typeSupportCtrlBlks[slot];
  dxil_t *dxil = dataTypeCtrlBlk->dxil;

  mp_obj_t obj_in = (mp_obj_t)untyped_ros_message;
  mp_map_t *root_obj = mp_obj_dict_get_map(obj_in);

  return serialize_instruction_range(dxil, 1, dataTypeCtrlBlk->componentCount, root_obj, cdr);
}

/**
 *
 *
 */
bool mpy_uros_typesupport_cdr_deserialize(int slot, ucdrBuffer *cdr, void *untyped_ros_message)
{
  (void)cdr;

  if (!untyped_ros_message)
  {
    return false;
  }

  void **ros_mesg = untyped_ros_message;

  ros_subscription *rsub = get_ROS_Subscription(slot);
  dxil_t *dxil = rsub->dataTypeCtrlBlk->dxil;
  mp_obj_t root_obj = mp_obj_new_dict(dxil->instructionList[0].shallowComponentCount);

  if (!deserialize_instruction_range(dxil, 1, rsub->dataTypeCtrlBlk->componentCount, root_obj, cdr)) {
    return false;
  }
  *ros_mesg = root_obj;

  return true;
}

/**
 *
 *
 *
 */
size_t mpy_uros_typesupport_get_serialized_size(int slot, const void *mp_obj, size_t current_alignment)
{
  if (!mp_obj)
    return 0;

  const size_t initial_alignment = current_alignment;

  dxc_cb_t *dataTypeCtrlBlk = g_typeSupportCtrlBlks[slot];
  dxil_t *dxil = dataTypeCtrlBlk->dxil;

  mp_obj_t obj_in = (mp_obj_t)mp_obj;
  mp_map_t *root_obj = mp_obj_dict_get_map(obj_in);
  current_alignment += serialized_size_instruction_range(dxil, 1, dataTypeCtrlBlk->componentCount, root_obj, current_alignment);

  return current_alignment - initial_alignment;
}

/**
 *
 *
 *
 */
uint32_t mpy_uros_typesupport_get_initial_serialized_size(int slot, const void *mp_obj)
{
  return (uint32_t)(mpy_uros_typesupport_get_serialized_size(slot, mp_obj, 0));
}

/**
 *
 *
 *
 */
size_t mpy_uros_typesupport_get_max_serialized_size(int slot, bool *full_bounded, size_t current_alignment)
{
  *full_bounded = true;
  const size_t initial_alignment = current_alignment;

  dxc_cb_t *dataTypeCtrlBlk = g_typeSupportCtrlBlks[slot];
  dxil_t *dxil = dataTypeCtrlBlk->dxil;

  current_alignment += max_serialized_size_instruction_range(dxil, 1, dataTypeCtrlBlk->componentCount, full_bounded, current_alignment);

  return current_alignment - initial_alignment;
}

/**
 *
 *
 *
 */
void deserializeROSType(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  mp_obj_t dict = mp_obj_new_dict(inst->shallowComponentCount);
  mp_obj_t parent_obj = obj_stack->objects[obj_stack->stkPtr - 1];
  mp_obj_dict_store(parent_obj, inst->name_obj, dict);
  if (obj_stack->stkPtr >= mp_obj_stack_size) {
    mp_raise_ValueError(MP_ERROR_TEXT("ROS type nesting is too deep"));
    return;
  }
  obj_stack->objects[obj_stack->stkPtr++] = dict;
}

size_t serializedSizeROSType(const void *mp_obj, size_t current_alignment)
{
  return 0;
}

void serializeROSType(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
}

static void store_deserialized_value(mp_obj_stk_t *obj_stack, dxi_t *inst, mp_obj_t value) {
  mp_obj_dict_store(obj_stack->objects[obj_stack->stkPtr - 1], inst->name_obj, value);
}

static mp_int_t get_mp_int(mp_obj_t value, dxi_t *inst) {
  if (!mp_obj_is_int(value)) {
    mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("ROS field '%s' must be an int"), inst->name);
  }
  return mp_obj_get_int_truncated(value);
}

static double get_mp_float(mp_obj_t value, dxi_t *inst) {
  if (mp_obj_is_float(value) || mp_obj_is_int(value)) {
    return mp_obj_get_float_to_d(value);
  }
  mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("ROS field '%s' must be a float"), inst->name);
  return 0;
}

static void serialize_one_scalar(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst) {
  switch (inst->kind) {
    case DXI_KIND_BOOL:
      ucdr_serialize_bool(cdr, mp_obj_is_true(value));
      return;
    case DXI_KIND_BYTE:
    case DXI_KIND_UINT8:
      ucdr_serialize_uint8_t(cdr, (uint8_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_CHAR:
      if (mp_obj_is_str(value)) {
        size_t len = 0;
        const char *data = mp_obj_str_get_data(value, &len);
        if (len != 1) {
          mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' char must be length 1"), inst->name);
        }
        ucdr_serialize_char(cdr, data[0]);
      } else {
        ucdr_serialize_char(cdr, (char)get_mp_int(value, inst));
      }
      return;
    case DXI_KIND_INT8:
      ucdr_serialize_int8_t(cdr, (int8_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_INT16:
      ucdr_serialize_int16_t(cdr, (int16_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_UINT16:
      ucdr_serialize_uint16_t(cdr, (uint16_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_INT32:
      ucdr_serialize_int32_t(cdr, (int32_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_UINT32:
      ucdr_serialize_uint32_t(cdr, (uint32_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_INT64:
      ucdr_serialize_int64_t(cdr, (int64_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_UINT64:
      ucdr_serialize_uint64_t(cdr, (uint64_t)get_mp_int(value, inst));
      return;
    case DXI_KIND_FLOAT32:
      ucdr_serialize_float(cdr, (float)get_mp_float(value, inst));
      return;
    case DXI_KIND_FLOAT64:
      ucdr_serialize_double(cdr, get_mp_float(value, inst));
      return;
    default:
      mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("unsupported ROS field type '%s'"), inst->type);
  }
}

static mp_obj_t deserialize_one_scalar(ucdrBuffer *cdr, dxi_t *inst) {
  switch (inst->kind) {
    case DXI_KIND_BOOL: {
      bool v;
      ucdr_deserialize_bool(cdr, &v);
      return mp_obj_new_bool(v);
    }
    case DXI_KIND_BYTE:
    case DXI_KIND_UINT8: {
      uint8_t v;
      ucdr_deserialize_uint8_t(cdr, &v);
      return mp_obj_new_int_from_uint(v);
    }
    case DXI_KIND_CHAR: {
      char v;
      ucdr_deserialize_char(cdr, &v);
      return mp_obj_new_str(&v, 1);
    }
    case DXI_KIND_INT8: {
      int8_t v;
      ucdr_deserialize_int8_t(cdr, &v);
      return mp_obj_new_int(v);
    }
    case DXI_KIND_INT16: {
      int16_t v;
      ucdr_deserialize_int16_t(cdr, &v);
      return mp_obj_new_int(v);
    }
    case DXI_KIND_UINT16: {
      uint16_t v;
      ucdr_deserialize_uint16_t(cdr, &v);
      return mp_obj_new_int_from_uint(v);
    }
    case DXI_KIND_INT32: {
      int32_t v;
      ucdr_deserialize_int32_t(cdr, &v);
      return mp_obj_new_int(v);
    }
    case DXI_KIND_UINT32: {
      uint32_t v;
      ucdr_deserialize_uint32_t(cdr, &v);
      return mp_obj_new_int_from_uint(v);
    }
    case DXI_KIND_INT64: {
      int64_t v;
      ucdr_deserialize_int64_t(cdr, &v);
      return mp_obj_new_int_from_ll(v);
    }
    case DXI_KIND_UINT64: {
      uint64_t v;
      ucdr_deserialize_uint64_t(cdr, &v);
      return mp_obj_new_int_from_ull(v);
    }
    case DXI_KIND_FLOAT32: {
      float v;
      ucdr_deserialize_float(cdr, &v);
      return mp_obj_new_float(v);
    }
    case DXI_KIND_FLOAT64: {
      double v;
      ucdr_deserialize_double(cdr, &v);
      return mp_obj_new_float(v);
    }
    default:
      mp_raise_msg_varg(&mp_type_TypeError, MP_ERROR_TEXT("unsupported ROS field type '%s'"), inst->type);
      return mp_const_none;
  }
}

static void serialize_array_or_sequence(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst) {
  size_t len = 0;
  mp_obj_t *items = NULL;

  if (inst->isSequence) {
    mp_buffer_info_t bufinfo;
    if ((inst->kind == DXI_KIND_BYTE || inst->kind == DXI_KIND_UINT8 || inst->kind == DXI_KIND_INT8) && mp_get_buffer(value, &bufinfo, MP_BUFFER_READ)) {
      if (inst->capicity > 0 && bufinfo.len > (size_t)inst->capicity) {
        mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds sequence capacity"), inst->name);
      }
      ucdr_serialize_uint32_t(cdr, (uint32_t)bufinfo.len);
      ucdr_serialize_array_uint8_t(cdr, (const uint8_t *)bufinfo.buf, bufinfo.len);
      return;
    }

    mp_obj_get_array(value, &len, &items);
    if (inst->capicity > 0 && len > (size_t)inst->capicity) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds sequence capacity"), inst->name);
    }
    ucdr_serialize_uint32_t(cdr, (uint32_t)len);
  } else {
    if (inst->capicity <= 0) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array requires capicity"), inst->name);
    }
    mp_obj_get_array(value, &len, &items);
    if (len != (size_t)inst->capicity) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array length mismatch"), inst->name);
    }
  }

  for (size_t i = 0; i < len; i++) {
    if (inst->kind == DXI_KIND_STRING) {
      serializeString(cdr, items[i], inst);
    } else {
      serialize_one_scalar(cdr, items[i], inst);
    }
  }
}

static void deserialize_array_or_sequence(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack) {
  uint32_t len = 0;
  if (inst->isSequence) {
    ucdr_deserialize_uint32_t(cdr, &len);
    if (inst->capicity > 0 && len > (uint32_t)inst->capicity) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds sequence capacity"), inst->name);
    }
  } else {
    if (inst->capicity <= 0) {
      mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' array requires capicity"), inst->name);
    }
    len = (uint32_t)inst->capicity;
  }

  mp_obj_t list = mp_obj_new_list(0, NULL);
  for (uint32_t i = 0; i < len; i++) {
    mp_obj_t item = inst->kind == DXI_KIND_STRING ? mp_const_none : deserialize_one_scalar(cdr, inst);
    if (inst->kind == DXI_KIND_STRING) {
      size_t cap = dxi_capacity_or_default(inst, MPY_UROS_DEFAULT_STRING_CAPACITY) + 1;
      char *buf = malloc(cap);
      if (buf == NULL) {
        mp_raise_msg(&mp_type_MemoryError, MP_ERROR_TEXT("allocating ROS string"));
      }
      if (!ucdr_deserialize_string(cdr, buf, cap)) {
        free(buf);
        mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("failed to deserialize string field '%s'"), inst->name);
      }
      item = mp_obj_new_str(buf, strlen(buf));
      free(buf);
    }
    mp_obj_list_append(list, item);
  }
  store_deserialized_value(obj_stack, inst, list);
}

/**
 *
 *
 *
 *
 */
void serializeBool(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (dxi_is_array_or_sequence(inst)) {
    serialize_array_or_sequence(cdr, value, inst);
  } else {
    serialize_one_scalar(cdr, value, inst);
  }
}

size_t serializedSizeBool(const void *mp_obj, size_t current_alignment)
{
  (void)mp_obj;
  return dxi_add_aligned_size(current_alignment, sizeof(bool));
}

void deserializeBool(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  if (dxi_is_array_or_sequence(inst)) {
    deserialize_array_or_sequence(cdr, inst, obj_stack);
  } else {
    store_deserialized_value(obj_stack, inst, deserialize_one_scalar(cdr, inst));
  }
}

/**
 *
 *
 *
 */
void serializeInt(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (dxi_is_array_or_sequence(inst)) {
    serialize_array_or_sequence(cdr, value, inst);
  } else {
    serialize_one_scalar(cdr, value, inst);
  }
}

size_t serializedSizeInt(const void *mp_obj, size_t current_alignment)
{
  (void)mp_obj;
  return dxi_add_aligned_size(current_alignment, sizeof(int32_t));
}

void deserializeInt(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  if (dxi_is_array_or_sequence(inst)) {
    deserialize_array_or_sequence(cdr, inst, obj_stack);
  } else {
    store_deserialized_value(obj_stack, inst, deserialize_one_scalar(cdr, inst));
  }
}

void serializeString(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (dxi_is_array_or_sequence(inst)) {
    serialize_array_or_sequence(cdr, value, inst);
    return;
  }

  size_t len = 0;
  const char *str = mp_obj_str_get_data(value, &len);
  if (inst->capicity > 0 && len > (size_t)inst->capicity) {
    mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("ROS field '%s' exceeds string capacity"), inst->name);
  }
  ucdr_serialize_string(cdr, str);
}

void deserializeString(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  if (dxi_is_array_or_sequence(inst)) {
    deserialize_array_or_sequence(cdr, inst, obj_stack);
    return;
  }

  size_t cap = dxi_capacity_or_default(inst, MPY_UROS_DEFAULT_STRING_CAPACITY) + 1;
  char *buf = malloc(cap);
  if (buf == NULL) {
    mp_raise_msg(&mp_type_MemoryError, MP_ERROR_TEXT("allocating ROS string"));
  }
  if (!ucdr_deserialize_string(cdr, buf, cap)) {
    free(buf);
    mp_raise_msg_varg(&mp_type_ValueError, MP_ERROR_TEXT("failed to deserialize string field '%s'"), inst->name);
  }
  store_deserialized_value(obj_stack, inst, mp_obj_new_str(buf, strlen(buf)));
  free(buf);
}

size_t serializedSizeString(const void *mp_obj, size_t current_alignment)
{
  size_t len = 0;
  mp_obj_str_get_data((mp_obj_t)mp_obj, &len);
  return dxi_string_serialized_size(current_alignment, len);
}

/**
 *
 *
 *
 *
 */
void serializeFloat(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (dxi_is_array_or_sequence(inst)) {
    serialize_array_or_sequence(cdr, value, inst);
  } else {
    serialize_one_scalar(cdr, value, inst);
  }
}

void deserializeFloat(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  if (dxi_is_array_or_sequence(inst)) {
    deserialize_array_or_sequence(cdr, inst, obj_stack);
  } else {
    store_deserialized_value(obj_stack, inst, deserialize_one_scalar(cdr, inst));
  }
}

size_t serializedSizeFloat(const void *mp_obj, size_t current_alignment)
{
  (void)mp_obj;
  return dxi_add_aligned_size(current_alignment, sizeof(float));
}

/**
 *
 *
 *
 *
 */
void deserializeDouble(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  if (dxi_is_array_or_sequence(inst)) {
    deserialize_array_or_sequence(cdr, inst, obj_stack);
  } else {
    store_deserialized_value(obj_stack, inst, deserialize_one_scalar(cdr, inst));
  }
}

void serializeDouble(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (dxi_is_array_or_sequence(inst)) {
    serialize_array_or_sequence(cdr, value, inst);
  } else {
    serialize_one_scalar(cdr, value, inst);
  }
}

size_t serializedSizeDouble(const void *mp_obj, size_t current_alignment)
{
  (void)mp_obj;
  return dxi_add_aligned_size(current_alignment, sizeof(double));
}

// ROSIDL_TYPESUPPORT_MICROXRCEDDS_C_PUBLIC_example_interfaces
// size_t get_serialized_size_example_interfaces__msg__String(
//   const void * untyped_ros_message,
//   size_t current_alignment)
// {
//   if (!untyped_ros_message) {
//     return 0;
//   }

//   const _String__ros_msg_type * ros_message = (const _String__ros_msg_type *)(untyped_ros_message);
//   (void)ros_message;

//   const size_t initial_alignment = current_alignment;

//   // Member: data
//   current_alignment += ucdr_alignment(current_alignment, MICROXRCEDDS_PADDING) + MICROXRCEDDS_PADDING;
//   current_alignment += ros_message->data.size + 1;

//   return current_alignment - initial_alignment;
// }

// UCDR_BASIC_TYPE_DECLARATIONS(_char, char)
// UCDR_BASIC_TYPE_DECLARATIONS(_bool, bool)
// UCDR_BASIC_TYPE_DECLARATIONS(_uint8_t, uint8_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_uint16_t, uint16_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_uint32_t, uint32_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_uint64_t, uint64_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_int8_t, int8_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_int16_t, int16_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_int32_t, int32_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_int64_t, int64_t)
// UCDR_BASIC_TYPE_DECLARATIONS(_float, float)
// UCDR_BASIC_TYPE_DECLARATIONS(_double, double)

// cdr
// dxi
