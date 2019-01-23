//
// Created by Gal Oscar on 23/05/2017.
//
#pragma once
#include "FileBasket.h"

class HTMLBasket: public FileBasket{
public:
    HTMLBasket();
    void writeToFile() override;
    void displayBasket() override;
};
