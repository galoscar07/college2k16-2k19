//
// Created by Gal Oscar on 18/06/2017.
//

#include "Ui.h"

Gui::Gui(Controller &c, QWidget *parent) : contr{ c }, QWidget { parent } {
    this->initGui();                                                        // Put all the items into a window
    this->currentEquations = this->contr.getAll();                          // Take all the equations from the repository
    this->populateList();                                                   // The function will populate the list with the equations
}

Gui::~Gui() {

}

void Gui::initGui() {
    QHBoxLayout* layout = new QHBoxLayout{this};
    QWidget* leftWidget = new QWidget{};
    QVBoxLayout* leftSide = new QVBoxLayout{ leftWidget };
    this->list = new QListWidget{};
    this->list->setSelectionMode(QAbstractItemView::SingleSelection);
    //Equation Data
    QWidget* equationDataWidget = new QWidget {};
    QFormLayout* formLayout = new QFormLayout{equationDataWidget};
    this->aEdit = new QLineEdit;
    this->bEdit = new QLineEdit;
    this->cEdit = new QLineEdit;
    formLayout->addRow("&A: ", aEdit);
    formLayout->addRow("&B: ", bEdit);
    formLayout->addRow("&C: ", cEdit);
    //Buttons
    QWidget* buttonsWidget = new QWidget{};
    QGridLayout* gridLayout = new QGridLayout{ buttonsWidget };
    this->updateButton = new QPushButton("Update");
    this->solutionButton = new QPushButton("Solution");
    gridLayout->addWidget(updateButton, 0, 0);
    gridLayout->addWidget(updateButton, 0, 1);
    this->all = new QRadioButton {" All "};
    this->real = new QRadioButton {" Real "};
    this->imaginary = new QRadioButton {" Imaginary "};

    leftSide->addWidget(new QLabel{"All Equation in the databse"});
    leftSide->addWidget(this->all);
    leftSide->addWidget(this->real);
    leftSide->addWidget(this->imaginary);
    leftSide->addWidget(list);
    leftSide->addWidget(equationDataWidget);
    leftSide->addWidget(buttonsWidget);
    leftSide->addWidget(new QLabel {" Solution for equation "});
    this->showSolutiuon = new QLineEdit{};
    leftSide->addWidget(showSolutiuon);

    layout->addWidget(leftWidget);

    this->connectSignalsAndSlots();
};

void Gui::populateList() {
    if (this->list->count() > 0) this->list->clear();                       //We check if there are items into the list already

    for (auto s : this->currentEquations){                                  //We parse through all the equations
        QString itemInList = QString::fromStdString(s.toString());          //Make a string out of them
        QListWidgetItem *item3 = new QListWidgetItem(itemInList);           //From string make it to a QListWidgetItem
        this->list->addItem(item3);                                         //Populate the list
    }
    if (this->currentEquations.size() > 0) this->list->setCurrentRow(0);    // If there are elements in the list set the row tot he first element
}

void Gui::connectSignalsAndSlots() {
    QObject::connect(this->list, SIGNAL(itemSelectionChanged()), this, SLOT(listItemChanged()));
    QObject::connect(this->updateButton, SIGNAL(clicked()), this, SLOT(updateEquation()));
    QObject::connect(this->solutionButton, SIGNAL(clicked()), this, SLOT(solutionEquation()));
    QObject::connect(this->all, SIGNAL(clicked()), this, SLOT(allList()));
    QObject::connect(this->real, SIGNAL(clicked()), this, SLOT(realList()));
    QObject::connect(this->imaginary, SIGNAL(clicked()), this, SLOT(imaginaryList()));
}

int Gui::getListSelectedIndex() {
    if (this->list->count() == 0)
        return -1;

    // get selected index
    QModelIndexList index = this->list->selectionModel()->selectedIndexes();
    if (index.size() == 0) {
        this->aEdit->clear();
        this->bEdit->clear();
        this->cEdit->clear();
        return -1;
        }

    int idx = index.at(0).row();
    return idx;
    }

void Gui::listItemChanged() {
    int idx = this->getListSelectedIndex();
    if (idx == -1)
        return;

    std::vector<Equation> ec = this->currentEquations;
    // get the equation at the selected index
    if (idx >= ec.size())
        return;
    Equation c = ec[idx];

    this->aEdit->setText(QString::fromStdString(c.toStringA()));
    this->bEdit->setText(QString::fromStdString(c.toStringB()));
    this->cEdit->setText(QString::fromStdString(c.toStringC()));

}

void Gui::allList() {
    populateList();
}

void Gui::updateEquation() {

}

void Gui::solutionEquation() {

}

void Gui::realList() {

}

void Gui::imaginaryList() {

}

