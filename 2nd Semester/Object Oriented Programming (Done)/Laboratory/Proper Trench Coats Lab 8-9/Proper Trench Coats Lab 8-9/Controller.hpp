//
//  Controller.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

//
//  Controller.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include "Repository.hpp"
#include "FileBasket.hpp"
#include <assert.h>
#include <vector>
#include "Validators.hpp"

class Controller{
private:
    Repository repo;
    CoatValidator validators;
public:
    FileBasket* basketList;
public:
    
    Controller(const Repository& r, CoatValidator v,FileBasket* file) : repo{ r }, validators{ v },basketList(file) {}
    
    Controller(const Repository& r) : repo(r) {}
    
    Repository getRepo() const { return repo; }
    
    void addCoatToRepo(const int& id, const int& size,const std::string& color,const float& price, const int& quantity, const std::string& photo, const float& length);
    
    void addCoatToBasket(Coat& coat);
    
    void removeCoatFromRepo(const int& id);
    
    void updateCoatInRepo(const int& id, const float& price, const int& quantity);
    
    std::vector<Coat> filterBySize(const int& size);
    
    std::vector<Coat> getBasket();
    
    float getMoney();
    
    std::vector<Coat> filterCoatsByLength(const float& length);
};
