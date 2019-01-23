//
//  RepositoryException.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 13/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "RepositoryExceptions.hpp"

FileException::FileException(const std::string & msg) : message(msg)
{
}

const char * FileException::what()
{
    return message.c_str();
}

RepositoryException::RepositoryException() : exception{}, message{""}{
}

RepositoryException::RepositoryException(const std::string & msg): message{msg}{
}

const char * RepositoryException::what(){
    return this->message.c_str();
}

const char * DuplicateCoatException::what(){
    return "There is another coat with the same id! ";
}

const char * InexistenCoatException::what(){
    return "There is no coat with the id";
}
