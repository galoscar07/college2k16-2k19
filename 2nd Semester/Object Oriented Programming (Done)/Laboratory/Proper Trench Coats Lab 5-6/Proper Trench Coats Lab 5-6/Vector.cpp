//
//  Vector.cpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Vector.hpp"
#include <assert.h>


Vector::Vector(int capacity){
    this->size = 0;
    this->capacity = capacity;
    this->elems = new TElement[capacity];
}

Vector::Vector(const Vector& v){
    this->size = v.size;
    this->capacity = v.capacity;
    this->elems = new TElement[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->elems[i] = v.elems[i];
}

Vector::~Vector(){
    delete[] this->elems;
}
void Vector::operator-(const TElement& e){
    int z = 0;
    for (int i = 0; i < this->size ; i++)
        if (this->elems[i]==(e.getId())){
            z = i;
            break;
        }
    
    for (int j = z; j < this->size - 1; j++)
        this->elems[j] = this->elems[j + 1];
    
    this->size--;

}

Vector& Vector::operator=(const Vector& v){
    if (this == &v)
        return *this;
    
    this->size = v.size;
    this->capacity = v.capacity;
    
    delete[] this->elems;
    this->elems = new TElement[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->elems[i] = v.elems[i];
    
    return *this;
}

void Vector::add(const TElement& e){
    if (this->size == this->capacity)
        this->resize();
    this->elems[this->size] = e;
    this->size++;
}

void Vector::remove(const int& pos) {
    if (this->elems == NULL)
        return;
    
    for (int i = pos; i < this->size - 1; i++)
        this->elems[i] = this->elems[i + 1];
    
    this->size--;
}

void Vector::resize(double factor){
    this->capacity *= static_cast<int>(factor);
    
    TElement* els = new TElement[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->elems[i] = els[i];
    
    delete[] this->elems;
    elems = els;
}

TElement* Vector::getAllElems() const{
    return this->elems;
}

TElement & Vector::get(int pos){
    return this->elems[pos];
}

Vector & Vector::operator+(const TElement& c){
    this->add(c);
    return *this;
}

int Vector::getSize() const{
    return this->size;
}

void testAdd(){
    Vector a = Vector(1);
    Coat b = Coat{ 0,1,"black",3.5,2,"abc.html", 99};
    assert(a.getSize() == 0);
    a = b + a;
    assert(a.getSize() == 1);
}

void testRemove(){
    Vector a = Vector(1);
    Coat b = Coat{ 0,1,"black",3.5,2,"abc.html", 99};
    a.add(b);
    assert(a.getSize() == 1);
    a.remove(0);
    assert(a.getSize() == 0);
}

void testGet(){
    Vector a = Vector(1);
    Coat b = Coat{ 0,1,"black",3.5,2,"abc.html", 99};
    a.add(b);
    assert(a.get(0).getSize() == 1);
}

Vector& operator+(const TElement & c, Vector &v){
    v.add(c);
    return v;
}
