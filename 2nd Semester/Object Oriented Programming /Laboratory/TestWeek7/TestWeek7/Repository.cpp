//
//  Repository.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Repository.hpp"
#include <string>
#include <assert.h>

using namespace std;

void Repository::addGenes(const Genes& g){
    this->geneses.add(g);
}

Genes Repository::findByName(const std::string& name){
    Genes* genesInVector = this->geneses.getAllElems();
    if (genesInVector == NULL)
        return Genes{};
    
    for (int i = 0; i < this->geneses.getSize(); i++){
        Genes c = genesInVector[i];
        if (c.getName() == name)
            return c;
    }
    return Genes{};
}
