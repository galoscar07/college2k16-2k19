//
//  Ui.c
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Ui.h"
#include <stdlib.h>

OfferUi* createUi(OfferController* of){
    OfferUi *ui = (OfferUi*)malloc(sizeof(OfferUi));
    ui->ctrl = of;
    return ui;
}

void destroyUi(OfferUi* ui){
    destroyController(ui->ctrl);
    free(ui);
}

void printMenu(){
    printf("Available Commands: \n");
    printf("\t 1 - Add an offer.\n");
    printf("\t 2 - Delete an offer.\n");
    printf("\t 3 - Update an offer.\n");
    printf("\t 4 - List all offers.\n");
    printf("\t 5 - Display all the tourism offers by a given string.\n");
    printf("\t 6 - Display all offers having a given type and a price less than a given value, sorted ascending by price.\n");
    printf("\t 7 - Display all offers of a given type, starting from a given date. \n");
    printf("\t 8 - Undo \n");
    printf("\t 9 - Redo \n");
    printf("\t 10 - Display all offers of a given type, sorted ascending by destination. \n");
    printf("\t 0 - to exit.\n");
    //printf("\n");
}

int validCommand(int command){
    if (command >= 0 && command <= 10)
        return 1;
    return 0;
}


int readIntegerNumber(const char message[])
{
    char s[16];
    int res = 0;
    int flag = 0;
    int r = 0;
    
    while (flag == 0)
    {
        printf("%s",message);
        scanf("%s", s);
        
        r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
        flag = (r == 1);
        if (flag == 0)
            printf("Error reading number!\n");
    }
    return res;
}

int addOfferUi(OfferUi* ui){
    char type[21], destination[26];
    calendar departureDate;
    int price;
    
    printf("Please give a type (must contain 20 letters): \n");
    scanf("%20s", type);
    printf("Please give a destination (must contain 25 letters): \n");
    scanf("%25s", destination);
    printf("Please input the date: \n");
    printf("First the day: ");
    scanf("%d", &departureDate.day);
    printf("Secound the month: ");
    scanf("%d", &departureDate.month);
    printf("Third the year:");
    scanf("%d", &departureDate.year);
    printf("And finally please give a price: \n");
    scanf("%d", &price);
    return addOfferController(ui->ctrl, type, destination, departureDate, price);
}

int deleteOfferUi(OfferUi* ui){
    char destination[26];
    calendar departureDate;
    printf("Please give a destination (must contain 25 letters): \n");
    scanf("%25s", destination);
    printf("Please input the date: \n");
    printf("First the day: ");
    scanf("%d", &departureDate.day);
    printf("Secound the month: ");
    scanf("%d", &departureDate.month);
    printf("Third the year:");
    scanf("%d", &departureDate.year);
    return deleteOfferController(ui->ctrl, destination, departureDate);
    
}

int updateOfferUI(OfferUi* ui){
    char type[21], destination[26];
    calendar departureDate;
    int price;
    
    printf("If you want to update write something, else just put a '-' for string and 0 for int \n");
    printf("Please give a type (must contain 20 letters): \n");
    scanf("%20s", type);
    printf("Please give a destination (must contain 25 letters): \n");
    scanf("%25s", destination);
    printf("Please input the date: \n");
    printf("First the day: ");
    scanf("%d", &departureDate.day);
    printf("Secound the month: ");
    scanf("%d", &departureDate.month);
    printf("Third the year:");
    scanf("%d", &departureDate.year);
    printf("And finally please give a price: \n");
    scanf("%d", &price);
    return updateOfferController(ui->ctrl, type, destination, departureDate, price);
}

void listAllOffers(OfferUi* ui){
    OfferRepository* repo = createRepo();
    for (int i=0; i< getLengthRepo(ui->ctrl->repo); i++){
        Offer *o = getOfferOnPositionRepo(ui->ctrl->repo, i);
        addRepo(repo, o);
    }
    int length = getLengthRepo(repo);
    if (length == 0){
        printf("There are no offers in the program.\n");
    }
    else {
        int i;
        for(i = 0; i < getLengthRepo(repo); i++){
            char str[300];
            toString(*getOfferOnPositionRepo(repo, i), str);
            printf("%s\n", str);
        }
    }
    destroyRepo(repo);
}

void listOfferWithString(OfferUi* ui){
    char destination[26];
    printf("Please input the destination combination (must contain maximum 25 letters), imput 'null' for no combination: ");
    scanf("%25s", destination);
    OfferRepository *something = filterByDestinationCombinationController(ui->ctrl,destination);
    int length = getLengthRepo(something);
    if (length == 0){
        printf("There are no offers with the given description to print.");
    }
    else{
        for (int i = 0; i < length; i++){
            char str[200];
            toString(*getOfferOnPositionRepo(something, i), str);
            printf("%s\n",str);
        }
    }
    destroyRepo(something);
}
void listOfferWithPrice(OfferUi* ui){
    char type[21];
    int pri;
    printf("Please input a type: ");
    scanf("%20s", type);
    printf("Please input a price: ");
    scanf("%d",&pri);
    OfferRepository *something = filterByPriceController(ui->ctrl,type,pri);
    int length = getLengthRepo(something);
    if (length == 0){
        printf("There are no offers with the given type to print.\n");
    }
    else{
        for (int i = 0; i < length; i++){
            char str[200];
            toString(*getOfferOnPositionRepo(something, i), str);
            printf("%s\n",str);
        }
    }
    destroyRepo(something);
}

void listOfferWithPriceDate(OfferUi* ui){
    char type[21];
    calendar date;
    printf("Please input a type: ");
    scanf("%20s", type);
    printf("Please input the date: \n");
    printf("First the day: ");
    scanf("%d", &date.day);
    printf("Secound the month: ");
    scanf("%d", &date.month);
    printf("Third the year:");
    scanf("%d", &date.year);
    OfferRepository* something = filterByPriceDateController(ui->ctrl, type, date);
    int length = getLengthRepo(something);
    if (length == 0){
        printf("There are no offers with the given type and date to be printed. \n");
    }
    else{
        for (int i = 0; i < length; i++){
            char str[200];
            toString(*getOfferOnPositionRepo(something, i), str);
            printf("%s\n",str);
        }
    }
    destroyRepo(something);
}

void listOfferWithTypeDestination(OfferUi* ui){
    char type[21];
    printf("Please input a type: ");
    scanf("%20s", type);
    OfferRepository* something = filterOfferWithTypeDestinationController(ui->ctrl, type);
    int length = getLengthRepo(something);
    if (length == 0){
        printf("There are no offers with the given type and date to be printed. \n");
    }
    else{
        for (int i = 0; i < length; i++){
            char str[200];
            toString(*getOfferOnPositionRepo(something, i), str);
            printf("%s\n",str);
        }
    }
    destroyRepo(something);
}

void mainLoop(OfferUi* ui){
    int keepAlive = 1;
    startUp(ui->ctrl);
    while(keepAlive){
        printMenu();
        printf("Command: ");
        int command = readIntegerNumber("");
        while (validCommand(command) == 0){
            printf("Please input a valid command! \n");
            command = readIntegerNumber("Input command: ");
        }
        if (command == 0){
            printf("Thank you for using the program :) \n");
            break;
        }
        switch (command) {
            case 1:{
                int something = addOfferUi(ui);
                if (something == 1)
                    printf("Offer successfully added.\n");
                else
                    printf("Error! Offer cannot be added because there is another offer with the same destination and departure date...\n");
                break;
            }
                
            case 2:{
                int something = deleteOfferUi(ui);
                if (something == 1)
                    printf("Offer successfully deleted.\n");
                else
                    printf("Error! Offer cannot be deleted because there is not an offer with the same destination and departure date...\n");
                break;
            }
            
            case 3:{
                int something = updateOfferUI(ui);
                if (something == 1)
                    printf("Offer sucessfully updated. \n");
                else
                    printf("Error! Offer cannot be updated because there is not an offer with the same destination and departure date ...");
                break;
            }
        
            case 4:{
                listAllOffers(ui);
                break;
            }
                
            case 5:{
                listOfferWithString(ui);
                break;
            }
            case 6:{
                listOfferWithPrice(ui);
                break;
            }
            case 7:{
                listOfferWithPriceDate(ui);
                break;
            }
            case 8:{
                int something = undoController(ui->ctrl);
                if (something == 0){
                    printf("Nothing to undo.. \n");
                }
                else {
                    printf("The undo worked \n");
                }
                break;
            }
            case 9:{
                int something = redoController(ui->ctrl);
                if (something == 0){
                    printf("Nothing to redo.. \n");
                }
                else {
                    printf("The redo worked \n");
                }
                break;
            }
            case 10:{
                listOfferWithTypeDestination(ui);
                break;
            }
        }
    }
}
