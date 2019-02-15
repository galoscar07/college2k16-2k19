//
//  Ui.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Ui.hpp"
#include <iostream>
#include <string>

using namespace std;

void Console::printMenu(){
    cout << "1 - Admin interface" << endl;
    cout << "2 - User interface" << endl;
    cout << "0 - Exit" << endl;
}

void Console::printAdminMenu(){
    cout << "Commands: " << endl;
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

void Console::printCoat(const Coat& c){
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
        this->admin.addCoatToRepo(id, size, color, price, quantity, photo, length);
    }
    catch (const char* msg){
        cout << msg << endl;
    }
}

void Console::removeCoatFromRepo(){
    cout << "Enter the id: ";
    int id;
    cin >> id;
    cin.ignore();
    try {
        this->admin.removeCoatFromRepo(id);
    }
    catch (const char* msg)
    {
        cout << msg << endl;
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
        this->admin.updateCoatInRepo(id,price,quantity);
    }
    catch (const char* msg)
    {
        cout << msg << endl;
    }
}

void Console::displayAllCoatsRepo(){
    Vector v = this->admin.getRepo().getCoats();
    Coat* coats = v.getAllElems();
    if (coats == NULL)
        return;
    if (v.getSize() == 0)
    {
        cout << "There are no coats in the repository." << endl;
        return;
    }
    
    for (int i = 0; i < v.getSize(); i++)
    {
        Coat c = coats[i];
        printCoat(c);
    }
}


void Console::filterBySize(){
    cout << "Enter the size: ";
    int size;
    cin >> size;
    cin.ignore();
    Vector r = Vector();
    r = this->admin.filterBySize(size);
    int i = 0;
    bool keepAlive = true;
    while (keepAlive){
        Coat c = r.get(i);
        printCoat(c);
        int command = 0 ;
        this->printFilterBySizeMenu();
        cout << "Input the command: " << endl;
        cin >> command;
        cin.ignore();
        switch (command) {
            case 1:
                if (i == r.getSize() - 1){
                    i = 0;
                }
                else{
                    i++;
                }
                break;
            case 2:
                this->admin.addCoatToBasket(c.getId(), c.getSize(), c.getColor(), c.getPrice(), c.getQuantity(), c.getPhoto(), c.getLength());
                break;
            case 0:
                keepAlive = false;
                break;
        }
    }
}

void Console::showCart(){
    cout << "In cart you have: " << endl;
    if (this->admin.getBasket().getSize() == 0){
        cout << "There is no item in your basket!" << endl;
    }
    else{
    for (int i = 0; i < this->admin.getBasket().getSize(); i++){
        Coat c = this->admin.getBasket().get(i);
        printCoat(c);
    }
    }
    cout << "And all products costs:  " << this->admin.getMoney() << " euro" << endl;
}

void Console::filterCoatsByLength(){
    cout << "Please give a length: ";
    float length;
    cin >> length;
    Vector vect = this->admin.filterCoatsByLength(length);
    for (int i = 0; i < vect.getSize(); i++){
        Coat c = vect.get(i);
        printCoat(c);
    }
}

void Console::run(){
    this->admin.addCoatToRepo(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    
    this->admin.addCoatToRepo(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    
    this->admin.addCoatToRepo(2, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    
    this->admin.addCoatToRepo(3, 34, "Honey", 1799.99, 3, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110571",188);
    
    this->admin.addCoatToRepo(4, 38, "Navy", 2177, 10, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39802111",188);
    
    this->admin.addCoatToRepo(5, 36, "Honey", 1995, 5, "https://us.burberry.com/long-cotton-gabardine-car-coat-p39428531",98);
    
    this->admin.addCoatToRepo(6, 40, "Black", 1995, 3, "https://us.burberry.com/long-cotton-gabardine-car-coat-p39428511",98);
    
    this->admin.addCoatToRepo(7, 38, "Bright Olive", 1995, 12, "https://us.burberry.com/oversize-storm-shield-tropical-gabardine-trench-coat-p40504731", 110);
    
    this->admin.addCoatToRepo(8, 40, "Canvas Blue", 1995, 7, "https://us.burberry.com/tropical-gabardine-cotton-trench-coat-p40504741", 105);
    
    this->admin.addCoatToRepo(9, 38, "Antique taupe pink", 1795, 9, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-p45533051", 116);
    
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
