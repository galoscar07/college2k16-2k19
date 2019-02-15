//
//  Surgery.hpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "HospitalDepartment.hpp"

using namespace std;

class Surgery : public HospitalDepartment{
private:
    int numberOfPatients;
public:
    Surgery();
    Surgery(int numberOfPatients);
    ~Surgery();
    
    bool isEfficient() override;
    string toString() override;
};
