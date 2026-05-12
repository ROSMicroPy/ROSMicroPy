/**
 * mp_obj_tools is a collection of functions that support interfacing MicroROS
 * with objects/variables in MicroPython.
 */

#include <stddef.h>

#include "py/obj.h"
#include "py/runtime.h"
#include "mp_obj_tools.h"

mp_obj_t mpt_getNamedObjFrom(mp_obj_t obj_in, qstr attr)
{
    if (mp_obj_is_type(obj_in, &mp_type_dict)) {
        mp_map_t *named_map = mp_obj_dict_get_map(obj_in);
        mp_map_elem_t *named_elem = mp_map_lookup(named_map, MP_OBJ_NEW_QSTR(attr), MP_MAP_LOOKUP);
        if (named_elem != NULL) {
            return named_elem->value;
        }
        return mp_const_none;
    }

    return mp_load_attr(obj_in, attr);
}

mp_obj_t mpt_getObjFromByIndex(mp_obj_t objin, size_t index)
{
    size_t len = 0;
    mp_obj_t *items = NULL;

    mp_obj_get_array(objin, &len, &items);
    if (index >= len) {
        return mp_const_none;
    }
    return items[index];
}

char *mpt_obj_to_cstr(mp_obj_t objin)
{
    return (char *)mp_obj_str_get_str(objin);
}

mp_obj_t parseDataMapDict(mp_obj_t dict)
{
    mp_map_t *named_map = mp_obj_dict_get_map(dict);
    mp_map_elem_t *named_elem = mp_map_lookup(named_map, MP_OBJ_NEW_QSTR(MP_QSTR_type), MP_MAP_LOOKUP);

    if (named_elem != NULL) {
        return named_elem->value;
    }
    return mp_const_none;
}
