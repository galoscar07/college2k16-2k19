//
//  RepositoryException.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 13/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <exception>
#include <string>

class FileException : public std::exception
{
protected:
    std::string message;
    
public:
    FileException(const std::string& msg);
    virtual const char* what();
};

class RepositoryException : public std::exception{
protected:
    std::string message;
public:
    RepositoryException();
    RepositoryException(const std::string& msg);
    virtual ~RepositoryException() {}
    virtual const char* what();
};

class DuplicateCoatException : public RepositoryException{
public:
    const char* what();
};

class InexistenCoatException : public RepositoryException{
public:
    const char* what();
};