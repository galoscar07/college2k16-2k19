#include "equations.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repository rep{ "equations.txt" };
	Controller cont{ rep };
	Equations w{ cont };
	w.show();
	return a.exec();
}
