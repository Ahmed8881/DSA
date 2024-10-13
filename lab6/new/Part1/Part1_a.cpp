#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class LinkList {
public:
    // Constructor
    LinkList() { head = NULL; }
    
    // Destructor
    ~LinkList() {
        while (!isEmpty()) {
            deleteFromStart();
        }
    }

    bool isEmpty() { return head == NULL; }

    Node* insertNode(int index, int x) {
        if (index < 0) return NULL;
        Node* newNode = new Node{x, nullptr};
        if (index == 0) {
            return insertAtHead(x);
        }
        Node* temp = head;
        for (int i = 0; temp != NULL && i < index - 1; i++) {
            temp = temp->next;
        }
        if (temp == NULL) return NULL;
        newNode->next = temp->next;
        temp->next = newNode;
        return head;
    }

    Node* insertAtHead(int x) {
        Node* newNode = new Node{x, head};
        head = newNode;
        return head;
    }

    Node* insertAtEnd(int x) {
        Node* newNode = new Node{x, nullptr};
        if (isEmpty()) {
            head = newNode;
            return head;
        }
        Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
        return head;
    }

    bool findNode(int x) {
        Node* temp = head;
        while (temp != NULL) {
            if (temp->data == x) return true;
            temp = temp->next;
        }
        return false;
    }

    bool deleteNode(int x) {
        bool deleted = false;
        while (head != NULL && head->data == x) {
            deleteFromStart();
            deleted = true;
        }
        Node* temp = head;
        while (temp != NULL && temp->next != NULL) {
            if (temp->next->data == x) {
                Node* toDelete = temp->next;
                temp->next = temp->next->next;
                delete toDelete;
                deleted = true;
            } else {
                temp = temp->next;
            }
        }
        return deleted;
    }

    bool deleteFromStart() {
        if (isEmpty()) return false;
        Node* temp = head;
        head = head->next;
        delete temp;
        return true;
    }

    bool deleteFromEnd() {
        if (isEmpty()) return false;
        if (head->next == NULL) {
            delete head;
            head = NULL;
            return true;
        }
        Node* temp = head;
        while (temp->next->next != NULL) {
            temp = temp->next;
        }
        delete temp->next;
        temp->next = NULL;
        return true;
    }

    void displayList() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data<<" ";
            temp = temp->next;
        }
        cout << endl;

       
    }

    Node* reverseList() {
        Node* prev = NULL;
        Node* curr = head;
        Node* next = NULL;
        while (curr != NULL) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
        return head;
    }

    Node* sortList(Node* list) {
        if (list == NULL || list->next == NULL) return list;
        bool swapped;
        Node* temp;
        do {
            swapped = false;
            temp = list;
            while (temp->next != NULL) {
                if (temp->data > temp->next->data) {
                    swap(temp->data, temp->next->data);
                    swapped = true;
                }
                temp = temp->next;
            }
        } while (swapped);
        return list;
    }

    Node* removeDuplicates(Node* list) {
        Node* temp = list;
        while (temp != NULL && temp->next != NULL) {
            if (temp->data == temp->next->data) {
                Node* toDelete = temp->next;
                temp->next = temp->next->next;
                delete toDelete;
            } else {
                temp = temp->next;
            }
        }
        return list;
    }

    Node* mergeLists(Node* list1, Node* list2) {
        Node* mergedHead = new Node{-1, NULL};
        Node* current = mergedHead;
        while (list1 != NULL && list2 != NULL) {
            if (list1->data < list2->data) {
                current->next = list1;
                list1 = list1->next;
            } else {
                current->next = list2;
                list2 = list2->next;
            }
            current = current->next;
        }
        current->next = (list1 != NULL) ? list1 : list2;
        Node* temp = mergedHead;
        mergedHead = mergedHead->next;
        delete temp;
        return mergedHead;
    }

    Node* interestLists(Node* list1, Node* list2) {
        Node* result = NULL;
        Node* last = NULL;
        Node* temp1 = list1;
        Node* temp2 = list2;

        while (temp1 != NULL && temp2 != NULL) {
            if (temp1->data == temp2->data) {
                Node* newNode = new Node{temp1->data, NULL};
                if (result == NULL) {
                    result = newNode;
                } else {
                    last->next = newNode;
                }
                last = newNode;
                temp1 = temp1->next;
                temp2 = temp2->next;
            } else if (temp1->data < temp2->data) {
                temp1 = temp1->next;
            } else {
                temp2 = temp2->next;
            }
        }
        return result;
    }

private:
    Node* head;
};

int main() {
    LinkList list;
    list.insertAtHead(1);
    list.insertAtEnd(2);
    list.insertAtEnd(3);
    list.insertAtEnd(0);
    cout << "List: ";
    list.displayList();
    cout<<"Reverse List: ";
    list.reverseList();
    list.displayList();
    cout<<"List after deleting 2: ";
    list.deleteNode(2);
    list.displayList();

    return 0;
}
