cmake_minimum_required(VERSION 3.7)
project(Testing)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        mainwindow.cpp
        mainwindow.h
        mainwindow.ui
        Tester.pro
        Tester.pro.user
        )

find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(Testing ${SOURCE_FILES})

target_link_libraries(Testing Qt5::Widgets)