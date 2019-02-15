//
//  main.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Ui.hpp"
#include "Tests.hpp"
#include "CSVBasket.hpp"
#include "HTMLBasket.hpp"
#include "FileBasket.hpp"

using namespace std;

int main() {
    FileBasket* something;
    string option;
    cout << "What do you want, CSV or HTML?" << endl;
    cin >> option;
    if (option == "CSV"){
        something = new CSVBasket();
        something->setFilename("/Users/galoscar/Documents/College/Semester 2/Object Oriented Programming/Laboratory/Proper Trench Coats Lab 8-9/Proper Trench Coats Lab 8-9/Basket.csv");
    }
    else if (option == "HTML"){
        something = new HTMLBasket();
        something->setFilename("/Users/galoscar/Documents/College/Semester 2/Object Oriented Programming/Laboratory/Proper Trench Coats Lab 8-9/Proper Trench Coats Lab 8-9/Basket.html");
    }
    else {
        cout << "Something went wrong restart the program" << endl;
        return 0;
    }
    Test test = Test();
    test.runTests();
    Repository repo = Repository("/Users/galoscar/Documents/College/Semester 2/Object Oriented Programming/Laboratory/Proper Trench Coats Lab 8-9/Proper Trench Coats Lab 8-9/Coats.txt");
    CoatValidator validator{};
    Controller admin = Controller(repo,validator,something);
    Console console = Console(admin);
    console.run();
    return 0;
}
