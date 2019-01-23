//
//  Ui.cpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Ui.hpp"
#include <iostream>
#include <fstream>
using namespace std;

void Ui::readFromFile(){
    string fileName = "Words.txt";
    string line;
    ifstream file(fileName);
    if (!file.is_open()){
        cout << "Something went wrong and the file wasn't open";
        return;
    }
    while (getline(file, line)){
        size_t found1, found2;
        string key, value;
        found1 = line.find("|");
        found2 = line.find("\n");
        key = line.substr(0,found1);
        value = line.substr(found1+1, found2);
        this->s.add(key, value);
    }
}

void Ui::displayFromIt()
{
	Iterator it = this->s.iterator();
	while (it.valid() == true) {
		cout << "Word: " << it.getCurrent().key << " -> Meaning" << it.getCurrent().value << endl;
		it.next();
	}
}

void Ui::printMenu(){
    cout << "1 - Add a new word into the database" << endl;
    cout << "2 - Show a meaning of a word by its key" << endl;
    cout << "3 - Delete a word from the database" << endl;
    cout << "4 - Display the number of elements in the dictionary" << endl;
	cout << "5 - Display all words in the databse in alphabetically order" << endl;
    cout << "0 - Exit" << endl;
}
void Ui::addWord(){
    cout << "Enter the word (key): " << endl;;
    string key;
    getline(cin, key);
    cout << "Enter the definition of the word (value)" << endl;
    string value;
    getline(cin, value);
    this->s.add(key, value);
}

void Ui::removeWord(){
    cout << "Enter the word (key): " << endl;;
    string key;
    getline(cin, key);
    this->s.remove(key);
}

void Ui::displayWord(){
    cout << "Enter the word to receive a definition: " << endl;
    string key;
    getline(cin,key);
    string value;
    value = this->s.search(key);
    if (value == "0"){
        cout << "There is no such word in our database" << endl;
    }
    else {
        cout << "For the given word: " << key << " the definition is: \n" << value << endl;
    }
}

void Ui::displayNoWord(){
    cout << "The number of words in the database is : " << this->s.size() << endl;
}


void Ui::run(){
    Ui::readFromFile();
    while (true){
        Ui::printMenu();
        int command{ 0 };
        cout << "Input the command: ";
        cin >> command;
        cin.ignore();
        if (command == 0){
            cout << "Thank you for using the program" << endl;
            break;
        }
        try {
            if (command == 1){
                Ui::addWord();
            }
            if (command == 2){
                Ui::displayWord();
            }
            if (command == 3){
                Ui::removeWord();
            }
            if (command == 4){
                Ui::displayNoWord();
            }
			if (command == 5) {
				Ui::displayFromIt();
			}

        } catch (string &e) {
            cout << e << endl;
        }
    }
}
