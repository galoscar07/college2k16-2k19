//
//  Tests.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 13/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Tests.hpp"
#include "Basket.hpp"
#include "Coat.hpp"
#include "Repository.hpp"
#include "RepositoryExceptions.hpp"
#include "Controller.hpp"
#include <vector>

using namespace std;

void TestCart::testAdd(){
    Basket b = Basket();
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat();
    b.add(c1);
    assert(b.getAll().size() == 1);
    b.add(c1);
    assert(b.getAll().size() == 1);
    b.add(c2);
    assert(b.getAll().size() == 2);
    vector<Coat> something = b.getAll();
    c3 = something[0];
}
void TestCart::testGetCurrentCoat(){
    Basket b = Basket();
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat();
    b.add(c1);
    b.add(c2);
    c3 = b.getCurrentCoat();
    assert(c3==(c1.getId()));
    c3 = b.next();
    assert(b.getCurrentCoat()==(c2.getId()));
}
void TestCart::testGetMoney(){
    Basket b = Basket();
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    b.add(c1);
    assert(b.getMoney() == c1.getPrice());
    b.add(c1);
    assert(b.getMoney() == c1.getPrice() * 2);
    b.add(c2);
    assert(b.getMoney() == (c1.getPrice() * 2 + c2.getPrice()));
}
void TestCart::testNext(){
    Basket b = Basket();
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat();
    b.add(c1);
    b.add(c2);
    assert(b.next()==(c2.getId()));
    c3 = b.next();
    assert(c3 == (c1.getId()));
    assert(b.next()==(c2.getId()));
    
}
void TestCart::testGetAll(){
    Basket b = Basket();
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat();
    b.add(c1);
    b.add(c2);
    vector<Coat> something = b.getAll();
    assert(something[0]==(c1.getId()));
    assert(something[1]==(c2.getId()));
}

void TestCoat::testOperators(){
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",189);
    bool equal = true;
    bool smaller = true;
    equal = c1 == (c2.getId());
    assert(equal == false);
    equal = c3 == (c2.getId());
    assert(equal == true);
    smaller = c1<(c2.getLength());
    assert(smaller == true);
    smaller = c3<(c2.getLength());
    assert(smaller == false);
}
void TestCoat::testSetters(){
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    c1.setPrice(1);
    c1.setQuantity(1);
    assert(c1.getPrice() == 1);
    assert(c1.getQuantity() == 1);
}
void TestCoat::testGetter(){
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    assert(c1.getQuantity() == 3);
    assert(c1.getPrice() == 1795);
    assert(c1.getId() == 0);
    assert(c1.getLength() == 116);
    assert(c1.getSize() == 52);
    assert(c1.getColor() == "Light taupe");
    assert(c1.getPhoto() == "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041");
}

void TestRepository::testConstructor(){
    //Nothing for now
}
void TestRepository::testAddCoat(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    repo.addCoat(c1);
    assert(repo.getCoats().size() == 1);
    repo.addCoat(c2);
    assert(repo.getCoats().size() == 2);
    try{
        repo.addCoat(c1);
    }
    catch (DuplicateCoatException& e){}
}
void TestRepository::testRemoveCoat(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(2, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    
    repo.addCoat(c1);
    repo.addCoat(c2);
    try{
        repo.removeCoat(c3);
    }catch (InexistenCoatException& e){}
    assert(repo.getCoats().size() == 2);
    repo.removeCoat(c1);
    assert(repo.getCoats().size() == 1);
    //repo.removeCoat(c2);
    //assert(repo.getCoats().size() == 0);
}
void TestRepository::testFindById(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat();
    repo.addCoat(c1);
    repo.addCoat(c2);
    c3 = repo.findById(c1.getId());
    assert(c3==(c1.getId()));
    try{
        c3 = repo.findById(55);
    }catch(InexistenCoatException& e){}
}
void TestRepository::testUpdateCoat(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(0, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(3, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    try{
        repo.updateCoat(c3);
    }catch(InexistenCoatException& e){}
    repo.updateCoat(c2);
    assert(repo.getCoats()[0].getQuantity() == 2);
}
void TestRepository::testGetCoats(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(3, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    repo.addCoat(c2);
    repo.addCoat(c3);
    vector<Coat> something = repo.getCoats();
    assert(something[0]==(c1.getId()));
    assert(something[1]==(c2.getId()));
    assert(something[2]==(c3.getId()));
}

void TestController::testGetRepo(){
    Repository repo = Repository("");
    Repository r1 = Repository("");
    Controller contr = Controller(repo);
    r1 = contr.getRepo();
    assert(repo.getCoats().size() == r1.getCoats().size());
    
}
void TestController::testAddCoatToRepo(){
    Repository repo = Repository("");
    Controller contr = Controller(repo);
    contr.addCoatToRepo(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    assert(contr.getRepo().getCoats().size() == 1);
    try{
       contr.addCoatToRepo(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    }catch(DuplicateCoatException& e){}
}

void TestController::testAddCoatToBasket(){
    Repository repo = Repository("");
    Controller contr = Controller(repo);
    Coat c3 = Coat(3, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    contr.addCoatToBasket(c3);
   // assert(contr.basket.getAll().size() == 1);
}
void TestController::testRemoveCoatFromRepo(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(3, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    repo.addCoat(c2);
    repo.addCoat(c3);
    Controller contr = Controller(repo);
    assert(contr.getRepo().getCoats().size() == 3);
    contr.removeCoatFromRepo(1);
    assert(contr.getRepo().getCoats().size() == 2);
    contr.removeCoatFromRepo(0);
    assert(contr.getRepo().getCoats().size() == 1);
    try{
        contr.removeCoatFromRepo(77);
    }catch(InexistenCoatException& e){}
    
}
void TestController::testUpdateCoatInRepo(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(0, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(3, 36, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    Controller contr = Controller(repo);
    try{
        contr.updateCoatInRepo(55, 55, 55);
    }catch(InexistenCoatException& e){}
    contr.updateCoatInRepo(0, 14, 2);
    vector<Coat> something = contr.getRepo().getCoats();
    Coat som = something[0];
    assert(som.getQuantity() == 2);
    assert(som.getPrice() == 14);
}

void TestController::testGetMoney(){
    Repository repo = Repository("");
    Controller contr = Controller(repo);
   // assert(contr.getMoney() == 0);
}

void TestController::testFilterBySize(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(2, 38, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    repo.addCoat(c2);
    repo.addCoat(c3);
    Controller contr = Controller(repo);
    vector<Coat> something = contr.filterBySize(38);
    assert(something.size() == 2);
    
}

void TestController::testGetBasket(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(0, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(3, 38, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    Controller contr = Controller(repo);
    //contr.addCoatToBasket(c1);
    //contr.addCoatToBasket(c2);
    //contr.addCoatToBasket(c3);
}

void TestController::testFilterCoatsByLength(){
    Repository repo = Repository("");
    Coat c1 = Coat(0, 52, "Light taupe", 1795, 3, "https://us.burberry.com/unisex-tropical-gabardine-car-coat-with-exaggerated-cuffs-p45533041", 116);
    Coat c2 = Coat(1, 38, "Black", 1695, 2, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39066881",188);
    Coat c3 = Coat(2, 38, "Stone", 1670, 5, "https://us.burberry.com/the-kensington-short-heritage-trench-coat-p39110561", 188);
    repo.addCoat(c1);
    repo.addCoat(c2);
    repo.addCoat(c3);
    Controller contr = Controller(repo);
    vector<Coat> something = contr.filterCoatsByLength(188);
    assert(something.size() == 1);
}

void Test::runTests(){
    cart.testAdd();
    cart.testNext();
    cart.testGetAll();
    cart.testGetCurrentCoat();
    cart.testGetMoney();
    coat.testOperators();
    coat.testSetters();
    coat.testGetter();
    repo.testConstructor();
    repo.testAddCoat();
    repo.testRemoveCoat();
    repo.testFindById();
    repo.testUpdateCoat();
    repo.testGetCoats();
    contr.testGetRepo();
    contr.testAddCoatToRepo();
    contr.testRemoveCoatFromRepo();
    contr.testUpdateCoatInRepo();
    contr.testGetMoney();
    contr.testFilterCoatsByLength();
    contr.testFilterBySize();
    contr.testGetBasket();
}

