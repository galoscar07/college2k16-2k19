//
//  main.cpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include <iostream>
#include "Ui.hpp"

int main() {
    Controller controller = Controller();
    Ui ui = Ui(controller);
    ui.run();
    
    return 0;
}
