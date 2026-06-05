/**
 * The MicroROS <-> Micropython Type Support function will support  
 * 
 **/

// https://github.com/gentijo/ROSMicroPy-TypeGen

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#include "py/runtime.h"
#include "py/obj.h"
#include "py/qstr.h"


#include "mp_uros_dataTypeParser.h"
#include "mp_uros_type_support.h"
#include "mp_helpers.h"


bool processComponent(dxc_cb_t *ctrlBlk, mp_obj_t obComponent,  bool debug, bool countOnly);


void         populateSerDeEntries(dxi_t *component, bool debug);


/**
 * Parse the Data Definition schema and create a list of instructions
 * that are needed to serialize / deserialize the data type passed into
 * ROS
*/
mp_obj_t parseDataTypeDefinition(mp_obj_t obj_in, bool debug) {

    dxc_cb_t* ctrlBlk = findAvailTypeSlot();
    if (ctrlBlk == NULL) {
        printf("No Available Type Slots while registering type");
        return mp_const_none;
    }

    // Import the Dict object into a map to locate values.
    mp_map_t *dataMap = mp_obj_dict_get_map(obj_in);

    // This is at the top level, get the general type and the list of components.
    const char *message_name = getStrFieldFromMap(dataMap,  MP_OBJ_NEW_QSTR(MP_QSTR_message_name));
    if (message_name == NULL || strlen(message_name)==0) {
        mp_raise_ValueError(MP_ERROR_TEXT("ROS Type Definition: message_name field is missing a value"));
        return mp_const_none;
    }

    const char *message_namespace = getStrFieldFromMap(dataMap,  MP_OBJ_NEW_QSTR(MP_QSTR_message_namespace));
    if (message_namespace == NULL || strlen(message_namespace)==0) {
         mp_raise_ValueError(MP_ERROR_TEXT("ROS Type Definition: message_namespace field is missing a value"));
        return mp_const_none;
    }

    mp_obj_t obComponentList = getListFieldFromMap(dataMap,  MP_OBJ_NEW_QSTR(MP_QSTR_components));
    if (obComponentList == NULL) {	
        printf("ROS Type Definition requires that one or more components are defined\r\n");
        return mp_const_none;
    } 

    size_t   componentListLen;
    mp_obj_t *componentList;
    mp_obj_list_get(obComponentList, &componentListLen, &componentList);


    ctrlBlk->componentCount=0;

    //
    // Do a countOnly pass to determine how much memory we need to 
    // Allocate for the instruction list
    // This will be a full count and not just a count of top level 
    // components. 
    //
    for (size_t i = 0; i < componentListLen; ++i) {
        mp_obj_t component = componentList[i];
        // Debug passed and only count objects, don't process them
        processComponent(ctrlBlk, component, debug, true);
    }

    dxil_t *dxil = malloc(sizeof(dxil_t));

    //
    // Need some extra space to account for word alignment
    //
    dxil->instructionList = malloc((sizeof(dxi_t)+4) * (ctrlBlk->componentCount+1) );
    dxil->type = strdup(message_name);

    ctrlBlk->type = strdup(message_name);
    ctrlBlk->componentCount=0;
    ctrlBlk->index=1;  // The root instruction is at index 0
    ctrlBlk->dxil = dxil;

     message_type_support_callbacks_t *callbackData = ( message_type_support_callbacks_t *) ctrlBlk->ros_mesg_type_support->data;
     callbackData->message_name_ = strdup(message_name);
     callbackData->message_namespace_ = strdup(message_namespace);

    dxi_t *root_i = &dxil->instructionList[0];
    root_i->isROSType=true;
    root_i->kind = DXI_KIND_ROS_TYPE;
    root_i->type=strdup("Root");
    root_i->name = strdup("Root");
    root_i->name_qstr = qstr_from_str("Root");
    root_i->name_obj = MP_OBJ_NEW_QSTR(root_i->name_qstr);
    root_i->shallowComponentCount=0;
    root_i->instructionEnd=0;


    //
    // Now run through the components and populate the instruction list
    //
    for (size_t i = 0; i < componentListLen; ++i) {
        mp_obj_t component = componentList[i];
        // Process entries on this pass
        processComponent(ctrlBlk, component, debug, false);
        root_i->shallowComponentCount++;
    }
    root_i->instructionEnd = ctrlBlk->componentCount;

    return mp_obj_new_str(message_name, strlen(message_name));
}


/**
 * 
 * 
 * 
*/
bool processComponent(dxc_cb_t *ctrlBlk, mp_obj_t obComponent,  bool debug, bool countOnly) {

    mp_map_t *map = mp_obj_dict_get_map(obComponent);

    const char *type = getStrFieldFromMap(map,  MP_OBJ_NEW_QSTR(MP_QSTR_type)) ;
    if (type == NULL || strlen(type)==0) {
        mp_raise_ValueError(MP_ERROR_TEXT("ROS Type Definition: type field is missing a value"));
        return false;
    }

    const char *name = getStrFieldFromMap(map,  MP_OBJ_NEW_QSTR(MP_QSTR_name)) ;
    if (name == NULL || strlen(name)==0) {
        mp_raise_ValueError(MP_ERROR_TEXT("ROS Type Definition: name field is missing a value"));
        return false;
    }

    const int capicity = getIntFieldFromMap(map,  MP_OBJ_NEW_QSTR(MP_QSTR_capicity)) ;
    const bool isSequence = getBoolFieldFromMap(map, MP_OBJ_NEW_QSTR(MP_QSTR_isSequence));
    const bool isArray = getBoolFieldFromMap(map, MP_OBJ_NEW_QSTR(MP_QSTR_isArray));


    dxi_t *component_inst = NULL;

    //
    //
    // Add instruction fot the instruction block.
    if (!countOnly) {
        component_inst = &ctrlBlk->dxil->instructionList[ctrlBlk->index];

        ctrlBlk->dxil->instructionList[ctrlBlk->index].type=(strdup(type));
        ctrlBlk->dxil->instructionList[ctrlBlk->index].name=(strdup(name));
        ctrlBlk->dxil->instructionList[ctrlBlk->index].name_qstr = qstr_from_str(name);
        ctrlBlk->dxil->instructionList[ctrlBlk->index].name_obj = MP_OBJ_NEW_QSTR(ctrlBlk->dxil->instructionList[ctrlBlk->index].name_qstr);
        ctrlBlk->dxil->instructionList[ctrlBlk->index].capicity=capicity;
        ctrlBlk->dxil->instructionList[ctrlBlk->index].isSequence=isSequence;
        ctrlBlk->dxil->instructionList[ctrlBlk->index].isArray=isArray;
        ctrlBlk->dxil->instructionList[ctrlBlk->index].instructionEnd=ctrlBlk->index;


        ctrlBlk->dxil->instructionList[ctrlBlk->index].islastBlk = false;
        ctrlBlk->dxil->instructionList[ctrlBlk->index].isROSType = false;
        ctrlBlk->dxil->instructionList[ctrlBlk->index].shallowComponentCount = 0;

        populateSerDeEntries(&ctrlBlk->dxil->instructionList[ctrlBlk->index], debug);

        ctrlBlk->index++;
    }

    ctrlBlk->componentCount++;

    //
    // Look for sub components, does this layer define a components section
    //
    mp_obj_t obComponentList = getListFieldFromMap(map,  MP_OBJ_NEW_QSTR(MP_QSTR_components));
    if (obComponentList != NULL) {	

        //
        // Get the list of components at this layer.
        // If a ROSType sub component, the layer will be pushed, then
        // the we will process the sub components of the RUS Type component
        size_t   componentListLen;
        mp_obj_t *componentList;
        mp_obj_list_get(obComponentList, &componentListLen, &componentList);

        if (componentListLen != 0) {

            for (size_t i = 0; i < componentListLen; ++i) {
                mp_obj_t component = componentList[i];
                processComponent(ctrlBlk, component, debug, countOnly);

                // The dxil is not established on the deep count run.
                if(!countOnly){
                    component_inst->shallowComponentCount++;
                }
            }

            if(!countOnly) {
                if (ctrlBlk->index >= 1) {
                    ctrlBlk->dxil->instructionList[(ctrlBlk->index)-1].islastBlk = true; 
                }
                component_inst->instructionEnd = ctrlBlk->index - 1;
            }

        }
    }


    return true;
}

/**
 * 
 * 
 * 
*/
void dumpDataTypeInstruction(dxi_t *inst) {
    printf("Type: [%s]  Name: [%s] IsROSType: [%d] isLastBlk: [%d]  shallow count:[%d]\r\n", 
        inst->type, inst->name, 
        inst->isROSType,
        inst->islastBlk,
        inst->shallowComponentCount
    );
}

/**
 * 
 * 
 * 
*/
void dumpDataTypeMap(mp_obj_t type) {

    if (&mp_type_str != mp_obj_get_type(type)) {
        mp_raise_TypeError(MP_ERROR_TEXT("expecting a str for data type"));
        return;
    }
    
    const char *cstr_type = mp_obj_str_get_str(type);
    if (cstr_type == NULL || strlen(cstr_type) == 0) {
        mp_raise_ValueError(MP_ERROR_TEXT("data type name has zero length"));
        return;
    }
    
    dxc_cb_t *ctrlBlk = findTypeByName(cstr_type);
    if (ctrlBlk == NULL) {
        mp_raise_ValueError(MP_ERROR_TEXT("data type is not registered"));
        return;       
    }

    message_type_support_callbacks_t *callbackData = ( message_type_support_callbacks_t *) ctrlBlk->ros_mesg_type_support->data;

    printf("Type name: %s\r\n", ctrlBlk->type);
    printf("Message Namespace: [%s] Name: [%s]\r\n", callbackData->message_namespace_, callbackData->message_name_ );
    printf("Number of components %d\r\n", ctrlBlk->componentCount);
    printf("Instruction List:\r\n");

    // +1 to include root instruction
    for (int x=0; x< ctrlBlk->componentCount+1; x++) {
        dumpDataTypeInstruction(&ctrlBlk->dxil->instructionList[x]);
    }
}




/**
 * Based on the Type defined in the Data Map, assign the proper Serializer / Deserializer to the Instruction block.
 * This assignment is different for every component / field defined in the dataMap.
 * If the Type is of a ROS type, i.e. Twist, Vector3, those will be treated as a placeholder for the subcomponents. 
 * i.e. a Vector3 is a placeholder for 3 Doubles. 
*/
void populateSerDeEntries(dxi_t *component, bool debug) {
    (void)debug;

    if (component == NULL) return;
    char *type = component->type;
    if (type == NULL) return;
    if (strlen(type) == 0) return;

    component->isROSType = false;

    if (strcmp("bool", type) == 0) {
        component->kind = DXI_KIND_BOOL;
        component->serialize = serializeBool;
        component->deserialize = deserializeBool;
        component->serializedSize = serializedSizeBool;
        return;
    }


    if (strcmp("byte", type) == 0)     {
        component->kind = DXI_KIND_BYTE;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }

    if (strcmp("char", type) == 0)     {
        component->kind = DXI_KIND_CHAR;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }

    if (strcmp("int8", type) == 0)     {
        component->kind = DXI_KIND_INT8;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    } 
  
    if (strcmp("uint8", type) == 0)    {
        component->kind = DXI_KIND_UINT8;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }
    
    if (strcmp("int16", type) == 0)    {
        component->kind = DXI_KIND_INT16;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }
    
    if (strcmp("uint16", type) == 0)   {
        component->kind = DXI_KIND_UINT16;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return; 
    }
    
    if (strcmp("int32", type) == 0)    {
        component->kind = DXI_KIND_INT32;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }
    
    if (strcmp("uint32", type) == 0)   {
        component->kind = DXI_KIND_UINT32;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
    
        return; 
    }
    
    if (strcmp("int64", type) == 0)    {
        component->kind = DXI_KIND_INT64;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;
        component->serializedSize = serializedSizeInt;
        return;
    }

    if (strcmp("uint64", type) == 0)   {
        component->kind = DXI_KIND_UINT64;
        component->serialize = serializeInt;
        component->deserialize = deserializeInt;    
        component->serializedSize = serializedSizeInt;
        return;
    }
    
    if (strcmp("float32", type) == 0)  {
        component->kind = DXI_KIND_FLOAT32;
        component->serialize = serializeFloat;
        component->deserialize = deserializeFloat;
        component->serializedSize = serializedSizeFloat;
        return;        
    }
    
    if (strcmp("float64", type) == 0)  {
        component->kind = DXI_KIND_FLOAT64;
        component->serialize = &serializeFloat;
        component->deserialize = &deserializeFloat;
        component->serializedSize = serializedSizeFloat;
        return;
    }      

    if (strcmp("double", type) == 0)  {
        component->kind = DXI_KIND_FLOAT64;
        component->serialize = &serializeDouble;
        component->deserialize = &deserializeDouble;
        component->serializedSize = serializedSizeDouble;
        return;
    }    

    if (strcmp("string", type) == 0)  {
        component->kind = DXI_KIND_STRING;
        component->serialize = &serializeString;
        component->deserialize = &deserializeString;
        component->serializedSize = serializedSizeString;
        return;
    }

    component->serialize = &serializeROSType;
    component->deserialize = &deserializeROSType;
    component->serializedSize = serializedSizeROSType;
    component->isROSType = true;
    component->kind = DXI_KIND_ROS_TYPE;
    return;
       
}
