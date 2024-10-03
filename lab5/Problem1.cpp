#include<iostream>
#include<vector>
#include<string>
using namespace std;

void printOptions();

int main(){
    int choice=0;
    vector<string> strings;
    while(choice!=3){
    system("cls");

        printOptions();
        cin>>choice;
        if(choice==1){
            string str;
            cout<<"Enter a string: ";
            cin>>str;
            strings.push_back(str);
            cout << "String added." << endl;
        } else if(choice==2){
            if(!strings.empty()){
                strings.pop_back();
                cout<<"Last string removed."<<endl;
            } else {
                cout<<"No strings to remove."<<endl;
            }
        }
        cout << "Size: " << strings.size() << ", Capacity: " << strings.capacity() << endl;
        cout << "Press Enter to continue...";
        cin.ignore();
        cin.get();
    }
    
}
void printOptions(){
    cout<<"1-Add String"<<endl;
    cout<<"2-Remove String"<<endl;
    cout<<"3-Exit"<<endl;
    cout<<"Enter your choice: ";
}