#include "Ui.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Repository rep{ "/Users/galoscar/Documents/College/Semester 2/Object Oriented Programming/Tests:Exams/Equation/equations.txt" };
    Controller cont{ rep };
    Gui w{ cont };
    w.show();
    return a.exec();
}
