//
//  Ui.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Ui.hpp"
#include "RepositoryExceptions.hpp"
#include "Validators.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Console::printMenu(){
    cout << "1 - Admin interface" << endl;
    cout << "2 - User interface" << endl;
    cout << "0 - Exit" << endl;
}

void Console::printAdminMenu(){
    cout << "Comands: " << endl;
    cout << "\t 1 - Add a coat." << endl;
    cout << "\t 2 - Remove a coat." << endl;
    cout << "\t 3 - Update a coat." << endl;
    cout << "\t 4 - Display all coats." << endl;
    cout << "\t 5 - Check which coats have the length smaller than." << endl;
    cout << "\t 0 - Back." << endl;
}

void Console::printUserMenu(){
    cout << "Commands: " << endl;
    cout << "\t 1 - Filter by size" << endl;
    cout << "\t 2 - Show cart" << endl;
    cout << "\t 0 - Back." << endl;
}

void Console::printFilterBySizeMenu(){
    cout << "1. Next" <<endl;
    cout << "2. Add To cart" << endl;
    cout << "0. Back to menu" << endl;
}

void Console::printCoat(Coat& c){
    cout << "Id: "<<c.getId() << " | Size: " << c.getSize() << " | Color: " << c.getColor() << " | Price: " << c.getPrice() << " | Quantity: " << c.getQuantity() << " | Photo: " << c.getPhoto() << " | Length: " << c.getLength() << endl;
}

void Console::addCoatToRepo(){
    cout << "Enter the id: ";
    int id;
    cin >> id;
    cin.ignore();
    cout << "Enter the size: ";
    int size;
    cin >> size;
    cin.ignore();
    cout << "Enter the color: ";
    std::string color;
    getline(cin, color);
    cout << "Enter the price: ";
    float price;
    cin >> price;
    cin.ignore();
    cout << "Enter the quantity: ";
    int quantity;
    cin >> quantity;
    cin.ignore();
    cout << "Enter the photo link: ";
    std::string photo;
    getline(cin, photo);
    cout << "Enter the length: ";
    float length;
    cin >> length;
    try {
        this->contr.addCoatToRepo(id, size, color, price, quantity, photo, length);
    }
    catch (CoatException& e){
        for (auto s : e.getErrors())
            cout << s;
    }
    catch (RepositoryException& e){
        cout << e.what() << endl;
    }
    catch (FileException& e){
        cout << e.what() << endl;
    }
}

void Console::removeCoatFromRepo(){
    cout << "Enter the id: ";
    int id;
    cin >> id;
    cin.ignore();
    try{
        this->contr.removeCoatFromRepo(id);
    }
    catch (CoatException& e){
        for (auto s : e.getErrors())
            cout << s;
    }
    catch (RepositoryException& e){
        cout << e.what() << endl;
    }
    catch (FileException& e){
        cout << e.what() << endl;
    }
}

void Console::updateCoatInRepo(){
    cout << "Enter the id: ";
    int id;
    cin >> id;
    cin.ignore();
    cout << "Enter the new price or -1 to skip: ";
    float price;
    cin >> price;
    cin.ignore();
    cout << "Enter the new quantity or -1 to skip: ";
    int quantity;
    cin >> quantity;
    cin.ignore();
    try {
        this->contr.updateCoatInRepo(id,price,quantity);
    }
    catch (CoatException& e){
        for (auto s : e.getErrors())
            cout << s;
    }
    catch (RepositoryException& e){
        cout << e.what() << endl;
    }
    catch (FileException& e){
        cout << e.what() << endl;
    }
}

void Console::displayAllCoatsRepo(){
    std::vector<Coat> v = this->contr.getRepo().getCoats();
    if (v.size() == 0){
        cout << "There are no coats in the repository." << endl;
        return;
    }
    for (auto c: v){
        this->printCoat(c);
    }
}


void Console::filterBySize(){
    cout << "Enter the size: ";
    int size;
    cin >> size;
    cin.ignore();
    std::vector<Coat> r;
    r = this->contr.filterBySize(size);
    int i = 0;
    bool keepAlive = true;
    if (r.size() == 0){
        cout << "I am sorry, we don't have coats size: " << size << ". Thank you four your understanding" << endl;
        return;
    }
    while (keepAlive){
        Coat c = r[i];
        printCoat(c);
        int command = 0 ;
        this->printFilterBySizeMenu();
        cout << "Input the command: " << endl;
        cin >> command;
        cin.ignore();
        switch (command) {
            case 1:
                if (i == r.size() - 1){
                    i = 0;
                }
                else{
                    i++;
                }
                break;
            case 2:{
                Coat c = r[i];
                c.setQuantity(1);
                this->contr.addCoatToBasket(c);
                break;
            }
            case 0:
                keepAlive = false;
                break;
        }
    }
}
void Console::showCart(){
    cout << "In cart you have: " << endl;
    if (this->contr.basketList->getAll().size() == 0){
        cout << "There is no item in your basket!" << endl;
    }
    else{
        for (auto c : this->contr.basketList->getAll()){
            printCoat(c);
        }
    cout << "And all products costs:  " << this->contr.getMoney() << " euro" << endl;
    }
    this->contr.basketList->writeToFile();
}

void Console::filterCoatsByLength(){
    vector<Coat> something;
    cout << "Please give a length: ";
    float length;
    cin >> length;
    something = contr.filterCoatsByLength(length);
    if (something.size() == 0){
        cout << "There is no element to be displayed" << endl;
    }
    else for (auto c : something){
        printCoat(c);
    }
}

void Console::run(){
    while (true)
    {
        Console::printMenu();
        int command{ 0 };
        cout << "Input the command: ";
        cin >> command;
        cin.ignore();
        if (command == 0)
            break;
        // admin
        if (command == 1)
        {
            while (true)
            {
                Console::printAdminMenu();
                int commandAdmin{ 0 };
                cout << "Input the command: ";
                cin >> commandAdmin;
                cin.ignore();
                if (commandAdmin == 0)
                    break;
                switch (commandAdmin)
                {
                    case 1:
                        this->addCoatToRepo();
                        break;
                    case 2:
                        this->removeCoatFromRepo();
                        break;
                    case 3:
                        this->updateCoatInRepo();
                        break;
                    case 4:
                        this->displayAllCoatsRepo();
                        break;
                    case 5:
                        this->filterCoatsByLength();
                        break;
                }
            }
        }
        if (command == 2)
        {
            while (true)
            {
                Console::printUserMenu();
                int commandUser{ 0 };
                cout << "Input the command: ";
                cin >> commandUser;
                cin.ignore();
                if (commandUser == 0)
                    break;
                switch (commandUser) {
                    case 1:
                        this->filterBySize();
                        break;
                    case 2:
                        this->showCart();
                        break;
                }
            }
        }
    }
}
