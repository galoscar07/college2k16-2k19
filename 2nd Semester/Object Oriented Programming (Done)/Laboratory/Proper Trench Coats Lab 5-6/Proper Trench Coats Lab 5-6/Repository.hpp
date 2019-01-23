//
//  Repository.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include <stdio.h>
#include "Vector.hpp"

class Repository{
private:
    Vector coats;
    
public:
    Repository() {}
    /*
     Default constructor for the repository.
     Initializes an object of type repository.
     */
    
    void addCoat(const Coat& c);
    /*
     Adds a coat to the repository.
     Input: c which is type coat.
     */
    
    Coat findById(const int& id);
    /*
     Finds a Coat by id and return the coat if the id was found and an empty coat if the coat wasn't found.
     Input: id which is an int.
     Output: the Coat that was found, or an "empty" Coat (all fields empty and id -1), if nothing was found.
     */
    
    void removeCoat(const int& id);
    /*
     Removes a Coat by id.
     Input: id id which is an int.
     */
    
    void updateCoat(const int& id, const float& price, const int& quantity);
    /*
     Updates a Coat's price and (or) quantity.
     Input: id which is an int, price id which is a float, quantity id which is an int
     
     */
    
    Vector getCoats() const { return coats; }
    /*
     Returns a Vector containing all the coats.
     Output: coats - Vector.
     */
};
