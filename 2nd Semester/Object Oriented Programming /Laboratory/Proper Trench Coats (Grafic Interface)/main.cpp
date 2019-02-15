#include "Ui.h"
#include "CSVBasket.h"
#include "HTMLBasket.h"
#include "FileBasket.h"
#include "Repository.h"
#include "Validators.h"
#include "Controller.h"
#include <iostream>
#include "BasketQt.h"
#include <QtWidgets/QApplication>

using namespace std;

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);
    FileBasket* something;
    string option;
    cout << "What do you want, CSV or HTML?" << endl;
    cin >> option;
    if (option == "CSV"){
        something = new CSVBasket();
        something->setFilename("/Users/galoscar/Documents/College/2nd Semester/Object Oriented Programming (Done)/Laboratory/Proper Trench Coats Lab 11-12/Basket.csv");
    }
    else if (option == "HTML"){
        something = new HTMLBasket();
        something->setFilename("/Users/galoscar/Documents/College/2nd Semester/Object Oriented Programming (Done)/Laboratory/Proper Trench Coats Lab 11-12/Basket.html");
    }
    else {
        cout << "Something went wrong restart the program" << endl;
        return 0;
    }
    Repository repo = Repository("/Users/galoscar/Documents/College/2nd Semester/Object Oriented Programming (Done)/Laboratory/Proper Trench Coats Lab 11-12/Coats.txt");
    CoatValidator validator{};
    Controller admin = Controller(repo,validator,something);
    BasketQt w{ admin };
    w.show();
    something->writeToFile();
    return a.exec();
}