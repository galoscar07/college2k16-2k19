//
//  FileBasket.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Basket.hpp"
using namespace std;

class FileBasket : public Basket{
protected:
    string fileName;
    
public:
    FileBasket();
    virtual ~FileBasket() {}
    void setFilename(const string& filename);
    virtual void writeToFile() = 0;
    virtual void displayBasket() = 0;
};
