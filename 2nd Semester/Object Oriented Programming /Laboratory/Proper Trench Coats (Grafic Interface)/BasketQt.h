//
// Created by Gal Oscar on 04/06/2017.
//
#ifndef BASKETQT_H
#define BASKETQT_H

#include <QtWidgets/QMainWindow>
#include <QtWidgets/qradiobutton.h>
#include "Controller.h"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>

class BasketQt : public QWidget{
	Q_OBJECT
public:
	BasketQt(Controller& c, QWidget *parent = 0);
	~BasketQt();
private:

	Controller& ctrl;
	std::vector<Coat> currentCoatsInRepoList;

	QListWidget* repoList;
	QLineEdit* idEdit;
	QLineEdit* sizeEdit;
	QLineEdit* colorEdit;
	QLineEdit* priceEdit;
	QLineEdit* quantityEdit;
	QLineEdit* photoEdit;
	QLineEdit* lengthEdit;
    QLineEdit* basketMoney;
    QRadioButton* normal;
    QRadioButton* sorted;
	QPushButton* addButton;
	QPushButton* deleteButton;
	QPushButton* updateButton;
	QPushButton* filterButtonSize;
	QPushButton* filterButtonLength;
	QPushButton* moveOneCoatButton;
	QPushButton* moveAllCoatsButton;

	QListWidget* basket;

	void initGUI();
	void populateRepoList();
	void populateBasket();
	int getRepoListSelectedIndex();

	void connectSignalsAndSlots();

private slots:
	// When an item in the list is clicked, the text boxes get filled with the item's information
	void listItemChanged();

	void addNewCoat();
	void deleteCoat();
	void updateCoat();

	// filters the elements in the list, by the artist written in the artist edit box
	void filterRepoCoatBySize();
	void filterRepoCoatByLength();

	void moveCoatToBasket();
	void moveAllCoats();

	void normalList();
	void suffleList();
};

#endif // BASKETQT_H
