#include <iostream>
using namespace std;
void queueDriverCode();
void stackDriverCode();


// Stack implementation using array
class StackArray {
private:
    int top;
    int capacity;
    int* arr;

public:
    StackArray(int size) {
        capacity = size;
        arr = new int[size];
        top = -1;
    }

    void push(int x) {
        if (isFull()) {
            cout << "Stack Overflow"<<endl;
            return;
        }
        arr[++top] = x;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack Underflow"<<endl;
            return -1;
        }
        return arr[top--];
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty"<<endl;
            return -1;
        }
        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }

    bool isFull() {
        return top == capacity - 1;
    }
};
//Que using array
class QueueArray {
private:
    int front, rear, capacity;
    int* arr;

public:
    QueueArray(int size) {
        capacity = size;
        front = rear = -1;
        arr = new int[size];
    }

    // Add an item to the queue
    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue Overflow"<<endl;
            return;
        }
        if (isEmpty()) front = 0;
        arr[++rear] = x;
    }

    // Remove an item from the queue
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow"<<endl;
            return -1;
        }
        int data = arr[front];
        if (front == rear) {
            front = rear = -1; // Reset queue after last element
        } else {
            front++;
        }
        return data;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return arr[front];
    }

    bool isEmpty() {
        return front == -1;
    }

    bool isFull() {
        return rear == capacity - 1;
    }
};

void stackDriverCode() {
    int size, choice, value;
    cout << "Enter the size of the stack: ";
    cin >> size;

    StackArray stack(size);

    while (true) {
        cout << "\nChoose an operation for Stack:\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Peek\n";
        cout << "4. Check if Stack is Full\n";
        cout << "5. Check if Stack is Empty\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to push: ";
            cin >> value;
            stack.push(value);
        } else if (choice == 2) {
            value = stack.pop();
            if (value != -1)
                cout << "Popped: " << value << endl;
        } else if (choice == 3) {
            value = stack.peek();
            if (value != -1)
                cout << "Top of Stack: " << value << endl;
        } else if (choice == 4) {
            if (stack.isFull())
                cout << "Stack is Full\n";
            else
                cout << "Stack is not Full\n";
        } else if (choice == 5) {
            if (stack.isEmpty())
                cout << "Stack is Empty\n";
            else
                cout << "Stack is not Empty\n";
        } else if (choice == 6) {
            break;
        } else {
            cout << "Invalid choice!\n";
        }
    }
}

void queueDriverCode() {
    int size, choice, value;
    cout << "Enter the size of the queue: ";
    cin >> size;

    QueueArray queue(size);

    while (true) {
        cout << "\nChoose an operation for Queue:\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Peek\n";
        cout << "4. Check if Queue is Full\n";
        cout << "5. Check if Queue is Empty\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to enqueue: ";
            cin >> value;
            queue.enqueue(value);
        } else if (choice == 2) {
            value = queue.dequeue();
            if (value != -1)
                cout << "Dequeued: " << value << endl;
        } else if (choice == 3) {
            value = queue.peek();
            if (value != -1)
                cout << "Front of Queue: " << value << endl;
        } else if (choice == 4) {
            if (queue.isFull())
                cout << "Queue is Full\n";
            else
                cout << "Queue is not Full\n";
        } else if (choice == 5) {
            if (queue.isEmpty())
                cout << "Queue is Empty\n";
            else
                cout << "Queue is not Empty\n";
        } else if (choice == 6) {

            break;
        } else {
            cout << "Invalid choice!\n";
        }
    }
}

int main() {
    int choice;
    cout << "Choose a data structure to test:\n";
    cout << "1. Stack\n";
    cout << "2. Queue\n";
    cout << "Enter your choice: ";
    cin >> choice;

    if (choice == 1) {
        stackDriverCode();
    } else if (choice == 2) {
        queueDriverCode();
    } else {
        cout << "Invalid choice!\n";
    }

    return 0;
}
