

#ifndef MPY_UROS_MSGS_MSG_FUNCTIONS_H_
#define MPY_UROS_MSGS_MSG_FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "rcutils/allocator.h"

#include "py/runtime.h"
#include "uros_support.h"


bool mpy_uros_msg_init(mp_obj_t *msg);
void mpy_uros_msg_fini(mp_obj_t * msg);


bool mpy_uros_msg_are_equal(const mp_obj_t *lhs, const mp_obj_t *rhs);

bool mpy_uros_msg_copy(const mp_obj_t * input, mp_obj_t *output);
mp_obj_t *mpy_uros_msg_create();
void mpy_uros_msg_destroy(mp_obj_t * msg);

bool mpy_uros_msg_Sequence__init(mp_obj_t * array, size_t size);
void mpy_uros_msg_Sequence__fini(mp_obj_t * array);

// mpy_uros_msg_Sequence *mpy_uros_msg_Sequence__create(size_t size);
// void mpy_uros_msg_Sequence__destroy(mp_obj_t * array);
// bool mpy_uros_msg_Sequence__are_equal(const mp_obj_t * lhs, const mp_obj_t * rhs);
// bool mpy_uros_msg_Sequence__copy( const mpy_uros_msg_Sequence * input, mpy_uros_msg_Sequence * output);

#endif
