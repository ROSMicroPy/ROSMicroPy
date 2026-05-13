
#include "mp_uros_type_support.h"
#include "mp_uros_dataTypeParser.h"
#include "uros_mesg_func.h"
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

  mp_obj_stk_t obj_stack;
  obj_stack.objects[0] = root_obj;
  obj_stack.stkPtr = 1;

  // Index 0 is the root object, do not process
  for (int x = 1; x < dataTypeCtrlBlk->componentCount + 1; x++)
  {

    dxi_t *instruction = &dxil->instructionList[x];
    const char *cstr_Name = instruction->name;
    mp_obj_t mpMap = obj_stack.objects[obj_stack.stkPtr - 1];

    mp_obj_t mpName = mp_obj_new_str(cstr_Name, strlen(cstr_Name));
    mp_map_elem_t *element = mp_map_lookup(mpMap, mpName, MP_MAP_LOOKUP);
    mp_obj_t value = element->value;

    if (instruction->isROSType)
    {
      mp_map_t *mobj = mp_obj_dict_get_map(value);
      obj_stack.objects[obj_stack.stkPtr++] = mobj;
    }
    else
    {
      instruction->serialize(cdr, value, instruction);
    }

    if (dxil->instructionList[x].islastBlk)
      obj_stack.stkPtr--;
  }

  return true;
}

/**
 *
 *
 */
bool mpy_uros_typesupport_cdr_deserialize(int slot, ucdrBuffer *cdr, void *untyped_ros_message)
{
  (void)cdr;

  mp_obj_stk_t obj_stack;

  if (!untyped_ros_message)
  {
    return false;
  }

  void **ros_mesg = untyped_ros_message;

  ros_subscription *rsub = get_ROS_Subscription(slot);
  dxil_t *dxil = rsub->dataTypeCtrlBlk->dxil;
  mp_obj_t root_obj = mp_obj_new_dict(dxil->instructionList[0].shallowComponentCount);
  obj_stack.objects[0] = root_obj;
  obj_stack.stkPtr = 1;

  // Index 0 is the root object, do not process
  for (int x = 1; x < rsub->dataTypeCtrlBlk->componentCount + 1; x++)
  {
    dxil->instructionList[x].deserialize(cdr, &dxil->instructionList[x], &obj_stack);
    if (dxil->instructionList[x].islastBlk)
      obj_stack.stkPtr--;
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

  // Index 0 is the root object, do not process
  for (int x = 1; x < dataTypeCtrlBlk->componentCount + 1; x++)
  {
    current_alignment += dxil->instructionList[x].serializedSize(mp_obj, current_alignment);
  }

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
  (void)current_alignment;
  *full_bounded = true;

  const size_t initial_alignment = current_alignment;

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
  mp_obj_dict_store(parent_obj, mp_obj_new_str(inst->name, strlen(inst->name)), dict);
  obj_stack->objects[obj_stack->stkPtr++] = dict;
}

size_t serializedSizeROSType(const void *mp_obj, size_t current_alignment)
{
  return 0;
}

void serializeROSType(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
}

/**
 *
 *
 *
 *
 */
void serializeBool(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  bool bVal = true;
  if (value == mp_const_none)
  {
    return;
  }
  if (&mp_type_bool != mp_obj_get_type(value))
  {
    return;
  }
  int iVal = mp_obj_get_int(value);
  if (iVal == 0)
    bVal = false;
  ucdr_serialize_bool(cdr, bVal);
}

size_t serializedSizeBool(const void *mp_obj, size_t current_alignment)
{
  bool val;
  const size_t initial_alignment = current_alignment;
  const size_t item_size = sizeof(val);
  current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  return current_alignment - initial_alignment;
}

void deserializeBool(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
}

/**
 *
 *
 *
 */
void serializeInt(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  int iVal;
  if (value == mp_const_none)
  {
    return;
  }
  if (&mp_type_int != mp_obj_get_type(value))
  {
    return;
  }
  iVal = mp_obj_get_int(value);
  ucdr_serialize_int32_t(cdr, iVal);
}

size_t serializedSizeInt(const void *mp_obj, size_t current_alignment)
{
  int intVal;
  const size_t initial_alignment = current_alignment;
  const size_t item_size = sizeof(intVal);
  current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  return current_alignment - initial_alignment;
}

void deserializeInt(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
}

/**
 *
 *
 *
 *
 */
void serializeFloat(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  if (value == mp_const_none)
  {
    return;
  }

  const mp_obj_type_t *mpType = mp_obj_get_type(value);

  if (&mp_type_float == mpType)
  {
    double dVal = mp_obj_get_float_to_d(value);
    ucdr_serialize_double(cdr, dVal);
  }
  else if (&mp_type_int == mpType)
  {
    int iVal = mp_obj_get_int(value);
    double dVal = (double)iVal;
    ucdr_serialize_double(cdr, dVal);
  }
}

void deserializeFloat(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  double doubleVal;
  ucdr_deserialize_double(cdr, &doubleVal);
  mp_obj_dict_store(obj_stack->objects[obj_stack->stkPtr - 1], mp_obj_new_str(inst->name, strlen(inst->name)), mp_obj_new_float(doubleVal));
}

size_t serializedSizeFloat(const void *mp_obj, size_t current_alignment)
{
  double doubleVal;
  const size_t initial_alignment = current_alignment;
  const size_t item_size = sizeof(doubleVal);
  current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;

  return current_alignment - initial_alignment;
}

/**
 *
 *
 *
 *
 */
void deserializeDouble(ucdrBuffer *cdr, dxi_t *inst, mp_obj_stk_t *obj_stack)
{
  double doubleVal;
  ucdr_deserialize_double(cdr, &doubleVal);
  mp_obj_dict_store(obj_stack->objects[obj_stack->stkPtr - 1], mp_obj_new_str(inst->name, strlen(inst->name)), mp_obj_new_float(doubleVal));
}

void serializeDouble(ucdrBuffer *cdr, mp_obj_t value, dxi_t *inst)
{
  double dVal;
  if (value == mp_const_none)
  {
    return;
  }
  if (&mp_type_float != mp_obj_get_type(value))
  {
    NULL;
  }
  dVal = mp_obj_get_float_to_d(value);
  ucdr_serialize_double(cdr, dVal);
}

size_t serializedSizeDouble(const void *mp_obj, size_t current_alignment)
{
  double doubleVal;
  const size_t initial_alignment = current_alignment;
  const size_t item_size = sizeof(doubleVal);
  current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  return current_alignment - initial_alignment;
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
