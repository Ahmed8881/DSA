#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <stdexcept>
using namespace std;

class Stack {
private:
    vector<int> data;

public:
    void push(int value) {
        data.push_back(value);
    }

    int pop() {
        if (isEmpty()) {
            throw runtime_error("Stack is empty.");
        }
        int value = data.back();
        data.pop_back();
        return value;
    }

    int top() const {
        if (isEmpty()) {
            throw runtime_error("Stack is empty.");
        }
        return data.back();
    }

    bool isEmpty() const {
        return data.empty();
    }

    string toString() const {
        if (data.empty()) return "Stack is empty.";
        
        stringstream ss;
        for (int i = data.size() - 1; i >= 0; --i) {
            ss << data[i] << " ";
        }
        return ss.str();
    }
};

void evaluatePostfix() {
    Stack stack;
    string input;

    cout << "Enter integers and operators (+, -, *, /, %) in postfix notation." << endl;
    cout << "Use '?' to print the stack, '^' to print the top element, and '!' to exit." << endl;
    

    while (true) {
        cout << "> ";
        getline(cin, input);
        stringstream ss(input);
        string token;

        if (input == "!") {
            cout << "Exiting..." << endl;
            break;
        }
        else if (input == "?") {
            cout << "Current stack: " << stack.toString() << endl;
            continue;
        }
        else if (input == "^") {
            if (!stack.isEmpty()) {
                cout << "Top element: " << stack.top() << endl;
            } else {
                cout << "Stack is empty." << endl;
            }
            continue;
        }

        while (ss >> token) {
            try {
                int num = stoi(token);
                stack.push(num);
            }
            catch (invalid_argument&) {
                if (token == "+" || token == "-" || token == "*" || token == "/" || token == "%") {
                    if (stack.isEmpty()) {
                        cout << "Insufficient operands in stack." << endl;
                        break;
                    }
                    int b = stack.pop();
                    if (stack.isEmpty()) {
                        cout << "Insufficient operands in stack." << endl;
                        stack.push(b); 
                        break;
                    }
                    int a = stack.pop();
                    int result;

                    if (token == "+") {
                        result = a + b;
                    } else if (token == "-") {
                        result = a - b;
                    } else if (token == "*") {
                        result = a * b;
                    } else if (token == "/") {
                        if (b == 0) {
                            cout << "Division by zero." << endl;
                            stack.push(a); 
                            stack.push(b); 
                            break;
                        }
                        result = a / b;
                    } else if (token == "%") {
                        result = a % b;
                    }

                    stack.push(result);
                } else {
                    cout << "Invalid input: " << token << endl;
                }
            }
        }
    }
}

int main() {
    evaluatePostfix();
    return 0;
}
