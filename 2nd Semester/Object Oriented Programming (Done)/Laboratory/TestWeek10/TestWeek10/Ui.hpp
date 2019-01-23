//
//  Ui.hpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Controller.hpp"

class Ui{
private:
    Controller controller;
public:
    Ui(Controller cont) { controller = cont; };
    ~Ui();
    
    void run();
    void printMenu();
    void addDepartment();
    void listHospitals();
    void showAllEfficient();
    void saveToFile();
    
};

