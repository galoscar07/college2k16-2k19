//
// Created by Gal Oscar on 23/05/2017.
//

#pragma once
#include "Coat.h"
#include <vector>

class Basket{
protected:
    std::vector<Coat> coats;
    int current;
    float money;

public:
    Basket();
    void add(Coat coat);
    Coat getCurrentCoat();
    float getMoney();
    Coat next();
    std::vector<Coat> getAll() {return coats;};
};
