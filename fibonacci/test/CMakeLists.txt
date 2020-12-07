cmake_minimum_required(VERSION 3.10)

include(GoogleTest)

enable_language(CXX)

add_executable(fibonacci_test src/tests.cpp)
target_compile_features(fibonacci_test PRIVATE cxx_std_11)
target_link_libraries(fibonacci_test ${CONAN_LIBS} fibonacci)

gtest_discover_tests(fibonacci_test)
