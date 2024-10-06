#include <iostream>
using namespace std;

// Template class for ArrayList
template <typename T>
class ArrayList {
private:
    T* array; // Pointer to the array
    int size; // Current size of the array
    int capacity; // Current capacity of the array

    // Function to grow the array by increasing its capacity by a factor of 1.5
    void grow() {
        capacity = capacity + capacity / 2; // Increase capacity by 1.5 times
        T* newArray = new T[capacity];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        delete[] array;
        array = newArray;
    }

public:
    // Constructor to initialize the array with size 0 and capacity 2
    ArrayList() : size(0), capacity(2) {
        array = new T[capacity];
    }

    // Destructor to free allocated memory
    ~ArrayList() {
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
    friend ostream& operator<<(ostream& out, const ArrayList& other) {
        for (int i = 0; i < other.size; i++) {
            out << other.array[i] << " ";
        }
        return out;
    }
};

int main() {
    ArrayList<int> arr; // Create an instance of ArrayList
    int choice, value, index;

    // Menu-driven program to demonstrate the functionalities
    while (true) {
        cout << "\nMenu:\n";
        cout << "1. PushBack\n";
        
        cout << "2. Get element by index\n";
        cout << "3. Print array\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to push: ";
            cin >> value;
            arr.PushBack(value);
        } else if (choice == 2) {
            cout << "Enter index: ";
            cin >> index;
           
                cout << "Element at index " << index << " is " << arr[index] << endl;
          
        } else if (choice == 3) {
            cout << "Array: " << arr << endl;
        } else if (choice == 4) {
            return 0;
        } else {
            cout << "Invalid choice. Try again.\n";
        }
    }
}