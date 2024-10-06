// #include <iostream>
// #include <vector>
// using namespace std;
// void displayMatrix(vector<vector<int>>& matrix);
// void addRow(vector<vector<int>>& matrix, vector<int>& row);
// void addColumn(vector<vector<int>>& matrix, vector<int>& column);
// vector<vector<int>> transposeMatrix(vector<vector<int>>& matrix);

// int main() {
//     vector<vector<int>> matrix = {{1, 2}, {3, 4}};
//     int choice=0;
//     while(choice<=5){
//         if(choice==1){}
//         if(choice==2){}
//         if(choice==3){}
//         if(choice==4){}
//         if(choice==1){}

//     }

//     cout << "Original Matrix:" << endl;
//     displayMatrix(matrix);

//     // Adding a new row to the matrix
//     vector<int> newRow = {5, 6};
//     addRow(matrix, newRow);
//     cout << "\nAfter adding a new row:" << endl;
//     displayMatrix(matrix);

//     // Adding a new column to the matrix
//     vector<int> newColumn = {7, 8, 9}; // Column has same number of elements as rows
//     addColumn(matrix, newColumn);
//     cout << "\nAfter adding a new column:" << endl;
//     displayMatrix(matrix);

//     // Transposing the matrix
//     vector<vector<int>> transposedMatrix = transposeMatrix(matrix);
//     cout << "\nTransposed Matrix:" << endl;
//     displayMatrix(transposedMatrix);

// }


// void printOption(){
//     cout<<"1-Add Row"<<endl;
//     cout<<"2-Add Column"<<endl;
//     cout<<"3-Display Matrix"<<endl;
//     cout<<"4-Transpose of Matrix"<<endl;
//     cout<<"5 Exit"<<endl;


// }
// // Function to display the matrix
// void displayMatrix(vector<vector<int>>& matrix) {
//     for (int i = 0; i < matrix.size(); i++) {
//         for (int j = 0; j < matrix[i].size(); j++) {
//             cout << matrix[i][j] << " ";
//         }
//         cout << endl;
//     }
// }

// // Function to add a row to the matrix
// void addRow(vector<vector<int>>& matrix, vector<int>& row) {
//     matrix.push_back(row);
// }

// // Function to add a column to the matrix
// void addColumn(vector<vector<int>>& matrix, vector<int>& column) {
//     for (int i = 0; i < matrix.size(); i++) {
//         matrix[i].push_back(column[i]);
//     }
// }

// // Function to transpose the matrix
// vector<vector<int>> transposeMatrix(vector<vector<int>>& matrix) {
//     vector<vector<int>> transposed;
//     int rows = matrix.size();
//     int cols = matrix[0].size();

//     // Initialize the transposed matrix with the number of columns as rows and rows as columns
//     for (int i = 0; i < cols; i++) {
//         vector<int> row;
//         for (int j = 0; j < rows; j++) {
//             row.push_back(0); // Initialize with zeros
//         }
//         transposed.push_back(row);
//     }

//     // Fill the transposed matrix
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             transposed[j][i] = matrix[i][j];
//         }
//     }

//     return transposed;
// }
