#include "equations.h"
#include <qpushbutton.h>
#include <qlistwidget.h>
#include <sstream>
#include <qmessagebox.h>


Equations::Equations(Controller con,QWidget *parent)
	: QMainWindow(parent)
{
	this->cont = con;
	ui.setupUi(this);
	this->connectSignalsAndSlots();
	this->ui.combo->insertItem(0, QString::fromStdString("All"));
	this->ui.combo->insertItem(1, QString::fromStdString("Real"));
	this->ui.combo->insertItem(2, QString::fromStdString("Imaginary"));
	emit listUpdatedSignal();
}

Equations::~Equations()
{

}

void Equations::connectSignalsAndSlots()
{
	connect(this->ui.updateButton, &QPushButton::clicked, this, &Equations::updateEquation);
	connect(this->ui.list, &QListWidget::itemSelectionChanged, this, &Equations::fillBoxes);
	connect(this, &Equations::listUpdatedSignal, this, &Equations::populate);
	connect(this->ui.solve, &QPushButton::clicked, this, &Equations::solveEquation);
	connect(this->ui.combo, &QComboBox::currentTextChanged, this, &Equations::populate);
}

void Equations::solveEquation()
{
	for (auto e : this->cont.getAll()) {
		if (e.equation() == this->ui.list->currentItem()->text().toStdString()) {
			this->ui.solution->setText(QString::fromStdString(e.solutions()));
			break;
		}
	}
}

double to_double(std::string a) {
	std::istringstream iss(a);
	double f;
	iss >> std::noskipws >> f;
	
	if (iss.eof() && !iss.fail())
		return f;
	else
		throw 1;
}

void Equations::updateEquation()
{
	if (this->ui.list->count() == 0)
		return;

	std::vector<Quadratic> v = this->cont.getAll();
	
	int i;
	for (i = 0; i < v.size(); i++)
		if (v[i].equation() == this->ui.list->currentItem()->text().toStdString())
			break;

	double a, b, c;
	std::string aS, bS, cS;

	aS = this->ui.aEdit->text().toStdString();
	bS = this->ui.bEdit->text().toStdString();
	cS = this->ui.cEdit->text().toStdString();
	
	try
	{
		a = to_double(aS);
		b = to_double(bS);
		c = to_double(cS);
	}
	catch (int a) {
		QMessageBox msg;
		msg.setText("Invalid input!");
		msg.exec();
		return;
	}

	this->cont.update(i, a, b, c);
	emit listUpdatedSignal();
}

void Equations::fillBoxes()
{
	if (this->ui.list->count() == 0)
		return;

	for (auto e : this->cont.getAll()) {
		if (e.equation() == this->ui.list->currentItem()->text().toStdString()) {
			this->ui.aEdit->setText(QString::fromStdString(std::to_string(e.getA())));
			this->ui.bEdit->setText(QString::fromStdString(std::to_string(e.getB())));
			this->ui.cEdit->setText(QString::fromStdString(std::to_string(e.getC())));
			break;
		}
	}
}

void Equations::populate()
{
	if (this->ui.list->count() > 0) {
		this->ui.list->clear();
	}

	std::vector<Quadratic> v = this->cont.filter(this->ui.combo->currentText().toStdString());
	
	for (auto e : v) {
			QString itemInList = QString::fromStdString(e.equation());
			QListWidgetItem* item = new QListWidgetItem{ itemInList };
			this->ui.list->addItem(item);
			}
		
	if (this->ui.list->count() > 0) {
		this->ui.list->setCurrentRow(0);
	}
}