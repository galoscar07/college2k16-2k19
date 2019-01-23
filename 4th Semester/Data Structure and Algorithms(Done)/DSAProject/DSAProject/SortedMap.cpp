//
//  SortedMap.cpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include <string>
#include <exception>
#include <assert.h>
#include "SortedMap.hpp"
#include <iostream>

bool relation(TElement a, TElement b){
    if (a.key > b.key) {
        return true;
    }
    return false;
}


// ----------------------------------------------------------- SORTED MAP ---------------------------------------------------------------------

SortedMap::SortedMap(bool(*r)(TElement,TElement)){
    this->root = NULL;                  
    this->relation = r;
}

SortedMap::~SortedMap(){
    
}


std::string SortedMap::search(std::string key){
    TElement something;
    something.key = key;
    something.value = "0";
    
    Node* currentNode = this->root;
    while (currentNode != NULL && currentNode->info.key != key){
        if (!this->relation(currentNode->info, something)){
            currentNode = currentNode->right;
        }
        else {
            currentNode = currentNode->left;
        }
    }
    if (currentNode == NULL){
        return "0";
    }
    return currentNode->info.value;
}


void SortedMap::add(std::string key, std::string value){
    TElement something;
    something.key = key;
    something.value = value;
    std::string exist = this->search(key);
    if (exist != "0"){
        throw (std::string)"The element is already in the container";
    }
    this->insertRec(&this->root, something);
}

void SortedMap::insertRec(Node** n, TElement something){
    if (*n == NULL){
        *n = new Node;
        (*n)->info = something;
        (*n)->left = NULL;
        (*n)->right = NULL;
    }
    else if (this->relation((*n)->info, something)) {
        this->insertRec(&(*n)->left, something);
    }
    else {
        this->insertRec(&(*n)->right, something);
    }
}

void SortedMap::sizeRec(int &nr, Node* n){
    if (n == NULL) {
        return;
    }
    nr++;
    this->sizeRec(nr, n->left);
    this->sizeRec(nr, n->right);
}


int SortedMap::size(){
    int nr = 0;
    this->sizeRec(nr, this->root);
    return nr;
}


Iterator SortedMap::iterator(){
    Iterator it{this};
    return it;
}

Node* SortedMap::minimum(Node* n){
    Node* currentNode = n;
    while(currentNode->left != NULL){
        currentNode = currentNode->left;
    }
    return currentNode;
}



Node* SortedMap::removeRec(Node * n, std::string key){
    int isRoot = 0;
    if (n == NULL)
        return n;
    else if (key < n->info.key)
        n->left = this->removeRec(n->left, key);
    else if (key > n->info.key)
        n->right = this->removeRec(n->right, key);
    else {
        if (n->left == NULL && n->right == NULL) {
            if (n == this->root)
                this->root = NULL;
            delete n;
            n = NULL;
        }
        else if (n->right == NULL) {
            if (n == this->root) isRoot = 1;
            Node* aux = n;
            n = n->left;
            delete aux;
            if (isRoot == 1)
                this->root = n;
        }
        else if (n->left == NULL) {
            if (n == this->root) isRoot = 1;
            Node* aux = n;
            n = n->right;
            delete aux;
            if (isRoot == 1)
                this->root = n;
        }
        else {
            if (n == this->root) isRoot = 1;
            Node* aux = this->minimum(n->right);
            n->info = aux->info;
            n->right = removeRec(n->right, aux->info.key);
            if (isRoot == 1)
                this->root = n;
        }
    }
    return n;
    
}


void SortedMap::remove(std::string key){
    std::string exist = this->search(key);
    if (exist == "0"){
        throw (std::string)"The element is not in the container";
    }
    this->removeRec(this->root, key);
}


// ----------------------------------------------------------------- ITERATOR ------------------------------------------------------------------

Iterator::~Iterator(){
    
}

Iterator::Iterator(SortedMap* sortMap){
    this->sm = sortMap;
    Node *nod = this->sm->root;
    while (nod != NULL){
        this->s.push(nod);
        nod = nod->left;
    }
    if (!this->s.empty()){
        this->currentNode = this->s.top();
    }
    else{
        this->currentNode = NULL;
    }
}

TElement Iterator::getCurrent(){
    return this->currentNode->info;
}

bool Iterator::valid(){
    if (this->currentNode == NULL){
        return false;
    }
    else{
        return true;
    }
}

void Iterator::next(){
    Node* nod = this->s.top();
    this->s.pop();
    if (nod->right != NULL){
        nod = nod->right;
        while (nod != NULL){
            this->s.push(nod);
            nod = nod->left;
        }
    }
    if (!this->s.empty()){
        this->currentNode = this->s.top();
    }
    else{
        this->currentNode = NULL;
    }
}

// ---------------------------------------------------- Tests -----------------------------------------------------------------------------

void Tests::testAll(){
    testAdd();
    testRemove();
    testSearch();
    testSize();
    testRelation();
    testIterator();
    
}

void Tests::testAdd(){
    SortedMap sm{&relation};
    sm.add("Ghost","A");
    sm.add("Chair","B");
    assert(sm.size() == 2);
    sm.add("Inspiration","C");
    sm.add("Apple","d");
    sm.add("Word","haha");
    assert(sm.size() == 5);
    try {
        sm.add("Ghost", "bla bla");
    } catch (std::string &e){
        
    }
}

void Tests::testSize(){
    SortedMap sm{&relation};
    assert(sm.size() == 0);
    sm.add("Ghost","A");
    sm.add("Chair","B");
    assert(sm.size() == 2);
    sm.remove("Ghost");
    assert(sm.size() == 1);
}

void Tests::testSearch(){
    SortedMap sm{&relation};
    sm.add("Ghost","A");
    sm.add("Chair","B");
    assert(sm.search("Ghost") == "A");
    assert(sm.search("Something") == "0");
}

void Tests::testIterator(){
    SortedMap sm{&relation};
    sm.add("Ghost","A");
    sm.add("Chair","B");
    sm.add("Inspiration","C");
    sm.add("Apple","d");
    sm.add("Word","haha");
    Iterator it {&sm};
    assert(it.valid() == true);
    assert(it.getCurrent().key == "Apple");
    it.next();
    assert(it.getCurrent().key == "Chair");
    it.next();
    it.next();
    it.next();
    it.next();
    assert(it.valid() == false);
    
}

void Tests::testRelation(){
    TElement a,b;
    a.key = "aa";
    b.key = "bb";
    a.value = "";
    b.value = "";
    assert(relation(a, b) == false);
    assert(relation(b, a) == true);
}

void Tests::testRemove(){
    SortedMap sm{&relation};
    sm.add("Ghost","A");
    sm.add("Chair","B");
    sm.add("Inspiration","C");
    sm.add("Apple","d");
    sm.add("Word","haha");
    sm.remove("Ghost");
    assert(sm.size() == 4);
    sm.remove("Apple");
    assert(sm.size() == 3);
    sm.remove("Chair");
    assert(sm.size() == 2);
    sm.remove("Inspiration");
    assert(sm.size() == 1);
    sm.remove("Word");
    assert(sm.size() == 0);
    try {
        sm.add("Ghost", "bla bla");
    } catch (std::string &e){
        
    }
}
