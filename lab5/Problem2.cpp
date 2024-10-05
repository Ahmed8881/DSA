#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> integers;
    for (int i=0; i<100;i++){
        integers.push_back(i);
        cout << "Size: " << integers.size() << ", Capacity: " << integers.capacity() << endl;

    }

}