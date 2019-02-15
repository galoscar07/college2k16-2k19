//
// Created by Gal Oscar on 23/05/2017.
//

#include "Basket.h"
#include <assert.h>

Basket::Basket() {
    this->current = 0;
    this->money = 0;

}

void Basket::add(Coat coat){
    int z = -1;
    int nr = -1;
    for (auto &i : this->coats){
        nr++;
        if (i.getId() == coat.getId()){
            z = 0;
            break;
        }
    }
    if (z == -1){
        this->coats.push_back(coat);
    }
    else{
        Coat c = this->coats[nr];
        c.setQuantity(c.getQuantity() + 1);
        this->coats[nr] = c;
    }
    this->money = this->money + coat.getPrice();
}

Coat Basket::getCurrentCoat(){
    if (this->current == this->coats.size())
        this->current = 0;
    return this->coats[this->current];
}

Coat Basket::next()
{
    if (this->coats.size() == 0)
        return Coat();
    this->current++;
    Coat currentCoat = this->getCurrentCoat();
    return currentCoat;
}

float Basket::getMoney(){
    return this->money;
}
