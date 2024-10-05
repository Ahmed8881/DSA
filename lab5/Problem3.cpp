#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    int target;
    
    cout << "Enter the integer to search for: ";
    cin >> target;
    
    bool found = false;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == target) {
            cout << "Integer found at index: " << i << endl;
            found = true;
            break;
        }
    }
    
    if (!found) {
        cout << "Integer not present in the vector." << endl;
    }
    
  
}