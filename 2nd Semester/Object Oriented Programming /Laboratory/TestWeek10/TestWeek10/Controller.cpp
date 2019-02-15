//
//  Controller.cpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Controller.hpp"

Controller::Controller()
{
}

Controller::~Controller()
{
}

void Controller::addDepartment(HospitalDepartment* d){
    hospitals.push_back(d);
}
std::vector<HospitalDepartment*> Controller::getAllDepartments() const{
    return this->hospitals
}
