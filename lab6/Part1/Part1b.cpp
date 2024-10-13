#include <iostream>

// Stack using array
class StackArray {
private:
    int top;
    int maxSize;
    int* stackArray;

public:
    StackArray(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    ~StackArray() {
        delete[] stackArray;
    }

    void push(int value) {
        if (top >= maxSize - 1) {
            std::cout << "Stack Overflow\n";
            return;
        }
        stackArray[++top] = value;
    }

    int pop() {
        if (top < 0) {
            std::cout << "Stack Underflow\n";
            return -1;
        }
        return stackArray[top--];
    }

    bool isEmpty() {
        return top < 0;
    }
};

// Queue using array
class QueueArray {
private:
    int front, rear, maxSize;
    int* queueArray;

public:
    QueueArray(int size) {
        maxSize = size;
        queueArray = new int[maxSize];
        front = rear = -1;
    }

    ~QueueArray() {
        delete[] queueArray;
    }

    void enqueue(int value) {
        if (rear >= maxSize - 1) {
            std::cout << "Queue Overflow\n";
            return;
        }
        if (front == -1) front = 0;
        queueArray[++rear] = value;
    }

    int dequeue() {
        if (front == -1 || front > rear) {
            std::cout << "Queue Underflow\n";
            return -1;
        }
        return queueArray[front++];
    }

    bool isEmpty() {
        return front == -1 || front > rear;
    }
};

// Node structure for linked list
struct Node {
    int data;
    Node* next;
};

// Stack using linked list
class StackLinkedList {
private:
    Node* top;

public:
    StackLinkedList() {
        top = nullptr;
    }

    void push(int value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (top == nullptr) {
            std::cout << "Stack Underflow\n";
            return -1;
        }
        int value = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return value;
    }

    bool isEmpty() {
        return top == nullptr;
    }
};

// Queue using linked list
class QueueLinkedList {
private:
    Node* front;
    Node* rear;

public:
    QueueLinkedList() {
        front = rear = nullptr;
    }

    void enqueue(int value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = nullptr;
        if (rear == nullptr) {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }

    int dequeue() {
        if (front == nullptr) {
            std::cout << "Queue Underflow\n";
            return -1;
        }
        int value = front->data;
        Node* temp = front;
        front = front->next;
        if (front == nullptr) rear = nullptr;
        delete temp;
        return value;
    }

    bool isEmpty() {
        return front == nullptr;
    }
};

int main() {
    // Example usage of Stack and Queue with arrays
    StackArray stackArray(5);
    stackArray.push(1);
    stackArray.push(2);
    std::cout << "Popped from stackArray: " << stackArray.pop() << "\n";

    QueueArray queueArray(5);
    queueArray.enqueue(1);
    queueArray.enqueue(2);
    std::cout << "Dequeued from queueArray: " << queueArray.dequeue() << "\n";

    // Example usage of Stack and Queue with linked lists
    StackLinkedList stackLinkedList;
    stackLinkedList.push(1);
    stackLinkedList.push(2);
    std::cout << "Popped from stackLinkedList: " << stackLinkedList.pop() << "\n";

    QueueLinkedList queueLinkedList;
    queueLinkedList.enqueue(1);
    queueLinkedList.enqueue(2);
    std::cout << "Dequeued from queueLinkedList: " << queueLinkedList.dequeue() << "\n";

    return 0;
}