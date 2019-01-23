//
//  Validators.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Validators.h"
using namespace std;

CoatException::CoatException(std::vector<std::string> _errors): errors{_errors}{
}

std::vector<std::string> CoatException::getErrors() const{
    return this->errors;
}

void CoatValidator::validate(const Coat & c){
    vector<string> errors;
    if (c.getId() < 0)
        errors.push_back("The id cannot be a negative number! \n");
    if (c.getSize() < 0)
        errors.push_back("The size cannot be a negative number!\n");
    if (c.getSize() < 0)
        errors.push_back("The length cannot be a negative number!\n");
    if (errors.size() > 0)
        throw CoatException(errors);
}

std::string CoatException::getErrorsAsString() const {
    string err;
    for (auto e : this->errors)
        err += e;
    return err;
}