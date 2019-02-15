//
//  Controller.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Repository.hpp"
#include <assert.h>

class AdminController{
private:
    Repository repo;
    Vector basket;
    int money;
public:
    AdminController(const Repository& r) : repo(r) {}
    
    Repository getRepo() const { return repo; }
    
    void addCoatToRepo(const int& id, const int& size,const std::string& color,const float& price, const int& quantity, const std::string& photo, const float& length);
    
    void addCoatToBasket(const int& id, const int& size,const std::string& color,const float& price, const int& quantity, const std::string& photo, const float& length);
    
    void removeCoatFromRepo(const int& id);
    
    void updateCoatInRepo(const int& id, const float& price, const int& quantity);
    
    Vector filterBySize(const int& size);
    
    Vector getBasket() const {return basket; }
    
    int getMoney() const {return money; }
    
    Vector filterCoatsByLength(const float& length);
};

void testAdminAdd();
void testAdminRemove();
void testAdminUpdate();
