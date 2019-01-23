//
// Created by Gal Oscar on 26/05/2017.
//

#pragma once
#include <string>
#include "Coat.h"
#include <vector>

class CoatException{
private:
    std::vector<std::string> errors;
public:
    CoatException(std::vector<std::string> _errors);
    std::vector<std::string> getErrors() const;
    std::string getErrorsAsString() const;
};

class CoatValidator{
public:
    CoatValidator() {}
    static void validate(const Coat& s);
};