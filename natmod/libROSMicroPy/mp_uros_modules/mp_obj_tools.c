/**
 * mp_obj_tools is a collection of functions that support interfacing MicroROS 
 * with the objects/variables in Micropython
*/

#include "py/runtime.h"
#include "mp_obj_tools.h"

typedef struct _mp_obj_enumerate_t {
    mp_obj_base_t base;
    mp_obj_t iter;
    mp_int_t cur;
} mp_obj_enumerate_t;


/**
 * 
 * Retrieve an object by Name from a collection
 * 
*/
mp_obj_t mpt_getNamedObjFrom(mp_obj_t obj_in, qstr attr)
{   
    mp_obj_type_t *type;
    char * type_str;
    mp_map_t *named_map;
    mp_map_elem_t *named_elem;

    size_t   data_map_len;
    mp_obj_t *data_map_items;

    printf("\r\nTest Func1\r\n");
    type = mp_obj_get_type(obj_in);
    type_str = qstr_str(type->name);

    printf("Obj_in type %s\r\n", type_str);
    if (type->name == MP_QSTR_list)
    {
        printf("Printing list objects");
        void mp_obj_get_array(mp_obj_t o, size_t *len, mp_obj_t **items) {
        mp_obj_list_get(obj_in, &data_map_len, &data_map_items);
        for (size_t i = 0; i < data_map_len; ++i) {
            mp_obj_t data_item = data_map_items[i];
            
            char * key = mp_obj_get_type_str(data_item);
            printf("Key type: %s\r\n", key);

            // key = mp_obj_str_get_str(data_item->key);
            // value = mp_obj_str_get_str(data_item->value);
            // printf("Value type: %s  Key type: %s\r\n", value, key);
        }
    }
    else
    {
        mp_map_t *named_map = mp_obj_dict_get_map(obj_in);
        mp_map_elem_t *named_elem = mp_map_lookup(named_map, attr, MP_MAP_LOOKUP);

        // size_t   data_map_len;
        // mp_obj_t *data_map_items;
        // mp_obj_list_get(obj_in, &data_map_len, &data_map_items);
        // for (size_t i = 0; i < data_map_len; ++i) {
        //      mp_obj_t data_map_elem = data_map_items[i];
        //      type = mp_obj_get_type(data_map_elem);
        //      type_str = qstr_str(type->name);
    }

    return NULL;
}

/**
 * 
 * 
*/
mp_obj_t mpt_getObjFromByIndex(mp_obj_t objin, size_t index)
{
    return NULL;
}

/**
 * 
 * 
*/
char *mpt_obj_to_cstr(mp_obj_t objin)
{
    return NULL;
}



const mp_obj_base_t *type_obj;
const mp_obj_type_t *type;
const char * type_str;

const mp_obj_base_t *name_obj;
const mp_obj_type_t *name;
const char * name_str;

mp_obj_base_t *objptr;
const mp_obj_base_t *type_obj;

mp_obj_t dict_map_elem;

//    self->data = mp_obj_dict_get(uasyncio_context, MP_OBJ_NEW_QSTR(MP_QSTR_CancelledError));

mp_obj_t parseDataMapDict(mp_obj_t dict) {

    mp_map_t *named_map = mp_obj_dict_get_map(dict);
    
    mp_map_elem_t *type = mp_map_lookup(named_map, MP_OBJ_NEW_QSTR(MP_QSTR_type), MP_MAP_LOOKUP);


    if (named_elem != NULL && named_elem->value != NULL) {

        char * key = mp_obj_get_type_str(named_elem->key );
        char * value = mp_obj_get_type_str( named_elem->value );
        printf("Value type: %s  Key type: %s\r\n", value, key);

        key = mp_obj_str_get_str(named_elem->key);
        value = mp_obj_str_get_str(named_elem->value);
        printf("Value type: %s  Key type: %s\r\n", value, key);

        return named_elem->value;
         
    }
    return NULL;
}





    // mp_obj_t data_map = mp_load_attr(eventType, MP_QSTR_dataMap);
    // size_t   data_map_len;
    // mp_obj_t *data_map_items;
    
    // type = mp_obj_get_type(data_map);
    // type_str = qstr_str(type->name);
    // printf ("Type: %s\r\n", type_str);
    
    // mp_obj_list_get(data_map, &data_map_len, &data_map_items);
    // for (size_t i = 0; i < data_map_len; ++i) {
    //     mp_obj_t data_map_elem = data_map_items[i];
    //     type = mp_obj_get_type(data_map_elem);
    //     type_str = qstr_str(type->name);

    //     parseDataMapDict(data_map_elem);
    // }

    // mp_obj_t obj_out = mp_load_attr(obj_in, attr);
    // size_t data_map_len;
    // mp_obj_t *data_map_items;
    
    // type = mp_obj_get_type(obj_in);
    // type_str = qstr_str(type->name);
    // printf ("Type: %s\r\n", type_str);
    
    // mp_obj_list_get(obj_in, &data_map_len, &data_map_items);

    // for (size_t i = 0; i < data_map_len; ++i) {
    //     mp_obj_t data_map_elem = data_map_items[i];
    //     type = mp_obj_get_type(data_map_elem);
    //     type_str = qstr_str(type->name);

    //     parseDataMapDict(data_map_elem);
    // }
