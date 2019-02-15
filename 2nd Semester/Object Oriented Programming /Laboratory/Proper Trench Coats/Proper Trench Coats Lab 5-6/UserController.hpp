//
//  UserController.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 06/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <stdio.h>
#include "Repository.hpp"
#include <assert.h>

class UserController{
private:
    Repository repo;
public:
    UserController(const Repository& r) : repo(r) {}
    Repository getRepo() const { return repo; }
    void filterBySize(const int& size);
};
