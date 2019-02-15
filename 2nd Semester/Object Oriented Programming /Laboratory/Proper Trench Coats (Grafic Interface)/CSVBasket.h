//
// Created by Gal Oscar on 23/05/2017.
//

#pragma once
#include "FileBasket.h"
#include <string>

class CSVBasket: public FileBasket{
public:
    CSVBasket();
    void writeToFile() override;
    void displayBasket() override;
};