//
//  Vector.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include "Coats.hpp"
#include <iterator>

typedef Coat TElement;

class Vector{
private:
    TElement* elems;
    int size;
    int capacity;
    
public:
    Vector(int capacity = 100);
    Vector(const Vector& v);
    ~Vector();
    void operator-(const TElement& e);
    Vector& operator=(const Vector& v);
    void add(const TElement& e);
    void remove(const int& pos);
    int getSize() const;
    TElement* getAllElems() const;
    TElement& get(int pos);
    Vector& operator+(const TElement& c);
    friend Vector& operator+(const TElement & c, Vector &v);
private:
    void resize(double factor = 2);
};

void testAdd();
void testRemove();
void testGet();
