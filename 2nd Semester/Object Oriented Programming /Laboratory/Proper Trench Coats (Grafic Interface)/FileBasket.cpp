//
// Created by Gal Oscar on 23/05/2017.
//

#include "FileBasket.h"
#include <string>

FileBasket::FileBasket() : Basket{}, fileName{""}{
}

void FileBasket::setFilename(const std::string& filename){
    if (filename != ""){
        this->fileName = filename;
    }
}
