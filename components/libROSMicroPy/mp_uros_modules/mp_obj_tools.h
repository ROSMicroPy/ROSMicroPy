#ifndef __MP_OBJ_TOOLS_H__
#define __MP_OBJ_TOOLS_H__

#include "py/runtime.h"

mp_obj_t mpt_getNamedObjFrom(mp_obj_t obj_in, qstr attr);
mp_obj_t mpt_getObjFromByIndex(mp_obj_t objin, size_t index);
char *mpt_obj_to_cstr(mp_obj_t objin);
mp_obj_t parseDataMapDict(mp_obj_t dict);

#endif