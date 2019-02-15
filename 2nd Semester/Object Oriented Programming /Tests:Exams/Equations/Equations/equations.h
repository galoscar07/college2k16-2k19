#ifndef EQUATIONS_H
#define EQUATIONS_H

#include <QtWidgets/QMainWindow>
#include "ui_equations.h"
#include "Controller.h"

class Equations : public QMainWindow
{
	Q_OBJECT

public:
	Equations(Controller con, QWidget *parent = 0);
	~Equations();

private:
	Ui::EquationsClass ui;
	Controller cont;

	void connectSignalsAndSlots();
	void updateEquation();
	void fillBoxes();
	void populate();
	void solveEquation();
signals:
	void listUpdatedSignal();
};

#endif // EQUATIONS_H
