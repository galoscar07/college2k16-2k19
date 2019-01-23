/********************************************************************************
** Form generated from reading UI file 'equations.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_EQUATIONS_H
#define UI_EQUATIONS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_EquationsClass
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QLabel *aLabel;
    QLabel *bLabel;
    QComboBox *combo;
    QLineEdit *aEdit;
    QListWidget *list;
    QLineEdit *bEdit;
    QLineEdit *cEdit;
    QLabel *cLabel;
    QPushButton *updateButton;
    QPushButton *solve;
    QLabel *solution;

    void setupUi(QMainWindow *EquationsClass)
    {
        if (EquationsClass->objectName().isEmpty())
            EquationsClass->setObjectName(QStringLiteral("EquationsClass"));
        EquationsClass->resize(425, 167);
        centralWidget = new QWidget(EquationsClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        aLabel = new QLabel(centralWidget);
        aLabel->setObjectName(QStringLiteral("aLabel"));

        gridLayout->addWidget(aLabel, 0, 3, 1, 1);

        bLabel = new QLabel(centralWidget);
        bLabel->setObjectName(QStringLiteral("bLabel"));

        gridLayout->addWidget(bLabel, 1, 3, 1, 1);

        combo = new QComboBox(centralWidget);
        combo->setObjectName(QStringLiteral("combo"));

        gridLayout->addWidget(combo, 4, 0, 1, 1);

        aEdit = new QLineEdit(centralWidget);
        aEdit->setObjectName(QStringLiteral("aEdit"));

        gridLayout->addWidget(aEdit, 0, 1, 1, 1);

        list = new QListWidget(centralWidget);
        list->setObjectName(QStringLiteral("list"));

        gridLayout->addWidget(list, 0, 0, 4, 1);

        bEdit = new QLineEdit(centralWidget);
        bEdit->setObjectName(QStringLiteral("bEdit"));

        gridLayout->addWidget(bEdit, 1, 1, 1, 1);

        cEdit = new QLineEdit(centralWidget);
        cEdit->setObjectName(QStringLiteral("cEdit"));

        gridLayout->addWidget(cEdit, 2, 1, 1, 1);

        cLabel = new QLabel(centralWidget);
        cLabel->setObjectName(QStringLiteral("cLabel"));

        gridLayout->addWidget(cLabel, 2, 3, 1, 1);

        updateButton = new QPushButton(centralWidget);
        updateButton->setObjectName(QStringLiteral("updateButton"));

        gridLayout->addWidget(updateButton, 3, 1, 1, 1);

        solve = new QPushButton(centralWidget);
        solve->setObjectName(QStringLiteral("solve"));

        gridLayout->addWidget(solve, 4, 1, 1, 1);

        solution = new QLabel(centralWidget);
        solution->setObjectName(QStringLiteral("solution"));

        gridLayout->addWidget(solution, 5, 0, 1, 1);

        EquationsClass->setCentralWidget(centralWidget);
#ifndef QT_NO_SHORTCUT
        aLabel->setBuddy(aEdit);
        bLabel->setBuddy(bEdit);
        cLabel->setBuddy(cEdit);
#endif // QT_NO_SHORTCUT

        retranslateUi(EquationsClass);

        QMetaObject::connectSlotsByName(EquationsClass);
    } // setupUi

    void retranslateUi(QMainWindow *EquationsClass)
    {
        EquationsClass->setWindowTitle(QApplication::translate("EquationsClass", "Equations", 0));
        aLabel->setText(QApplication::translate("EquationsClass", "a", 0));
        bLabel->setText(QApplication::translate("EquationsClass", "b", 0));
        cLabel->setText(QApplication::translate("EquationsClass", "c", 0));
        updateButton->setText(QApplication::translate("EquationsClass", "Update", 0));
        solve->setText(QApplication::translate("EquationsClass", "Solve", 0));
        solution->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class EquationsClass: public Ui_EquationsClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_EQUATIONS_H
