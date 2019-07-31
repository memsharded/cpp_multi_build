#include "hello.h"

std::string hello(){
    #ifdef NDEBUG
    return  "Hello World Release!";
    #else
    return  "Hello World Debug!";
    #endif
}