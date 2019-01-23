//
//  HospitalDepartment.hpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <string>
#include <sstream>
#include <iostream>
#include <exception>
#include <vector>

using namespace std;


class HospitalDepartment{
private:
    string HospitalName;
    int NoOfDoctors;
public:
    HospitalDepartment();
    ~HospitalDepartment();
    
    virtual bool isEfficient() = 0 ;
    virtual string toString() = 0;
};
