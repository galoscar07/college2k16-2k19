//
//  CVSBasket.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "CSVBasket.hpp"
#include "FileBasket.hpp"
#include <fstream>
#include "RepositoryExceptions.hpp"
using namespace std;

CSVBasket::CSVBasket() : FileBasket(){
}

void CSVBasket::writeToFile(){
    ofstream f(this->fileName);
    if (!f.is_open())
        throw FileException("The file could not be opened!");
    for (auto s : this->coats)
        f << s;
    f.close();
}
/*
void CSVBasket::displayBasket(){
    string aux = "\"" + this->fileName + "\"";
    ShellExecuteA(NULL, NULL, "c:\\Program Files\\Microsoft Office\\Office15\\EXCEL.EXE", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}
*/

void CSVBasket::displayBasket(){
    
}
