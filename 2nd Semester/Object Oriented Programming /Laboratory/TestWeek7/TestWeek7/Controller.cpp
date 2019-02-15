//
//  Controller.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Controller.hpp"

int Controller::addGenesC(const std::string& name, const std::string& organism,const std::string& sequence){
    Genes g{ name,  organism, sequence};
    Genes a = this->repo.findByName(name);
    if ((a.getName() != "") && (a.getOrganism() != ""))
        return 0;
    this->repo.addGenes(g);
    return 1;
}

