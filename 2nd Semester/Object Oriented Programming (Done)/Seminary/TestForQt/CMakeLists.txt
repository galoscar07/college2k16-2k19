cmake_minimum_required(VERSION 3.7)
project(TestForQt)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        Controller.h
        Controller.cpp
        CSVPlaylist.h
        CSVPlaylist.cpp
        FilePlaylist.h
        FilePlaylist.cpp
        PlayList.h
        PlayList.cpp
        playlistqt.h
        playlistqt.cpp
        Repository.h
        Repository.cpp
        RepositoryExceptions.h
        RepositoryExceptions.cpp
        Song.h
        Song.cpp
        SongValidator.h
        SongValidator.cpp
        Undo.h
        Utils.h
        Utils.cpp)

find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(TestForQt ${SOURCE_FILES})

target_link_libraries(TestForQt Qt5::Widgets)