#include <iostream>
#include <vector>

using namespace std;
void removeDuplicates(vector<int>& vec);
void reverseVector(vector<int>& vec);
void sortVector(vector<int>& vec);
void printOption();
void printVector(vector<int>& vec);
int main() {

   
    vector<int> vec = {10, 20, 30, 40, 50,50,30,90};
    int option=0;
    while(option<=4){
        printOption();
        cin>>option;
        if(option==1){
            reverseVector(vec);
            printVector(vec);

        }
        if(option==2){
             sortVector(vec);
            printVector(vec);

        }
        if(option==3){
            removeDuplicates(vec);
            printVector(vec);


        }
        if(option==4){
            break;
        }

    }  

}
void printVector(vector<int>& vec){
      cout << "Vector: ";
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;
}

void reverseVector(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n / 2; i++) {
        int var = vec[i];
        vec[i] = vec[n - i - 1];
        vec[n - i - 1] = var;
    }
}

void sortVector(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (vec[i] > vec[j]) {
                int temp = vec[i];
                vec[i] = vec[j];
                vec[j] = temp;
            }
        }
    }
}

void removeDuplicates(vector<int>& vec) {
    int n = vec.size();
    vector<int> result;
    for (int i = 0; i < n; i++) {
        bool ContainDuplicate = false;
        for (int j = 0; j < result.size(); j++) {
            if (vec[i] == result[j]) {
                ContainDuplicate = true;
                break;
            }
        }
        if (!ContainDuplicate) {
            result.push_back(vec[i]);
        }
    }
    vec = result;
}
void printOption(){
    cout<<"1-Reverse vetor"<<endl;
    cout<<"2-Sort In Acsending Order"<<endl;
    cout<<"3-Remove Duplicates"<<endl;
    cout<<"4-Exit"<<endl;
  

}