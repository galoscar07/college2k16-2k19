//
//  Entities.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Entities.hpp"

Genes::Genes(): name(""), organism(""), sequence("") {}
Genes::Genes(const std::string& name, const std::string& organism, const std::string& sequence){
    this->name = name;
    this->organism = organism;
    this->sequence = sequence;
}
