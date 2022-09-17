cmake_minimum_required(VERSION 3.10)

set(LibraryName MyModule)

# Create library
add_library(${LibraryName}
    my_class.h my_class.cpp
)

target_include_directories(${LibraryName} PUBLIC ./)    # add public so that test module can include header files
