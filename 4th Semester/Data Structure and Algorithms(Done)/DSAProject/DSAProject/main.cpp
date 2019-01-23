//
//  main.cpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include <iostream>
#include "SortedMap.hpp"
#include "Ui.hpp"

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    Tests t;
    t.testAll();
    SortedMap sort{&relation};
    Ui console = Ui(sort);
    console.run();
    return 0;
}
