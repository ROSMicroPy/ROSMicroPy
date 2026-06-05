#ifndef __MP_UROS_DATATYPEPARSER_h__
#define __MP_UROS_DATATYPEPARSER_h__


#include "py/runtime.h"
#include "py/obj.h"
#include "py/qstr.h"
#include <ucdr/microcdr.h>

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_microxrcedds_c/identifier.h"
#include "rosidl_typesupport_microxrcedds_c/message_type_support.h"
#include "mp_uros_type_support_visibility_control.h"

/**
 * When Serializing or deserializing, we need to maintain the parent child
 * relationship, the Stack will help create a tracker to hold the current
 * object.  i.e. In a Geometry_Twist deserialization, we 
*/

#define mp_obj_stack_size 5
typedef struct mp_obj_stack {
  mp_obj_t  objects[mp_obj_stack_size];
  size_t    stkPtr;
} mp_obj_stk_t;


typedef struct dataXferInst dxi_t;

typedef enum dataXferKind {
    DXI_KIND_UNSUPPORTED = 0,
    DXI_KIND_BOOL,
    DXI_KIND_BYTE,
    DXI_KIND_CHAR,
    DXI_KIND_INT8,
    DXI_KIND_UINT8,
    DXI_KIND_INT16,
    DXI_KIND_UINT16,
    DXI_KIND_INT32,
    DXI_KIND_UINT32,
    DXI_KIND_INT64,
    DXI_KIND_UINT64,
    DXI_KIND_FLOAT32,
    DXI_KIND_FLOAT64,
    DXI_KIND_STRING,
    DXI_KIND_ROS_TYPE,
} dxi_kind_t;

struct dataXferInst {
    char *type;
    char *name;
    qstr name_qstr;
    mp_obj_t name_obj;
    dxi_kind_t kind;
    bool islastBlk;
    bool isROSType;
    int  shallowComponentCount;
    bool isSequence;
    bool isArray;
    int  capicity;
    int  instructionEnd;

    void (*deserialize) (ucdrBuffer *cdr,   dxi_t* inst, mp_obj_stk_t *obj_stack);
    void (*serialize)   (ucdrBuffer *cdr,  mp_obj_t value, dxi_t* inst);
    size_t (*serializedSize) (const void *mp_obj, size_t current_alignment);

};


typedef struct dataXferInst_List {
    char    *type;
    size_t  component_len;
    dxi_t   *instructionList;
} dxil_t;



typedef struct DataXferCompiler_CtrlBlock {
    char    *type;
    dxil_t  *dxil;
    rosidl_message_type_support_t *ros_mesg_type_support;
    size_t componentCount;
    // Current index into the DXIL when populating the instruction list
    size_t index;
} dxc_cb_t;



mp_obj_t parseDataTypeDefinition(mp_obj_t obj_in, bool debug);

void dumpDataTypeMap(mp_obj_t type);


#endif
