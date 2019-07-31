#include "hello.h"

std::string hello(){
    #ifdef 	_M_IX86
        #ifdef NDEBUG
        return  "Hello World Release 32bits!";
        #else
        return  "Hello World Debug 32bits!";
        #endif
    #else
        #ifdef NDEBUG
        return  "Hello World Release!";
        #else
        return  "Hello World Debug!";
        #endif
    #endif
}