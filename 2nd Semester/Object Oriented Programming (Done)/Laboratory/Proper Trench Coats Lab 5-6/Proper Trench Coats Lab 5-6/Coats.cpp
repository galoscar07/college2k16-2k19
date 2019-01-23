//
//  Coats.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Coats.hpp"

Coat::Coat() : id(-1), size(0), color(""), price(0), quantity(0), photo("") {}

Coat::Coat(const int& id, const int& size, const std::string& color, const float& price, const int& quantity, const std::string& photo, const float& length){
    this->id = id;
    this->size = size;
    this->color = color;
    this->price = price;
    this->quantity = quantity;
    this->photo = photo;
    this->length = length;
}

void Coat::setPrice(const float & price){
    this->price = price;
}

void Coat::setQuantity(const int & quantity){
    this->quantity = quantity;
}

bool Coat::operator==(const int& value) const{
    if (this->id == value) {
        return true;
    }
    else return false;
}

bool Coat::operator<(const int& value) const{
    if (this->length < value){
        return true;
    }
    else return false;
}
