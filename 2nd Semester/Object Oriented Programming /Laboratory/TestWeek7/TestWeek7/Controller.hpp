//
//  Controller.hpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Repository.hpp"
#include <assert.h>

class Controller{
private:
    Repository repo;
public:
    Controller(const Repository& r) : repo(r) {}
    Repository getRepo() const { return repo; }
    /*
     This function will add a Genes into the repository list of elements.
     Input: as input the function got 3 variables, all of them beeing strings 
     Output: The function will return o if the Genes wasn't added and 1 otherwise.
    */
    int addGenesC(const std::string& name, const std::string& organism,const std::string& sequence);
};
