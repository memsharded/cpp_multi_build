set(CMAKE_CXX_COMPILER_WORKS 1)
set(CMAKE_CXX_ABI_COMPILED 1)

project(HelloWorld CXX)

add_library(hello hello.cpp)
add_executable(app app.cpp)
target_link_libraries(app hello)