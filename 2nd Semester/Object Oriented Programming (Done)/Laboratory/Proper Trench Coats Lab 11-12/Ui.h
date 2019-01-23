//
// Created by Gal Oscar on 26/05/2017.
//

#pragma once
#include "Controller.h"

class Console{
private:
    Controller contr;
public:
    Console(const Controller& c) : contr(c) {};
    void run();

private:
    //for printing
    static void printMenu();
    static void printAdminMenu();
    static void printUserMenu();
    static void printFilterBySizeMenu();
    static void printCoat(Coat& c);
    //admin interface
    void addCoatToRepo();
    void removeCoatFromRepo();
    void updateCoatInRepo();
    void displayAllCoatsRepo();
    void filterCoatsByLength();
    //user interface
    void filterBySize();
    void showCart();
};
