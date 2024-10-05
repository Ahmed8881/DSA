#include<iostream>
#include<vector>
using namespace std;
int printOption();

int main(){
    vector<int> integer={10, 20, 30, 40, 50};
    int option=printOption();
    while(option<=4){
        if(option==1){
         for (int i=integer.size(); i>=0;i--){
           for(int j=0;j<=integer.size();j++){
            int var=integer[j];
            integer[j]=integer[i];
            integer[i]=var;
           
        }
    }
    

        }
     
         

    }

    
}


int printOption(){
    cout<<"1-Reverse vetor"<<endl;
    cout<<"2-Sort In Acsending Order"<<endl;
    cout<<"3-Remove Duplicates"<<endl;
    cout<<"4-Exit"<<endl;
    int input;
    cin>>input;
    return input;

}