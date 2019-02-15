//
//  FileBasket.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "FileBasket.hpp"

FileBasket::FileBasket() : Basket{}, fileName{""}{
}

void FileBasket::setFilename(const std::string& filename){
    if (filename != ""){
        this->fileName = filename;
    }
}
