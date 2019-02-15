//
//  Tests.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 13/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once


class TestCart{ //Done
public:
    void testAdd();
    void testGetCurrentCoat();
    void testGetMoney();
    void testNext();
    void testGetAll();
};

class TestCoat{ //Done
public:
    void testOperators();
    void testSetters();
    void testGetter();
};

class TestRepository{ //Done
public:
    void testConstructor();
    void testAddCoat();
    void testRemoveCoat();
    void testFindById();
    void testUpdateCoat();
    void testGetCoats();
};

class TestController{
public:
    void testConstructor();
    void testGetRepo();
    void testAddCoatToRepo();
    void testAddCoatToBasket();
    void testRemoveCoatFromRepo();
    void testUpdateCoatInRepo();
    void testFilterBySize();
    void testGetBasket();
    void testGetMoney();
    void testFilterCoatsByLength();
};

class Test{
private:
    TestCart cart;
    TestCoat coat;
    TestController contr;
    TestRepository repo;
public:
    void runTests();
};

