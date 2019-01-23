//
//  Ui.hpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Controller.hpp"

class Ui{
private:
    Controller contr;
public:
    Ui(const Controller& c) : contr(c) {}
    void run();
    
private:
    static void printMenu();
    void addGenesToRepo();
    void displayAllGenesesRepo();
};
