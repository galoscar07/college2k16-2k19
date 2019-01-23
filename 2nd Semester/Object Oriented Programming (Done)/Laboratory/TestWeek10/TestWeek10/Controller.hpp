//
//  Controller.hpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include "HospitalDepartment.hpp"
#include <vector>

class Controller
{
private:
    std::vector<HospitalDepartment*> hospitals;
public:
    Controller();
    ~Controller();
    
};

