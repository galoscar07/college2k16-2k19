//
// Created by Gal Oscar on 23/05/2017.
//

#include "CSVBasket.h"
#include "FileBasket.h"
#include <fstream>
#include "RepositoryExceptions.h"
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
