//
// Created by Gal Oscar on 04/06/2017.
//

#include "BasketQt.h"
#include <QMessageBox>
#include "RepositoryExceptions.h"
#include <algorithm>
#include <random>


BasketQt::BasketQt(Controller& c, QWidget *parent) : ctrl{ c }, QWidget { parent } {
    this->initGUI();
    this->currentCoatsInRepoList = this->ctrl.getAllCoats();
    this->populateRepoList();
}

BasketQt::~BasketQt() {

}

void BasketQt::initGUI() {
    QHBoxLayout* layout = new QHBoxLayout{this};

    QWidget* leftWidget = new QWidget{};
    QVBoxLayout* leftSide = new QVBoxLayout{ leftWidget };

    this->repoList = new QListWidget{};

    this->repoList->setSelectionMode(QAbstractItemView::SingleSelection);

    // coat data
    QWidget* coatDataWidget = new QWidget{};
    QFormLayout* formLayout = new QFormLayout{coatDataWidget};
    this->idEdit = new QLineEdit{};
    this->sizeEdit = new QLineEdit{};
    this->colorEdit = new QLineEdit{};
    this->priceEdit = new QLineEdit{};
    this->quantityEdit = new QLineEdit{};
    this->photoEdit = new QLineEdit{};
    this->lengthEdit = new QLineEdit{};
    formLayout->addRow("&Id:", idEdit);
    formLayout->addRow("&Size:", sizeEdit);
    formLayout->addRow("&Color:", colorEdit);
    formLayout->addRow("&Price:", priceEdit);
    formLayout->addRow("&Quantity:", quantityEdit);
    formLayout->addRow("&Photo:", photoEdit);
    formLayout->addRow("&Length:", lengthEdit);

    // buttons
    QWidget* buttonsWidget = new QWidget{};
    QGridLayout* gridLayout = new QGridLayout{ buttonsWidget };
    this->addButton = new QPushButton("Add");
    this->deleteButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");
    this->filterButtonSize = new QPushButton("Filter Size");
    this->filterButtonLength = new QPushButton("Filter Lenght");

    gridLayout->addWidget(addButton, 0, 0);
    gridLayout->addWidget(deleteButton, 0, 1);
    gridLayout->addWidget(updateButton, 0, 2);
    gridLayout->addWidget(filterButtonSize, 0, 3);
    gridLayout->addWidget(filterButtonLength, 0, 4);

    this->normal = new QRadioButton {" Normal "};
    this->sorted = new QRadioButton {" Sorted "};

    leftSide->addWidget(new QLabel{"All coats available"});
    leftSide->addWidget(this->normal);
    leftSide->addWidget(this->sorted);
    leftSide->addWidget(repoList);
    leftSide->addWidget(coatDataWidget);
    leftSide->addWidget(buttonsWidget);

    QWidget* middleWidget = new QWidget{};
    QVBoxLayout* vLayoutMiddle = new QVBoxLayout{ middleWidget };
    this->moveOneCoatButton = new QPushButton{ ">> Move one coat to cart" };
    this->moveAllCoatsButton = new QPushButton{ ">> Move all coats to cart" };
    QWidget* upperPart = new QWidget{};
    QWidget* lowerPart = new QWidget{};
    QVBoxLayout* vLayoutUpperPart = new QVBoxLayout{ upperPart };
    vLayoutUpperPart->addWidget(this->moveOneCoatButton);
    vLayoutUpperPart->addWidget(this->moveAllCoatsButton);
    vLayoutMiddle->addWidget(upperPart);
    vLayoutMiddle->addWidget(lowerPart);

    QWidget* rightWidget = new QWidget{};
    QVBoxLayout* rightSide = new QVBoxLayout{ rightWidget };

    basket = new QListWidget{};

    rightSide->addWidget(new QLabel{ "Basket" });
    rightSide->addWidget(basket);
    rightSide->addWidget(new QLabel{"Total"});
    this->basketMoney = new QLineEdit{};
    rightSide->addWidget(this->basketMoney);

    layout->addWidget(leftWidget);
    layout->addWidget(middleWidget);
    layout->addWidget(rightWidget);

    this->connectSignalsAndSlots();
}

void BasketQt::connectSignalsAndSlots() {

    QObject::connect(this->repoList, SIGNAL(itemSelectionChanged()), this, SLOT(listItemChanged()));

    QObject::connect(this->addButton, SIGNAL(clicked()), this, SLOT(addNewCoat()));
    QObject::connect(this->deleteButton, SIGNAL(clicked()), this, SLOT(deleteCoat()));
    QObject::connect(this->updateButton, SIGNAL(clicked()), this, SLOT(updateCoat()));
    QObject::connect(this->filterButtonSize, SIGNAL(clicked()), this, SLOT(filterRepoCoatBySize()));
    QObject::connect(this->filterButtonLength, SIGNAL(clicked()), this, SLOT(filterRepoCoatByLength()));
    QObject::connect(this->sorted, SIGNAL(clicked()), this, SLOT(suffleList()));
    QObject::connect(this->normal, SIGNAL(clicked()), this, SLOT(normalList()));

    QObject::connect(this->moveOneCoatButton, SIGNAL(clicked()), this, SLOT(moveCoatToBasket()));
    QObject::connect(this->moveAllCoatsButton, SIGNAL(clicked()), this, SLOT(moveAllCoats()));
}

void BasketQt::populateRepoList() {
    // clear the list, if there are elements in it
    if (this->repoList->count() > 0)
        this->repoList->clear();

    for (auto s : this->currentCoatsInRepoList)
    {
        QString itemInList = QString::fromStdString("Id: " + s.toStringId() + " | Size: "+ s.toStringSize() + " | Color: " + s.getColor() + " | Price: " + s.toStringPrice() + " | Quantity: " + s.toStringQuantity() + " | Length: " + s.toStringLength());
        QListWidgetItem *item3 = new QListWidgetItem(itemInList);
        //QFont font("Courier", 20, 10, true);
        //item3->setFont(font);
        this->repoList->addItem(item3);
    }

    // set the selection on the first item in the list
    if (this->currentCoatsInRepoList.size() > 0)
        this->repoList->setCurrentRow(0);
}

void BasketQt::populateBasket() {
    // clear the list, if there are elements in it
    if (this->basket->count() > 0)
        this->basket->clear();

    for (auto s : this->ctrl.getCoatsFromBasket())
    {
        QString itemInList = QString::fromStdString("Id: " + s.toStringId() + " | Size: "+ s.toStringSize() + " | Color: " + s.getColor() + " | Price: " + s.toStringPrice() + " | Quantity: " + s.toStringQuantity() + " | Length: " + s.toStringLength());
        this->basket->addItem(itemInList);
    }
    this->basketMoney->clear();
    std::string something = this->ctrl.getMoney();
    this->basketMoney->setText(QString::fromStdString(something));
}

int BasketQt::getRepoListSelectedIndex() {
    if (this->repoList->count() == 0)
        return -1;

    // get selected index
    QModelIndexList index = this->repoList->selectionModel()->selectedIndexes();
    if (index.size() == 0)
    {
        this->idEdit->clear();
        this->sizeEdit->clear();
        this->colorEdit->clear();
        this->priceEdit->clear();
        this->quantityEdit->clear();
        this->photoEdit->clear();
        this->lengthEdit->clear();
        return -1;
    }

    int idx = index.at(0).row();
    return idx;
}

void BasketQt::listItemChanged() {
    int idx = this->getRepoListSelectedIndex();
    if (idx == -1)
        return;

    std::vector<Coat> coats = this->currentCoatsInRepoList;

    // get the song at the selected index
    if (idx >= coats.size())
        return;
    Coat c = coats[idx];

    this->idEdit->setText(QString::fromStdString(c.toStringId()));
    this->sizeEdit->setText(QString::fromStdString(c.toStringSize()));
    this->colorEdit->setText(QString::fromStdString(c.getColor()));
    this->priceEdit->setText(QString::fromStdString(c.toStringPrice()));
    this->quantityEdit->setText(QString::fromStdString(c.toStringQuantity()));
    this->photoEdit->setText(QString::fromStdString(c.getPhoto()));
    this->lengthEdit->setText(QString::fromStdString(c.toStringLength()));
}

void BasketQt::addNewCoat() {
    int id = this->idEdit->text().toInt();
    int size = this->sizeEdit->text().toInt();
    std::string color = this->colorEdit->text().toStdString();
    float price = this->priceEdit->text().toFloat();
    int quantity = this->quantityEdit->text().toInt();
    std::string photo = this->photoEdit->text().toStdString();
    float length = this->lengthEdit->text().toFloat();

    try
    {
        this->ctrl.addCoatToRepo(id, size, color, price, quantity, photo, length);
        // refresh the list
        this->currentCoatsInRepoList = this->ctrl.getAllCoats();
        this->populateRepoList();
    }
    catch (CoatException& e)
    {
        QMessageBox messageBox;
        messageBox.critical(0, "Error", QString::fromStdString(e.getErrorsAsString()));
    }
    catch (DuplicateCoatException& e)
    {
        QMessageBox messageBox;
        messageBox.critical(0, "Error", e.what());
    }
}

void BasketQt::deleteCoat() {
    int id = this->idEdit->text().toInt();
    try
    {
        this->ctrl.removeCoatFromRepo(id);
        // refresh the list
        this->currentCoatsInRepoList = this->ctrl.getAllCoats();
        this->populateRepoList();
    }
    catch (InexistenCoatException& e)
    {
        QMessageBox messageBox;
        messageBox.critical(0, "Error", e.what());
    }
}

void BasketQt::updateCoat() {
    int id = this->idEdit->text().toInt();
    float price = this->priceEdit->text().toFloat();
    int quantity = this->quantityEdit->text().toInt();
    try{
        this->ctrl.updateCoatInRepo(id, price, quantity);
        this->currentCoatsInRepoList = this->ctrl.getAllCoats();
        this->populateRepoList();
    }
    catch (InexistenCoatException& e){
        QMessageBox messageBox;
        messageBox.critical(0, "Error", e.what());
    }
}
void BasketQt::filterRepoCoatBySize() {
    int size = this->sizeEdit->text().toInt();

    this->currentCoatsInRepoList = this->ctrl.filterBySize(size);
    this->populateRepoList();
}

void BasketQt::filterRepoCoatByLength(){
    float length = this->lengthEdit->text().toFloat();

    this->currentCoatsInRepoList = this->ctrl.filterCoatsByLength(length);
    this->populateRepoList();
}

void BasketQt::moveCoatToBasket() {
    int idx = this->getRepoListSelectedIndex();
    if (idx == -1 || idx >= this->currentCoatsInRepoList.size())
        return;

    Coat& c = this->currentCoatsInRepoList[idx];
    c.setQuantity(1);
    this->ctrl.addCoatToBasket(c);
    this->populateBasket();
}

void BasketQt::moveAllCoats() {
    for (auto s : this->currentCoatsInRepoList)
    {
        s.setQuantity(1);
        this->ctrl.addCoatToBasket(s);
    }
    this->populateBasket();
}

void BasketQt::suffleList() {
    auto engine = std::default_random_engine{};
    std::shuffle(std::begin(this->currentCoatsInRepoList), std::end(this->currentCoatsInRepoList), engine);
    populateRepoList();
}

bool cmp(Coat a, Coat b){
    return a.getId() < b.getId();
}

void BasketQt::normalList(){
    std::sort(this->currentCoatsInRepoList.begin(), this->currentCoatsInRepoList.end(), cmp);
    populateRepoList();
}
