using namespace std;

#include "Repository.h"

vector<Equation> Repository::getAll() {
    return this->equations;
}

Repository::Repository(std::string filename) {
    this->filename = filename;
}

Repository::~Repository() {

}

void Repository::load() {
    ifstream f(this->filename);
    int a,b,c;
    while (f >> a){
        f >> b;
        f >> c;
        this->equations.push_back(Equation{a,b,c});
    }
    f.close;
}
