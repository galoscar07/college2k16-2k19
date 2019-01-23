//
//  main.cpp
//  DSAProject
//
//  Created by Gal Oscar on 09/06/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
/*
#include <iostream>
#include "SortedMap.hpp"
#include "Ui.hpp"

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    Tests t;
    t.testAll();
    //SortedMap sort{&relation};
    //Ui console = Ui(sort);
    //console.run();
    return 0;
}
*/
#include <iostream>
#include <stdlib.h>

using namespace std;

void getUserGuesses(int spot[2]);
void printBoard(char field[10][10]);
bool isHit(int guessSpot[2], int shipSpot[2]);
void changeBoard(char field[10][10], bool hit, int guessSpot[2]);

int main() {

    char field[10][10];
    int missCount = 1, spot[2], row, col, count;
    bool hit = true;
    int shipSpot[2], guessSpot[2];

    //Creates initial field
    for (int i = 0; i < 10; i++) {
        for (int k = 0; k < 10; k++) {
            field[i][k] = 'O';
        }
    }

    cout << "Welcome to BattleShip!" << endl;
    cout << "Your objective is to sink my 1 space ship on this board:\n" << endl;
    printBoard(field);
    cout << "\nYou'll do that by gussing a row and column position" << endl;

    //Initialize ship spot
    row = rand() % 10;
    col = rand() % 10;
    shipSpot[0] = row;
    shipSpot[1] = col;

    //Get user guesses
    getUserGuesses(guessSpot);
    
    hit = isHit(guessSpot, shipSpot);

    while (missCount < 11 && !hit) {
        changeBoard(field, hit, guessSpot);
        printBoard(field);
        cout << "\nYou missed! Try again" << endl;
        getUserGuesses(guessSpot);
        hit = isHit(guessSpot, shipSpot);
        missCount++;
    }

    changeBoard(field, hit, guessSpot);

    if (missCount == 11) {
        cout << "You couldn't hit water if you fell out of a boat!" << endl;
    } else {
        cout << "It took you " << missCount << " trie(s) to hit my ship." << endl;
    }

    printBoard(field);
    
    return 0;
}

void getUserGuesses(int spot[2]) {
    /*
        This function gets the user's row and column guess and returns the address of the
        resulting array
    */
    cout << "Please guess the row: ";
    cin >> spot[0];
    cout << "Please guess the column: ";
    cin >> spot[1];
}

void printBoard(char field[10][10]) {
    /*
        This function prints the 2D array field
    */
    for (int i = 0; i < 10; i++) {
        for (int k = 0; k < 10; k++) {
            cout << field[i][k]<< " ";
        }
        cout << endl;
    }
}

bool isHit(int guessSpot[2], int shipSpot[2]) {
    /*
        This function returns true iff both the column and row guesses match 
        the column and row spot of the ship's position
    */
    if (shipSpot[0] == guessSpot[0]) {
        if (shipSpot[1] == guessSpot[1]) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

void changeBoard(char field[10][10], bool hit, int guessSpot[2]) {
    /*
        This function will change the board with a '!' for a hit and a
        'X' for a miss so the player can keep track
    */
    if (hit) {
        field[guessSpot[0]][guessSpot[1]] = '!';
    } else {
        field[guessSpot[0]][guessSpot[1]] = 'X';
    }
}

