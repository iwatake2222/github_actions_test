cmake_minimum_required(VERSION 3.10)

# Include GoogleTest
set(gtest_as_submodule ON)
if(gtest_as_submodule)
    set(GTest_DIR ${CMAKE_CURRENT_SOURCE_DIR}/third_party/googletest)
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    add_subdirectory(${GTest_DIR})
    include(GoogleTest)
else()
    include(FetchContent)
    FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/tags/release-1.12.1.zip
    )
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)
    include(GoogleTest)
endif()
set(INSTALL_GTEST OFF CACHE BOOL "" FORCE)

# Compile option (re-do this, because GoogleTest seems to set CMAKE_CXX_STANDARD to 11)
include(${CMAKE_SOURCE_DIR}/cmakes/compile_option.cmake)

# Add test modules
add_subdirectory(./main)
add_subdirectory(./my_module)
