#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include "Problem6.cpp" // Include AutoGrowingArray
#include "Problem7.cpp" // Include Vector
#include "Problem8.cpp" // Include ArrayList

using namespace std;

// Function to create a random file
void CreateRandomFile(string fn, int Size, int RN = 100) {
    srand(time(0));
    ofstream Writer(fn);
    if (!Writer.is_open()) {
        cout << "Error: Unable to create file " << fn << endl;
        return;
    }
    for (int i = 0; i < Size * 1024 * 1024; i++) {
        Writer << rand() % RN << " ";
    }
    Writer.close();
    cout << "Random file created: " << fn << endl;
}

// Function to load data into AutoGrowingArray
void LoadAutoGrowingArray(string fn, AutoGrowingArray<int>& arr) {
    ifstream Reader(fn);
    if (!Reader.is_open()) {
        cout << "Error: Unable to open file " << fn << endl;
        return;
    }
    
    int value;
    int count = 0; // Track number of values read
    while (Reader >> value) {
        arr.PushBack(value);
        count++;
        if (count % 1000000 == 0) {
            cout << "Loaded " << count << " values into AutoGrowingArray\n";
        }
    }
    
    Reader.close();
    cout << "Data loaded into AutoGrowingArray, total: " << count << " values" << endl;
}

// Function to load data into Vector
void LoadVector(string fn, Vector<int>& vec) {
    ifstream Reader(fn);
    if (!Reader.is_open()) {
        cout << "Error: Unable to open file " << fn << endl;
        return;
    }

    int value;
    int count = 0; // Track number of values read
    while (Reader >> value) {
        vec.PushBack(value);
        count++;
        if (count % 1000000 == 0) {
            cout << "Loaded " << count << " values into Vector\n";
        }
    }

    Reader.close();
    cout << "Data loaded into Vector, total: " << count << " values" << endl;
}

// Function to load data into ArrayList
void LoadArrayList(string fn, ArrayList<int>& arr) {
    ifstream Reader(fn);
    if (!Reader.is_open()) {
        cout << "Error: Unable to open file " << fn << endl;
        return;
    }

    int value;
    int count = 0; // Track number of values read
    while (Reader >> value) {
        arr.PushBack(value);
        count++;
        if (count % 1000000 == 0) {
            cout << "Loaded " << count << " values into ArrayList\n";
        }
    }

    Reader.close();
    cout << "Data loaded into ArrayList, total: " << count << " values" << endl;
}

// Function to write data to output file
template <typename T>
void WriteToFile(string fn, const T& container) {
    ofstream Writer(fn);
    if (!Writer.is_open()) {
        cout << "Error: Unable to open output file " << fn << endl;
        return;
    }
    Writer << container;
    Writer.close();
    cout << "Data written to file: " << fn << endl;
}

int main() {
    string filename = "random_data.txt";
    int fileSizeMB = 2; // Further reduced file size for testing

    // Create random file
    CreateRandomFile(filename, fileSizeMB);

    // Measure time for AutoGrowingArray
    AutoGrowingArray<int> autoArray;
    time_t start = time(0);
    LoadAutoGrowingArray(filename, autoArray);
    time_t end = time(0);
    cout << "Time taken for AutoGrowingArray: " << difftime(end, start) << " seconds" << endl;
    WriteToFile("OutputGA.txt", autoArray);

    // Measure time for Vector
    Vector<int> vec;
    start = time(0);
    LoadVector(filename, vec);
    end = time(0);
    cout << "Time taken for Vector: " << difftime(end, start) << " seconds" << endl;
    WriteToFile("OutputVector.txt", vec);

    // Measure time for ArrayList
    ArrayList<int> arrList;
    start = time(0);
    LoadArrayList(filename, arrList);
    end = time(0);
    cout << "Time taken for ArrayList: " << difftime(end, start) << " seconds" << endl;
    WriteToFile("OutputArraylist.txt", arrList);

    return 0;
}