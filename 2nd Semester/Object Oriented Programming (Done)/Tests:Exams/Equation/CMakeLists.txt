cmake_minimum_required(VERSION 3.7)
project(Equation)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        Equation.cpp
        Equation.h
        Repository.h
        Repository.cpp Controller.cpp Controller.h Ui.cpp Ui.h)

find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(Equation ${SOURCE_FILES})

target_link_libraries(Equation Qt5::Widgets)