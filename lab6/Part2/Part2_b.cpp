#include <iostream>
#include <stack>
#include <sstream>
#include <string>

class Stack {
private:
    std::stack<int> stack;

public:
    void push(int value) {
        stack.push(value);
    }

    int pop() {
        if (stack.empty()) {
            throw std::runtime_error("Stack is empty");
        }
        int value = stack.top();
        stack.pop();
        return value;
    }

    std::string toString() {
        std::stack<int> temp = stack;
        std::string result;
        while (!temp.empty()) {
            result += std::to_string(temp.top()) + " ";
            temp.pop();
        }
        return result;
    }

    bool isEmpty() {
        return stack.empty();
    }
};

void printHelp() {
    std::cout << "Commands:\n";
    std::cout << "  + : Add top two elements\n";
    std::cout << "  - : Subtract top two elements\n";
    std::cout << "  * : Multiply top two elements\n";
    std::cout << "  / : Divide top two elements\n";
    std::cout << "  % : Modulus of top two elements\n";
    std::cout << "  ? : Print stack\n";
    std::cout << "  ^ : Pop and print top element\n";
    std::cout << "  ! : Exit\n";
    std::cout << "  <number> : Push number onto stack\n";
}

int main() {
    Stack stack;
    std::string input;

    printHelp();

    while (true) {
        std::cout << "Enter command: ";
        std::getline(std::cin, input);
        std::istringstream iss(input);
        std::string token;

        while (iss >> token) {
            if (token == "+") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                int b = stack.pop();
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    stack.push(b);
                    continue;
                }
                int a = stack.pop();
                stack.push(a + b);
            } else if (token == "-") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                int b = stack.pop();
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    stack.push(b);
                    continue;
                }
                int a = stack.pop();
                stack.push(a - b);
            } else if (token == "*") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                int b = stack.pop();
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    stack.push(b);
                    continue;
                }
                int a = stack.pop();
                stack.push(a * b);
            } else if (token == "/") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                int b = stack.pop();
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    stack.push(b);
                    continue;
                }
                int a = stack.pop();
                if (b == 0) {
                    std::cerr << "Division by zero error" << std::endl;
                    stack.push(a);
                    stack.push(b);
                    continue;
                }
                stack.push(a / b);
            } else if (token == "%") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                int b = stack.pop();
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    stack.push(b);
                    continue;
                }
                int a = stack.pop();
                stack.push(a % b);
            } else if (token == "?") {
                std::cout << stack.toString() << std::endl;
            } else if (token == "^") {
                if (stack.isEmpty()) {
                    std::cerr << "Stack is empty" << std::endl;
                    continue;
                }
                std::cout << stack.pop() << std::endl;
            } else if (token == "!") {
                return 0;
            } else {
                try {
                    int value = std::stoi(token);
                    stack.push(value);
                } catch (std::invalid_argument&) {
                    std::cerr << "Invalid input" << std::endl;
                }
            }
        }
    }

    return 0;
}