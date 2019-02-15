#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <cassert>
#include <chrono>

using namespace std;

const int MAXN = 2001;
const int MAXT[] = {1, 3, 10, 30, 100, 300, 1000};

int n, m;
int a[MAXN][MAXN], b[MAXN][MAXN], c[MAXN][MAXN];

template <class T>
void loadData(T a[MAXN][MAXN], T b[MAXN][MAXN], string fileName) {
    // function that reads the data from a file
    // open the file
    ifstream fin(fileName);
    // read number of columns and rows
    fin >> n >> m;
    // parse and save the first matrix
    for(int i = 0; i < n ;++ i) {
        for(int j = 0; j < m; ++ j) {
            fin >> a[i][j];
        }
    }
    // parse and save the second matrix
    for(int i = 0; i < n ;++ i) {
        for(int j = 0; j < m; ++ j) {
            fin >> b[i][j];
        }
    }
}

void addLines(int line, int T) {
    // function that adds line, line + T, line + 2 * T and so on
    for(int i = line; i < n; i += T) {
        for(int j = 0; j < m; ++ j) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}

inline void addMat(int T, bool check = false) {
    // note the time in which we start
    auto start = std::chrono::high_resolution_clock::now();
    // creates a list of threads
    vector <thread> threads;
    // read the data calling the function loadData
    loadData<int>(a, b, "/Users/galoscar/Documents/uni&shit/Parallel and Distributed Programming/Laboratory/LabAssignment2/add.in");
    cerr << "Matrix of dimension " << n << '\n';
    // creates threads either for every line or the number of threads T, put them into the threads list
    for(int i = 0; i < min(T, n); ++ i) {
        threads.push_back(thread(addLines, i, T));
    }
    // join them
    for(int i = 0; i < min(T, n); ++ i) {
        threads[i].join();
    }
    if (check) {
        for(int i = 0; i < n; ++ i) {
            for(int j = 0; j < m; ++ j) {
                assert(c[i][j] == a[i][j] + b[i][j]);
                cerr << c[i][j] << ' ';
            }
        cerr << '\n';
        }
    }
    auto finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    cerr << "Elapsed time: " << elapsed.count() << '\n';
}

inline void statistics() {
    for(int i = 0; i < 7; ++ i) {
        int t = MAXT[i];
        cerr << t << " threads\n";
        addMat(t);
    }
}

int main() {
    statistics();
    return 0;
}
