//
//  Repository.hpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Vector.hpp"

class Repository{
private:
    Vector geneses;
    
public:
    Repository() {}
    void addGenes(const Genes& g);
    Genes findByName(const std::string& name);
    Vector getGenes() const { return geneses; }
};
