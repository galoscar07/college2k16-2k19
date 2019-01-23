//
//  Ui.hpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "SortedMap.hpp"

class Ui{
private:
    SortedMap s;
    std::string fileName;
public:
    Ui (const SortedMap& c) : s(c) {};
    void run();
    
private:
    static void printMenu();
    void addWord();
    void removeWord();
    void displayWord();
    void displayNoWord();
    void readFromFile();
    void displayFromIt();
};
