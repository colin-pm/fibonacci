cmake_minimum_required(VERSION 3.13)

project(fibonacci LANGUAGES CXX)

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

add_subdirectory("fibonacci")
add_subdirectory("docs")