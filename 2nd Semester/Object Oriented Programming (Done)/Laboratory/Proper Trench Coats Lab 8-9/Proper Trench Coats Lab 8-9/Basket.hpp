//
//  Cart.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 13/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Coat.hpp"
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
