#pragma once

#include "Equation.h"
#include <vector>
#include <string>

class Repository{
private:
    std::string filename;
    std::vector<Equation> equations;
public:
    Repository() {};
    Repository(std::string filename);
    ~Repository();

    void load();
    std::vector<Equation> getAll();

};