//
// Created by Gal Oscar on 26/05/2017.
//

#include "Repository.h"
#include "RepositoryExceptions.h"
#include <string>
#include <fstream>
#include <vector>

using namespace std;

Repository::Repository(){

}

Repository::Repository(const std::string& filename){
    this->filename = filename;
    this->readFromFile();
}

void Repository::addCoat(const Coat& coat){
    Coat c1{};
    try{
        c1 = this->findById(coat.getId());
        throw DuplicateCoatException();
    }
    catch (InexistenCoatException& e) {}
    this->coats.push_back(coat);
    this->writeToFile();
}

void Repository::removeCoat(const Coat& coat){
    int z = -1;
    bool ok = true;
    for (auto i : this->coats){
        z++;
        if (i.getId() == coat.getId()){
            ok = false;
            break;
        }
    }
    if (ok == true){
        throw InexistenCoatException{};
    }
    this->coats.erase(this->coats.begin() + z);
    this->writeToFile();
}

Coat Repository::findById(const int& id) const{
    for (auto c: this->coats){
        if (c.getId() == id)
            return c;
    }

    throw InexistenCoatException{};
}

void Repository::updateCoat(const Coat& coat){
    int z = -1;
    Coat c1{};
    for (auto c : this->coats){
        z++;
        if (c==(coat.getId())){
            c1 = c;
            break;
        }
    }
    if (c1.getId() == -1){
        throw InexistenCoatException{};
    }
    if (coat.getQuantity()>0){
        c1.setQuantity(coat.getQuantity());
    }
    if (coat.getPrice()>0){
        c1.setPrice(coat.getPrice());
    }
    this->coats[z] = c1;
    this->writeToFile();
}

void Repository::readFromFile(){
    if (this->filename == ""){
        return;
    }
    ifstream file(this->filename);
    if (!file.is_open()){
        throw FileException("The file could not be opened!");
    }
    Coat c;
    while (file >> c)
        this->coats.push_back(c);
    file.close();
}

void Repository::writeToFile(){
    if (this->filename == ""){
        return;
    }
    ofstream file(this->filename);
    if (!file.is_open()){
        throw FileException("The file could not be opened!");
    }
    for (auto s : this->coats){
        file << s;
    }
    file.close();
}
