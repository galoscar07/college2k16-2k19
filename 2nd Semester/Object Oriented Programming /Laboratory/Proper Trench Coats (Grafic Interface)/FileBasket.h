//
// Created by Gal Oscar on 23/05/2017.
//

#pragma once
#include "Basket.h"
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
