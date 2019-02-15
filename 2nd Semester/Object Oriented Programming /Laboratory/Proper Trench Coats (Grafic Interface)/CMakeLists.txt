cmake_minimum_required(VERSION 3.7)
project(Proper_Trench_Coats_Lab_11_12)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        Coat.cpp
        Coat.h
        Utils.cpp
        Utils.h
        Basket.cpp
        Basket.h
        Controller.cpp
        Controller.h
        CSVBasket.cpp
        CSVBasket.h
        FileBasket.cpp
        FileBasket.h
        HTMLBasket.cpp
        HTMLBasket.h
        Validators.cpp
        Validators.h
        Repository.cpp
        Repository.h
        RepositoryExceptions.cpp
        RepositoryExceptions.h
        Ui.cpp
        Ui.h
        Coats.txt BasketQt.cpp BasketQt.h)

find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(Proper_Trench_Coats_Lab_11_12 ${SOURCE_FILES})

target_link_libraries(Proper_Trench_Coats_Lab_11_12 Qt5::Widgets)