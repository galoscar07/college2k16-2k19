//
//  Vector.cpp
//  TestWeek7
//
//  Created by Gal Oscar on 10/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Vector.hpp"
#include <assert.h>

Vector::Vector(int capacity){
    this->size = 0;
    this->capacity = capacity;
    this->elems = new Element[capacity];
}

Vector::Vector(const Vector& v){
    this->size = v.size;
    this->capacity = v.capacity;
    this->elems = new Element[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->elems[i] = v.elems[i];
}

Vector::~Vector(){
    delete[] this->elems;
}

void Vector::add(const Element& e){
    if (this->size == this->capacity)
        this->resize();
    this->elems[this->size] = e;
    this->size++;
}


void Vector::resize(double factor){
    this->capacity *= static_cast<int>(factor);
    Element* els = new Element[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->elems[i] = els[i];
    
    delete[] this->elems;
    elems = els;
}

Element* Vector::getAllElems() const{
    return this->elems;
}

Element & Vector::get(int pos){
    return this->elems[pos];
}

int Vector::getSize() const{
    return this->size;
}

void test_add(){
    Vector a = Vector(1);
    Genes b = Genes{"E_coli", "yyyy", "ATGAATTTGGA" };
    assert(a.getSize() == 0);
    a.add(b);
    assert(a.getSize() == 1);
    
}
