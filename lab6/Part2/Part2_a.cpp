#include <iostream>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

void reverseWords(const string &sentence) {
    stack<string> wordStack;
    stringstream ss(sentence);
    string word;

    while (ss >> word) {
        wordStack.push(word);
    }

    // Print reversed words
    while (!wordStack.empty()) {
        cout << wordStack.top() << " ";
        wordStack.pop();
    }
}

int main() {
    string sentence = "I am from University of Engineering and Technology Lahore";
    reverseWords(sentence);
    return 0;
}
