//
//  Repository.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Repository.hpp"
#include <string>

using namespace std;

void Repository::addCoat(const Coat& c){
    this->coats.add(c);
}

Coat Repository::findById(const int&id){
    Coat* coatsInVector = this->coats.getAllElems();
    if (coatsInVector == NULL)
        return Coat{};
    
    for (int i = 0; i < this->coats.getSize(); i++)
    {
        Coat c = coatsInVector[i];
        if (c==(id))
            return c;
    }
    return Coat{};
}

void Repository::removeCoat(const int & id){
    int i;
    Coat * c = this->coats.getAllElems();
    for (i = 0; i < this->coats.getSize(); i++)
    {
        if (c[i].getId() == id) {
            this->coats.remove(i);
            break;
        }
    }
}

void Repository::updateCoat(const int & id, const float & price, const int & quantity){
    Vector &v = this->coats;
    if (price > 0) {
        for (int i = 0; i < this->getCoats().getSize(); i++) {
            if (v.get(i).getId() == id) {
                v.get(i).setPrice(price);
                break;
            }
        }
    }
    if (quantity > 0) {
        for (int i = 0; i < this->getCoats().getSize(); i++) {
            if (v.get(i).getId() == id) {
                v.get(i).setQuantity(quantity);
                break;
            }
        }
    }
}




