//
//  Controller.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Controller.hpp"
#include <iostream>

void Controller::addCoatToRepo(const int& id, const int& size, const std::string& color, const float& price, const int& quantity, const std::string& photo, const float& length){
    Coat c{ id,  size, color, price, quantity, photo, length };
    this->validators.validate(c);
    this->repo.addCoat(c);
}

void Controller::removeCoatFromRepo(const int & id){
    Coat c = Coat(id, 0, "", 0, 0, "", 0);
    this->validators.validate(c);
    this->repo.removeCoat(c);
}

void Controller::updateCoatInRepo(const int & id, const float & price, const int & quantity){
    Coat c = Coat(id, 0, "", price, quantity, "", 0);
    this->validators.validate(c);
    this->repo.updateCoat(c);
}

std::vector<Coat> Controller::filterBySize(const int& size){
    std::vector<Coat> r;
    for (auto c: this->getRepo().getCoats()){
        if (c.getSize() == size)
                r.push_back(c);
    }
    return r;
}

void Controller::addCoatToBasket(Coat& coat){
    this->basketList->add(coat);
}

std::vector<Coat> Controller::filterCoatsByLength(const float& length){
    std::vector<Coat> r;
    for (auto c: this->getRepo().getCoats()){
        if (c.getLength() < length)
            r.push_back(c);
    }
    return r;
}

float Controller::getMoney(){
    return this->basketList->getMoney();
}
    
