cmake_minimum_required(VERSION 3.7)
project(Lecture_11_run)


set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
                socks.txt
                socks_test.txt
                cmake-build-debug/main.cpp
                Console.cpp
                Console.hpp
                Controller.cpp
                Controller.hpp
                Exceptions.cpp
                Repository.cpp
                Repository.hpp
                Socks.cpp
                Socks.hpp
                Tests.cpp
                Tests.hpp
                GUI.cpp
                GUI.hpp)


find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

set(SOURCE_FILES cmake-build-debug/main.cpp)

add_executable(Lecture_11_run ${SOURCE_FILES})

target_link_libraries(Lecture_11_run Qt5::Widgets)