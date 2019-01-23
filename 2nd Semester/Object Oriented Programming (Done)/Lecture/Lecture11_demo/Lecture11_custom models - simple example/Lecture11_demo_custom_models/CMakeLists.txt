cmake_minimum_required(VERSION 3.7)
project(Lecture11_demo_custom_models)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        Controller.cpp
        Controller.h
        CSVPlaylist.cpp
        CSVPlaylist.h
        FilePlaylist.cpp
        FilePlaylist.h
        PlayList.cpp
        PlayList.h
        playlistqt.cpp
        playlistqt.h
        Repository.cpp
        Repository.h
        RepositoryExceptions.cpp
        RepositoryExceptions.h
        Song.cpp
        Song.h
        SongValidator.cpp
        SongValidator.h
        Undo.h
        Utils.cpp
        Utils.h
        Songs.txt)

find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(Lecture11_demo_custom_models ${SOURCE_FILES})

target_link_libraries(Lecture11_demo_custom_models Qt5::Widgets)