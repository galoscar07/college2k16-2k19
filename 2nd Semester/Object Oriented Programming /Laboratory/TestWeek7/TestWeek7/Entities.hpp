//
//  Entities.hpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <iostream>

class Genes{
private:
    std::string name;
    std::string organism;
    std::string sequence;
public:
    Genes(); // default constructor
    Genes(const std::string& name, const std::string& organism, const std::string& sequence);
    
    std::string getName() const {return name;}
    std::string getOrganism() const {return organism;}
    std::string getSequence() const {return sequence;}
    
};
