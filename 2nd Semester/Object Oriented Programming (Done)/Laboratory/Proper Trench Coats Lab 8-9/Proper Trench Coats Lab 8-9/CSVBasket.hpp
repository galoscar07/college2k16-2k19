//
//  CVSBasket.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "FileBasket.hpp"
#include <string>

class CSVBasket: public FileBasket{
public:
    CSVBasket();
    void writeToFile() override;
    void displayBasket() override;
};

