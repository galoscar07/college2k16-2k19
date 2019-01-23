//
//  Ui.cpp
//  TestWeek10
//
//  Created by Gal Oscar on 08/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Ui.hpp"

Ui::~Ui()
{
}


void Ui::printMenu(){
    cout << "Available Commands: " << endl;
    cout << "\t 1. Add a new department" << endl;
    cout << "\t 2. Show all efficient departments in the country" << endl;
    cout << "\t 3. Save to file" << endl;
    cout << "\t 4. List all hospitals" << endl;
    cout << "\t 0. Exit" << endl;
}

void Ui::addDepartment(){
    cout << "Give a type of department: " << endl;
    std::string type;
    cin >> type;
    cout << "Number of doctors: " << endl;
    int noDoctors = 0;
    cin >> noDoctors;
    double grade = 0;
    int noPatiens = 0;
    int noMothers = 0;
    int noNewborns = 0;
    if (type == "Surgery"){
        cout << "Number of patiens: " << endl;
        cin >> noPatiens;
        this->controller.addDepartment(this->controller.hospitals, type,noDoctors, noPatiens, noMothers, noNewborns, grade);
    }
    else if (type == "NeonatalUnit"){
        cout << "Number of mothers: " << endl;
        cin >> noMothers;
        cout << "Number of newborns: " << endl;
        cin >> noNewborns;
        cout << "Average grade: " << endl;
        cin >> grade;
        this->controller.addDepartment(this->controller.hospitals, type,noDoctors, noPatiens, noMothers, noNewborns, grade);
        
        }
}

void Ui::listHospitals(){
    cout << "Option not yet implemented" << endl;
}
void Ui::showAllEfficient(){
    cout << "Option not yet implemented" << endl;
}
void Ui::saveToFile(){
    cout << "Option not yet implemented" << endl;
}

void Ui::run(){
    bool keepAlive = true;
    while (keepAlive) {
        printMenu();
        int command = 0;
        cin >> command;
        switch (command) {
            case 0:
                keepAlive = false;
                cout << "Thank you for using the program " << endl;
                break;
            case 1:
                this->addDepartment();
                break;
            case 2:
                this->showAllEfficient();
                break;
            case 3:
                this->saveToFile();
                break;
            case 4:
                this->listHospitals();
                break;
            default:
                cout << "Invalid command " << endl;
                break;
        }
    }
}
