//
// Created by Gal Oscar on 18/06/2017.
//

#ifndef EQUATION_UI_H
#define EQUATION_UI_H

#include <QtWidgets/QMainWindow>
#include <QtWidgets/qradiobutton.h>
#include "Controller.h"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>


class Gui : public QWidget{
    Q_OBJECT
public:
    Gui(Controller& c, QWidget* parent = 0);
    ~Gui();
private:
    Controller& contr;
    std::vector<Equation> currentEquations;

    QListWidget* list;
    QLineEdit* aEdit;
    QLineEdit* bEdit;
    QLineEdit* cEdit;
    QLineEdit* showSolutiuon;
    QRadioButton* all;
    QRadioButton* imaginary;
    QRadioButton* real;
    QPushButton* updateButton;
    QPushButton* solutionButton;

    void initGui();
    void populateList();
    int getListSelectedIndex();
    void connectSignalsAndSlots();

private: slots
    void listItemChanged();
    void allList();
    void updateEquation();
    void solutionEquation();
    void realList();
    void imaginaryList();
};




#endif //EQUATION_UI_H
