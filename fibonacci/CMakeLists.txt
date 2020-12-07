include(CTest)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

set(CODE_COVERAGE "NO" CACHE STRING "If code coverage analysis is enabled")

add_compile_options("--coverage")
add_link_options("--coverage")

add_library(fibonacci src/fibonacci.cpp include/fibonacci.h)
target_link_libraries(fibonacci ${CONAN_LIBS})
target_include_directories(fibonacci PUBLIC include)
target_compile_features(fibonacci PRIVATE cxx_std_11)

include_directories("include")

if(BUILD_TESTING)
    add_subdirectory("test")
endif()