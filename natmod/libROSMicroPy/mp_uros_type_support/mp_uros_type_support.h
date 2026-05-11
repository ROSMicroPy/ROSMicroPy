#ifndef __MP_UROS_TYPE_SUPPORT_H__
#define __MP_UROS_TYPE_SUPPORT_H__

#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "rosidl_typesupport_microxrcedds_c/identifier.h"
//#include "rosidl_typesupport_microxrcedds_c/message_type_support.h"
#include "mp_uros_type_support_visibility_control.h"

#include "mp_uros_sdk.h"

#include "mp_uros_dataTypeParser.h"

#include <ucdr/microcdr.h>
#include "py/obj.h"

#define MICROXRCEDDS_PADDING sizeof(uint32_t)


void init_mpy_ROS_TypeSupport(void); 
dxc_cb_t* findAvailTypeSlot();
dxc_cb_t* findTypeByName(const char *type);

void serializeBool(ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
void deserializeBool(ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
size_t serializedSizeBool(const void *mp_obj, size_t current_alignment);

void serializeInt(ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
void deserializeInt(ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
size_t serializedSizeInt(const void *mp_obj, size_t current_alignment);

void serializeFloat(ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
void deserializeFloat(ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
size_t serializedSizeFloat(const void *mp_obj, size_t current_alignment);

void deserializeDouble(ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
void serializeDouble(ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
size_t serializedSizeDouble(const void *mp_obj, size_t current_alignment);

void deserializeROSType(ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
void serializeROSType(ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
size_t serializedSizeROSType(const void *mp_obj, size_t current_alignment);


#endif