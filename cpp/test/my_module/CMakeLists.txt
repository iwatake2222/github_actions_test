cmake_minimum_required(VERSION 3.10)

set(TestName TestMyModule)

# Create test
add_executable(${TestName}
    test_my_class.cpp
)

# Link to gtest_main to call test cases
target_link_libraries(${TestName} gtest_main gmock_main)
gtest_discover_tests(${TestName})

# Link to the target module
target_link_libraries(${TestName} MyModule)
