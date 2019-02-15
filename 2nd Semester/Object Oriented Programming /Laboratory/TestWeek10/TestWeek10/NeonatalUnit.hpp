//
//  NeonatalUnit.hpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "HospitalDepartment.hpp"

using namespace std;

class NeonatalUnit : public HospitalDepartment{
private:
    int numberOfMothers;
    int numberOfNewborns;
    double averageGrade;
public:
    NeonatalUnit();
    NeonatalUnit(int numberOfMothers, int numberOfNewborns, double averageGrade);
    ~NeonatalUnit();
    
    bool isEfficient() override;
    string toString() override;
};

