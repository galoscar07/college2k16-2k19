//
//  Ui.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Controller.hpp"

class Console{
private:
    AdminController admin;
public:
    Console(const AdminController& c) : admin(c) {};
    void run();
    
private:
    //for printing
    static void printMenu();
    static void printAdminMenu();
    static void printUserMenu();
    static void printFilterBySizeMenu();
    static void printCoat(const Coat& c);
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
