#include <iostream>
using namespace std;

// Template class for AutoGrowingArray
template <typename T>
class AutoGrowingArray {
private:
    T* array; // Pointer to the array
    int size; // Current size of the array
    int capacity; // Current capacity of the array

    // Function to grow the array by increasing capacity by 1
    void grow() {
        capacity++;
        T* newArray = new T[capacity];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        delete[] array;
        array = newArray;
    }

public:
    // Constructor to initialize the array with size 0 and capacity 1
    AutoGrowingArray() : size(0), capacity(1) {
        array = new T[capacity];
    }

    // Destructor to free allocated memory
    ~AutoGrowingArray() {
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
    friend ostream& operator<<(ostream& out, const AutoGrowingArray& other) {
        for (int i = 0; i < other.size; i++) {
            out << other.array[i] << " ";
        }
        return out;
    }
};

// int main() {
//     AutoGrowingArray<int> arr; // Create an instance of AutoGrowingArray
//     int choice, value, index;

//     // Menu-driven program to demonstrate the functionalities
//     while (true) {
//         cout << "\nMenu:\n";
//         cout << "1. PushBack\n";
//         cout << "2. Get element by index\n";
//         cout << "3. Print array\n";
//         cout << "4. Exit\n";
//         cout << "Enter your choice: ";
//         cin >> choice;
//         if(choice==1){
//                 cout << "Enter value to push: ";
//                 cin >> value;
//                 arr.PushBack(value);
//         }
//         if(choice==2){

//             cout << "Enter index: ";
//                 cin >> index;
//                 cout << "Element at index " << index << " is " << arr[index] << endl;
//         }
//         if(choice==3){
//             cout << "Array: " << arr << endl;
//         }
//         if(choice==4){
//             return 0;
//         }
//         if(choice<1 || choice>4){
//             cout << "Invalid choice. Try again.\n";
//         }

        
//     }
// }