//
//  Ui.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Ui.hpp"
#include <iostream>
#include <string>

using namespace std;

void Ui::printMenu(){
    cout << "1 - Add a new gene" << endl;
    cout << "2 - Show all genes" << endl;
    cout << "0 - Exit." << endl;
}

void Ui::addGenesToRepo(){
    cout << "Enter the name: ";
    std::string name;
    getline(cin, name);
    cout << "Enter the organism: ";
    std::string organism;
    getline(cin, organism);
    cout << "Enter the associated sequence: ";
    std::string sequence;
    getline(cin, sequence);
    if (this->contr.addGenesC(name, organism, sequence) == 0){
        cout << "The item wasn.t added" << endl;
    }
    else {
        cout << "The item was added" << endl;
    }
}

void Ui::displayAllGenesesRepo()
{
    Vector v = this->contr.getRepo().getGenes();
    Genes* genes = v.getAllElems();
    if (genes == NULL)
        return;
    if (v.getSize() == 0){
        cout << "There are no geneses in the repository." << endl;
        return;
    }
    for (int i = 0; i < v.getSize(); i++){
        Genes g = genes[i];
        cout <<g.getName() << " | " << g.getOrganism() << " | " << g.getSequence() << endl;
    }
}


void Ui::run(){
    this->contr.addGenesC("E_coli_k12", "yghE", "ATGGA");
    this->contr.addGenesC("Mouse", "yCOsE", "ATATGAGGA");
    this->contr.addGenesC("E_coliETC", "ysdgdgjhE", "AAAAATGGA");
    this->contr.addGenesC("E_coli_ASD", "yasdE", "ATTTTTGGA");
    this->contr.addGenesC("E_coli_k16", "ygasd", "ATCCCCGGA");
    bool keepAlive;
    keepAlive = true;
    while (keepAlive){
        Ui::printMenu();
        int command{ 0 };
        cout << "Input the command: ";
        cin >> command;
        cin.ignore();
        switch (command) {
            case 0:
                cout << "Thank you for using the program, Bye !!" << endl;
                keepAlive = false;
                break;
                
            case 1:
                this->addGenesToRepo();
                break;
            case 2:
                this->displayAllGenesesRepo();
                break;
        }
    }
}
