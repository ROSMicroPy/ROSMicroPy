
#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"
#include "py/runtime.h"


//ROSIDL_TYPESUPPORT_MICROXRCEDDS_C_EXPORT_mpy_uros_msgs
size_t mpy_uros_typesupport_get_serialized_size(const void * mp_obj, size_t current_alignment);

// ROSIDL_TYPESUPPORT_MICROXRCEDDS_C_EXPORT_mpy_uros_msgs
static uint32_t mpy_uros_typesupport_get_initial_serialized_size(const void * mp_obj);
static size_t mp_uros_typesupport_max_serialized_size();

bool mpy_uros_msg_init(mp_obj_t *msg)
{
  if (!msg) {
    return false;
  }
  // // linear
  // if (!geometry_msgs__msg__Vector3__init(&msg->linear)) {
  //   mpy_uros_msg_fini(msg);
  //   return false;
  // }
  // // angular
  // if (!geometry_msgs__msg__Vector3__init(&msg->angular)) {
  //   mpy_uros_msg_fini(msg);
  //   return false;
  // }
  return true;
}

void mpy_uros_msg_fini(mp_obj_t * msg)
{
  if (!msg) {
    return;
  }
  // // linear
  // geometry_msgs__msg__Vector3__fini(&msg->linear);
  // // angular
  // geometry_msgs__msg__Vector3__fini(&msg->angular);
}

bool mpy_uros_msg_are_equal(const mp_obj_t *lhs, const mp_obj_t *rhs)
{
  if (!lhs || !rhs) {
    return false;
  }

  // // linear
  // if (!geometry_msgs__msg__Vector3__are_equal(
  //     &(lhs->linear), &(rhs->linear)))
  // {
  //   return false;
  // }
  // // angular
  // if (!geometry_msgs__msg__Vector3__are_equal(
  //     &(lhs->angular), &(rhs->angular)))
  // {
  //   return false;
  // }
  return true;
}

bool mpy_uros_msg_copy(const mp_obj_t * input, mp_obj_t *output)
{
  if (!input || !output) {
    return false;
  }


  // // linear
  // if (!geometry_msgs__msg__Vector3__copy(
  //     &(input->linear), &(output->linear)))
  // {
  //   return false;
  // }
  // // angular
  // if (!geometry_msgs__msg__Vector3__copy(
  //     &(input->angular), &(output->angular)))
  // {
  //   return false;
  // }
  return true;
}

mp_obj_t *mpy_uros_msg_create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mp_obj_t * msg = (mp_obj_t *)allocator.allocate(sizeof(mp_obj_t), allocator.state);
  if (!msg) {
    return NULL;
  }

  //memset(msg, 0, sizeof(geometry_msgs__msg__Twist));
  bool success = mpy_uros_msg_init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void mpy_uros_msg_destroy(mp_obj_t * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mpy_uros_msg_fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool mpy_uros_msg_Sequence__init(mp_obj_t * array, size_t size)
{

  if (!array) {
    return false;
  }
  
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  //geometry_msgs__msg__Twist * data = NULL;

  if (size) {
    data = (geometry_msgs__msg__Twist *)allocator.zero_allocate(size, sizeof(geometry_msgs__msg__Twist), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mpy_uros_msg_init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mpy_uros_msg_fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void mpy_uros_msg_Sequence__fini(mp_obj_t * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mpy_uros_msg_fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mpy_uros_msg_Sequence *
mpy_uros_msg_Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mpy_uros_msg_Sequence * array = (mpy_uros_msg_Sequence *)allocator.allocate(sizeof(mpy_uros_msg_Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mpy_uros_msg_Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void mpy_uros_msg_Sequence__destroy(mp_obj_t * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mpy_uros_msg_Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool mpy_uros_msg_Sequence__are_equal(const mp_obj_t * lhs, const mp_obj_t * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mpy_uros_msg_are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool mpy_uros_msg_Sequence__copy( const mpy_uros_msg_Sequence * input, mpy_uros_msg_Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(geometry_msgs__msg__Twist);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    geometry_msgs__msg__Twist * data =
      (geometry_msgs__msg__Twist *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mpy_uros_msg_init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mpy_uros_msg_fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mpy_uros_msg_copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
