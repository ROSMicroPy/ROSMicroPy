#include <errno.h>

int setenv(const char *name, const char *value, int overwrite) {
    (void)name;
    (void)value;
    (void)overwrite;
    errno = ENOSYS;
    return -1;
}

int unsetenv(const char *name) {
    (void)name;
    errno = ENOSYS;
    return -1;
}
