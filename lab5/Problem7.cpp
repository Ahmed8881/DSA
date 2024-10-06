#include <iostream>
using namespace std;

// Template class for Vector
template <typename T>
class Vector {
private:
    T* array; // Pointer to the array
    int size; // Current size of the array
    int capacity; // Current capacity of the array

    // Function to grow the array by doubling its capacity
    void grow() {
        capacity *= 2;
        T* newArray = new T[capacity];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        delete[] array;
        array = newArray;
    }

public:
    // Constructor to initialize the array with size 0 and capacity 1
    Vector() : size(0), capacity(1) {
        array = new T[capacity];
    }

    // Destructor to free allocated memory
    ~Vector() {
        delete[] array;
    }

    // Function to add elements and grow the array if needed
    void PushBack(T value) {
        if (size == capacity) {
            grow();
        }
        array[size++] = value;
    }

    // Const version of operator[] to access elements
    T operator[](int index) const {
        if (index >= 0 && index < size) {
            return array[index];
        }
        throw out_of_range("Index out of range");
    }

    // Non-const version of operator[] to access elements
    T& operator[](int index) {
        if (index >= 0 && index < size) {
            return array[index];
        }
        throw out_of_range("Index out of range");
    }

    // Friend function to print the array
    friend ostream& operator<<(ostream& out, const Vector& other) {
        for (int i = 0; i < other.size; i++) {
            out << other.array[i] << " ";
        }
        return out;
    }
};

int main() {
    Vector<int> vec; // Create an instance of Vector
    int choice, value, index;

    // Menu-driven program to demonstrate the functionalities
    while (true) {
        cout << "\nMenu:\n";
        cout << "1. PushBack\n";
        cout << "2. Get element by index\n";
        cout << "3. Print vector\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to push: ";
            cin >> value;
            vec.PushBack(value);
        } else if (choice == 2) {
            cout << "Enter index: ";
            cin >> index;
            try {
                cout << "Element at index " << index << " is " << vec[index] << endl;
            } catch (const out_of_range& e) {
                cout << e.what() << endl;
            }
        } else if (choice == 3) {
            cout << "Vector: " << vec << endl;
        } else if (choice == 4) {
            return 0;
        } else {
            cout << "Invalid choice. Try again.\n";
        }
    }
}