//
//  main.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 03/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//


#include "Ui.hpp"

using namespace std;

int main() {
    
    Repository repo = Repository();
    AdminController admin = AdminController(repo);
    Console console = Console(admin);
    console.run();
    return 0;
}
