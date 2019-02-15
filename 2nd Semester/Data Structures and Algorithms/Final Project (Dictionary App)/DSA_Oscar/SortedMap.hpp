//
//  SortedMap.hpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include <stack>
#include <string>

//Structures
typedef struct{
    std::string key;
    std::string value;
}TElement;

struct Node{
    TElement info;
    Node* left;
    Node* right;
};

//Names
typedef struct Node Node;
class Iterator;
bool relation(TElement a, TElement b);



//Classes
class SortedMap{
    friend class Iterator;
private:
    Node* root;
private:
    bool(*relation)(TElement, TElement);
    void insertRec(Node** n, TElement a);
    void sizeRec(int& nr, Node* n);
    Node* removeRec(Node* n, std::string key);
    Node* minimum(Node* n);
public:
    SortedMap(bool(*r)(TElement,TElement));
    ~SortedMap();
    void remove(std::string key);
    std::string search(std::string key);
    void add(std::string key, std::string value);
    Iterator iterator();
    int size();

    
};


class Iterator{
private:
    SortedMap* sm;
    std::stack<Node*> s;
    Node* currentNode;
public:
    Iterator(SortedMap* sortMap);
    ~Iterator();
    TElement getCurrent();
    bool valid();
    void next();
};



class Tests{
private:
    void testAdd();
    void testRemove();
    void testSize();
    void testSearch();
    void testRelation();
    void testIterator();
public:
    void testAll();
};
