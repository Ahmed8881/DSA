#include <iostream>
using namespace std;

class MyStack {
private:
    struct Node {
        string data;
        Node* next;
        Node(const string& data) : data(data), next(nullptr) {}
    };
    Node* topNode;

public:
    MyStack() : topNode(nullptr) {}

    ~MyStack() {
        while (!isEmpty()) {
            pop();
        }
    }

    void push(const string& data) {
        Node* newNode = new Node(data);
        newNode->next = topNode;
        topNode = newNode;
    }

    void pop() {
        if (isEmpty()) return;
        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
    }

    string top() const {
        if (isEmpty()) return "";
        return topNode->data;
    }

    bool isEmpty() const {
        return topNode == nullptr;
    }
};

void reverseWordsInSentence(const string& sentence) {
    MyStack wordStack; 
    string tempWord;   

 
    for (char ch : sentence) {
        if (ch != ' ') { 
            tempWord += ch; 
        } else {
            if (!tempWord.empty()) { 
                wordStack.push(tempWord); 
                tempWord.clear();
            }
        }
    }

    if (!tempWord.empty()) {
        wordStack.push(tempWord);
    }

    while (!wordStack.isEmpty()) {
        cout << wordStack.top(); 
        wordStack.pop(); 
        if (!wordStack.isEmpty()) {
            cout << " ";
            }
    }
    cout << endl; 
}

int main() {
    string sentence = "I am from University of Engineering and Technology Lahore";
    cout << "Original Sentence: " << sentence << endl;
    cout << "Reversed Sentence: ";
    reverseWordsInSentence(sentence);
    return 0;
}
