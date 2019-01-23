//
// Created by Gal Oscar on 18/05/2017.
//
#include <qapplication.h>
#include "GeneRepository.h"
#include "tableviewexample.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    GeneRepository repo("genes.txt");
    TableViewExample w{repo};
    w.show();
    return a.exec();
}