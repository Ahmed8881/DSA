#include <iostream>
#include <vector>
using namespace std;

void displayMatrix(vector<vector<int>>& matrix);
void addRow(vector<vector<int>>& matrix, vector<int>& row);
void addColumn(vector<vector<int>>& matrix, vector<int>& column);
vector<vector<int>> transposeMatrix(vector<vector<int>>& matrix);
void printOptions();

int main() {
    vector<vector<int>> matrix = {{1, 2}, {3, 4}};
    int choice = 0;
    
    while (choice <= 5) {
        printOptions();
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            // Adding a new row to the matrix
            int rowSize = matrix[0].size();
            vector<int> newRow(rowSize);
            cout << "Enter " << rowSize << " elements for the new row: ";
            for (int i = 0; i < rowSize; i++) {
                cin >> newRow[i];
            }
            addRow(matrix, newRow);
            cout << "\nAfter adding a new row:" << endl;
            displayMatrix(matrix);
        } 
        else if (choice == 2) {
            // Adding a new column to the matrix
            int colSize = matrix.size();
            vector<int> newColumn(colSize);
            cout << "Enter " << colSize << " elements for the new column: ";
            for (int i = 0; i < colSize; i++) {
                cin >> newColumn[i];
            }
            addColumn(matrix, newColumn);
            cout << "\nAfter adding a new column:" << endl;
            displayMatrix(matrix);
        } 
        else if (choice == 3) {
            cout << "\nCurrent Matrix:" << endl;
            displayMatrix(matrix);
        } 
        else if (choice == 4) {
            vector<vector<int>> transposedMatrix = transposeMatrix(matrix);
            cout << "\nTransposed Matrix:" << endl;
            displayMatrix(transposedMatrix);
        } 
        else if (choice == 5) {
                break;     
                   } 
        else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}

void displayMatrix(vector<vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void addRow(vector<vector<int>>& matrix, vector<int>& row) {
    matrix.push_back(row);
}

void addColumn(vector<vector<int>>& matrix, vector<int>& column) {
    for (int i = 0; i < matrix.size(); i++) {
        matrix[i].push_back(column[i]);
    }
}

vector<vector<int>> transposeMatrix(vector<vector<int>>& matrix) {
    vector<vector<int>> transposed;
    int rows = matrix.size();
    int cols = matrix[0].size();

    for (int i = 0; i < cols; i++) {
        vector<int> row;
        for (int j = 0; j < rows; j++) {
            row.push_back(0); 
        }
        transposed.push_back(row);
    }

    // Fill the transposed matrix
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}

// Function to display options
void printOptions() {
   
    cout << "1 - Add Row: "<<endl;
    cout << "2 - Add Column: "<<endl;
    cout << "3 - Display Matrix"<<endl;
    cout << "4 - Transpose of Matrix"<<endl;
    cout << "5 - Exit"<<endl;
}
