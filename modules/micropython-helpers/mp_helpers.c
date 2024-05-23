#include "mp_helpers.h"


mp_map_elem_t* getElementFromMap(mp_map_t *dataMap, mp_obj_t fieldName) {

    return  mp_map_lookup(dataMap, fieldName, MP_MAP_LOOKUP);   
}

/**
 * From a map, look for a field by name, verify it's type to be a list
 * and return that object.  If the object is not found or is not of Type
 * list, then return a NULL value
 * 
*/
mp_obj_list_t* getListFieldFromMap(mp_map_t *dataMap, mp_obj_t fieldName) {
    mp_map_elem_t *obComponents = getElementFromMap(dataMap, fieldName);   
    if (obComponents == NULL) {	
        return NULL;
    }

    //
    // Make sure the type passed in for the Component list is of type list.
    //
    mp_obj_list_t* obComponentList = obComponents->value;  
    if (obComponentList == mp_const_none) {	
        return NULL;
    }

    if (&mp_type_list != mp_obj_get_type(obComponentList) ) {
        return NULL;
    }

    if (obComponentList->len == 0 ) {
        return NULL;
    }

    return obComponentList;
}

/**
 * 
 * From a map look for a field named y fieldName, verify it's value
 * is a str and return a C compatible string. If the field is not
 * found or it is not dict_iterof type Str then return NULL
 * 
*/
const char * getStrFieldFromMap(mp_map_t *dataMap, mp_obj_t fieldName) {

    mp_map_elem_t *obElem = getElementFromMap(dataMap, fieldName);   
    if (obElem == NULL) {	
        return NULL;
    }

    mp_obj_t obField = obElem->value;
    if (&mp_type_str != mp_obj_get_type(obField)) {
        return NULL;
    }

    return mp_obj_str_get_str(obField);
}