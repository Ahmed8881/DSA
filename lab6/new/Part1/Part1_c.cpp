#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;

    // Constructor
    Node(int x) {
        data = x;
        next = nullptr;
        prev = nullptr;
    }
};

// DoublyLinkedList class
class DoublyLinkedList {
public:
    // Constructor
    DoublyLinkedList() { head = nullptr; }

    // Destructor
    ~DoublyLinkedList() {
        while (!isEmpty()) {
            deleteFromStart();
        }
    }

    bool isEmpty() { return head == nullptr; }

    Node* insertAtHead(int x) {
        Node* newNode = new Node(x);
        if (head != nullptr) {
            head->prev = newNode;
        }
        newNode->next = head;
        head = newNode;
        return head;
    }

    Node* insertAtEnd(int x) {
        Node* newNode = new Node(x);
        if (isEmpty()) {
            head = newNode;
            return head;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
        return head;
    }

    bool deleteNode(int x) {
        Node* temp = head;
        while (temp != nullptr) {
            if (temp->data == x) {
                if (temp->prev != nullptr) {
                    temp->prev->next = temp->next;
                } else {
                    head = temp->next;
                }
                if (temp->next != nullptr) {
                    temp->next->prev = temp->prev;
                }
                delete temp;
                return true;
            }
            temp = temp->next;
        }
        return false;
    }

    bool deleteFromStart() {
        if (isEmpty()) return false;
        Node* temp = head;
        head = head->next;
        if (head != nullptr) {
            head->prev = nullptr;
        }
        delete temp;
        return true;
    }

    bool deleteFromEnd() {
        if (isEmpty()) return false;
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        if (temp->prev != nullptr) {
            temp->prev->next = nullptr;
        } else {
            head = nullptr;
        }
        delete temp;
        return true;
    }

    Node* reverseList() {
        Node* temp = nullptr;
        Node* current = head;
        while (current != nullptr) {
            temp = current->prev;
            current->prev = current->next;
            current->next = temp;
            current = current->prev;
        }
        if (temp != nullptr) {
            head = temp->prev;
        }
        return head;
    }

    void displayList() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

private:
    Node* head;
};

int main() {
    DoublyLinkedList list;
    list.insertAtHead(5);
    list.insertAtEnd(6);
    list.insertAtEnd(7);
    list.insertAtEnd(8);
    cout << "List: ";
    list.displayList();
      cout << "List after deleting 6: ";
    list.deleteNode(6);
    list.displayList();


    cout << "Reverse List: ";
    list.reverseList();
    list.displayList();

  
    return 0;
}
