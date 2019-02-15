//
// Created by Gal Oscar on 18/06/2017.
//
#pragma once
#include "Repository.h"

class Controller{
private:
    Repository repo;
public:
    Controller();
    Controller(Repository r);
    ~Controller();

    std::vector<Equation> getAll();
};