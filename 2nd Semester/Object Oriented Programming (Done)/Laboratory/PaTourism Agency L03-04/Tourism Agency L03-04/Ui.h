//
//  Ui.h
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include "Controller.h"

typedef struct{
    OfferController* ctrl;
}OfferUi;

OfferUi* createUi(OfferController* of);
    /*
     This function will create an ui
     */
void destroyUi(OfferUi* ui);


void mainLoop(OfferUi* ui);
    /*
     The function will start the ui. The main loop will be here, with the menu
    */

