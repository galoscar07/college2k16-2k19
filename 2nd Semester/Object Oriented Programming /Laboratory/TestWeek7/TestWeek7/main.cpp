//
//  main.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Ui.hpp"
using namespace std;
int main(){
    
    // Test
    Vector a = Vector(1);
    Genes b = Genes{"E_coli", "yyyy", "ATGAATTTGGA" };
    assert(a.getSize() == 0);
    a.add(b);
    assert(a.getSize() == 1);
    
    Repository repo = Repository();
    Controller admin = Controller(repo);
    Ui ui = Ui(admin);
    ui.run();
    system("pause");
    return 0;
}
