//
//  Controller.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Controller.hpp"
#include <iostream>

void AdminController::addCoatToRepo(const int& id, const int& size, const std::string& color, const float& price, const int& quantity, const std::string& photo, const float& length){
    Coat c{ id,  size, color, price, quantity, photo, length };
    Coat a = this->repo.findById(c.getId());
    if (a.getId() != -1)
        throw "Duplicate id!";
    this->repo.addCoat(c);
}

void AdminController::removeCoatFromRepo(const int & id){
    Coat a = this->repo.findById(id);
    if (a.getId() == -1)
        throw "Invalid id!";
    this->repo.removeCoat(id);
}

void AdminController::updateCoatInRepo(const int & id, const float & price, const int & quantity){
    Coat c = this->getRepo().findById(id);
    if (c.getId() == -1)
        throw "Invalid id!";
    this->repo.updateCoat(id, price, quantity);
}

Vector AdminController::filterBySize(const int& size){
    Vector r = Vector();
    for (int i = 0; i < this->getRepo().getCoats().getSize() ; i++){
        Coat c = this->getRepo().getCoats().get(i);
        if (c.getSize() == size) {
            r.add(c);
        }
    }
    return r;
}
void AdminController::addCoatToBasket(const int& id, const int& size,const std::string& color,const float& price, const int& quantity, const std::string& photo, const float& length){
    Coat c{ id,  size, color, price, 1, photo, length };
    bool ok = false;
    for (int i = 0; i < this->basket.getSize(); i++ ){
        Coat b = this->basket.get(i);
        if (b.getId() == id){
            ok = true;
            this->basket.get(i).setQuantity(this->basket.get(i).getQuantity() + 1);
            this->money = this->money + price ;
        }
    }
    if (ok == false){
        this->basket.add(c);
        this->money = this->money + price ;
    }
}

Vector AdminController::filterCoatsByLength(const float& length){
    Vector r = Vector();
    for (int i = 0; i < this->getRepo().getCoats().getSize() ; i++){
        Coat c = this->getRepo().getCoats().get(i);
        if (c<(length)) {
            r.add(c);
        }
    }
    return r;
}

void test_admin_add(){
    Repository rep = Repository();
    AdminController adm = AdminController(rep);
    adm.addCoatToRepo(0, 1, "black", 6.6, 3, "abc.html", 15);
    assert(adm.getRepo().getCoats().getSize() == 1);
    adm.addCoatToRepo(1, 2, "black", 6.6, 3, "abc.html", 15);
    assert(adm.getRepo().getCoats().getSize() == 2);
}

void test_admin_remove(){
    Repository rep = Repository();
    AdminController adm = AdminController(rep);
    adm.addCoatToRepo(0, 1, "black", 6.6, 3, "abc.html", 15);
    assert(adm.getRepo().getCoats().getSize() == 1);
    adm.removeCoatFromRepo(0);
    assert(adm.getRepo().getCoats().getSize() == 0);
}

void test_admin_update(){
    Repository rep = Repository();
    AdminController adm = AdminController(rep);
    adm.addCoatToRepo(0, 1,"black", 6.6, 3, "abc.html", 15);
    assert(adm.getRepo().getCoats().getSize() == 1);
    adm.updateCoatInRepo(0,3.3,4);
    assert(adm.getRepo().getCoats().get(0).getQuantity() == 4);
}
