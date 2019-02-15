//
//  Coat.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Coat.hpp"
#include "Utils.hpp"
#include <sstream>
#include <iostream>
#include <vector>

using namespace std;

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

istream & operator>>(istream & is, Coat & c){
    string line;
    getline(is, line);
    vector<string> tokens = tokenize(line, ',');
    if (tokens.size() != 7)
        return is;
    c.id = stod(tokens[0]);
    c.size = stod(tokens[1]);
    c.color = tokens[2];
    c.price = stod(tokens[3]);
    c.quantity = stod(tokens[4]);
    c.photo = tokens[5];
    c.length = stod(tokens[6]);
    return is;
    
}

ostream & operator<<(ostream & os, const Coat & c){
    os << c.id << "," << c.size << "," << c.color << "," << c.price << "," << c.quantity << "," << c.photo << "," << c.length <<"\n";
    return os;
}

