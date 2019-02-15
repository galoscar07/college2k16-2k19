//
//  Vector.hpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Entities.hpp"
#include <iterator>

typedef Genes Element;

class Vector{
private:
    Element* elems;
    int size;
    int capacity;
public:
    Vector(int capacity = 10);
    Vector(const Vector& v);
    ~Vector();
    void add(const Element& e);
    int getSize() const;
    Element* getAllElems() const;
    Element& get(int pos);
    //Vector& operator+(const Element& c);
    //friend Vector& operator+(const Element & c, Vector &v);
    void testAdd();
private:
    void resize(double factor=2);
};
