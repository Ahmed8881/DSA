#include <iostream>

template <typename T>
class Node {
public:
    T data;
    Node* next;
    Node(T val) : data(val), next(NULL) {}
};

template <typename T>
class LinkedList {
public:
    LinkedList() : head(NULL) {}
    ~LinkedList();
    bool isEmpty() const { return head == NULL; }
    Node<T>* insertNode(int index, T x);
    Node<T>* insertAtHead(T x);
    Node<T>* insertAtEnd(T x);
    bool findNode(T x) const;
    bool deleteNode(T x);
    bool deleteFromStart();
    bool deleteFromEnd();
    void displayList() const;
    Node<T>* reverseList();
    Node<T>* sortList(Node<T>* list);
    Node<T>* removeDuplicates(Node<T>* list);
    Node<T>* mergeLists(Node<T>* list1, Node<T>* list2);
    Node<T>* interestLists(Node<T>* list1, Node<T>* list2);
    Node<T>* getHead() const { return head; }

private:
    Node<T>* head;
};

template <typename T>
LinkedList<T>::~LinkedList() {
    Node<T>* current = head;
    Node<T>* next;
    while (current != NULL) {
        next = current->next;
        delete current;
        current = next;
    }
    head = NULL;
}

template <typename T>
Node<T>* LinkedList<T>::insertNode(int index, T x) {
    if (index < 0) return NULL;
    Node<T>* newNode = new Node<T>(x);
    if (index == 0) {
        newNode->next = head;
        head = newNode;
        return head;
    }
    Node<T>* current = head;
    for (int i = 0; current != NULL && i < index - 1; ++i) {
        current = current->next;
    }
    if (current == NULL) return NULL;
    newNode->next = current->next;
    current->next = newNode;
    return head;
}

template <typename T>
Node<T>* LinkedList<T>::insertAtHead(T x) {
    Node<T>* newNode = new Node<T>(x);
    newNode->next = head;
    head = newNode;
    return head;
}

template <typename T>
Node<T>* LinkedList<T>::insertAtEnd(T x) {
    Node<T>* newNode = new Node<T>(x);
    if (head == NULL) {
        head = newNode;
        return head;
    }
    Node<T>* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

template <typename T>
bool LinkedList<T>::findNode(T x) const {
    Node<T>* current = head;
    while (current != NULL) {
        if (current->data == x) {
            return true;
        }
        current = current->next;
    }
    return false;
}

template <typename T>
bool LinkedList<T>::deleteNode(T x) {
    Node<T>* current = head;
    if (current->data == x) {
        head = current->next;
        delete current;
        return true;
    }
    while (current->next != NULL) {
        if (current->next->data == x) {
            Node<T>* temp = current->next;
            current->next = current->next->next;
            delete temp;
            return true;
        }
        current = current->next;
    }
    return false;
}

template <typename T>
bool LinkedList<T>::deleteFromStart() {
    if (head == NULL) return false;
    Node<T>* temp = head;
    head = head->next;
    delete temp;
    return true;
}

template <typename T>
bool LinkedList<T>::deleteFromEnd() {
    if (head == NULL) return false;
    if (head->next == NULL) {
        delete head;
        head = NULL;
        return true;
    }
    Node<T>* current = head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    delete current->next;
    current->next = NULL;
    return true;
}

template <typename T>
void LinkedList<T>::displayList() const {
    Node<T>* current = head;
    while (current != NULL) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

template <typename T>
Node<T>* LinkedList<T>::reverseList() {
    Node<T>* prev = NULL;
    Node<T>* current = head;
    Node<T>* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
    return head;
}

template <typename T>
Node<T>* LinkedList<T>::sortList(Node<T>* list) {
    if (list == NULL || list->next == NULL) return list;
    Node<T>* mid = list;
    Node<T>* fast = list->next;
    while (fast != NULL && fast->next != NULL) {
        mid = mid->next;
        fast = fast->next->next;
    }
    Node<T>* half = mid->next;
    mid->next = NULL;
    return mergeLists(sortList(list), sortList(half));
}

template <typename T>
Node<T>* LinkedList<T>::removeDuplicates(Node<T>* list) {
    if (list == NULL) return list;
    Node<T>* current = list;
    while (current->next != NULL) {
        if (current->data == current->next->data) {
            Node<T>* temp = current->next;
            current->next = current->next->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
    return list;
}

template <typename T>
Node<T>* LinkedList<T>::mergeLists(Node<T>* list1, Node<T>* list2) {
    Node<T>* dummy = new Node<T>(0);
    Node<T>* current = dummy;
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
    if (list1 != NULL) {
        current->next = list1;
    } else {
        current->next = list2;
    }
    Node<T>* result = dummy->next;
    delete dummy;
    return result;
}

template <typename T>
Node<T>* LinkedList<T>::interestLists(Node<T>* list1, Node<T>* list2) {
    Node<T>* dummy = new Node<T>(0);
    Node<T>* current = dummy;
    while (list1 != NULL && list2 != NULL) {
        if (list1->data == list2->data) {
            current->next = list1;
            list1 = list1->next;
            list2 = list2->next;
            current = current->next;
        } else if (list1->data < list2->data) {
            list1 = list1->next;
        } else {
            list2 = list2->next;
        }
    }
    Node<T>* result = dummy->next;
    delete dummy;
    return result;
}

int main() {
    LinkedList<int> list;
    list.insertAtEnd(1);
    list.insertAtEnd(2);
    list.insertAtEnd(3);
    list.insertAtEnd(4);
    list.insertAtEnd(5);
    list.insertAtEnd(6);
    list.insertAtEnd(7);
    list.insertAtEnd(8);
    list.insertAtEnd(9);
    list.insertAtEnd(10);
    list.displayList();
    list.reverseList();
    list.displayList();
    list.sortList(list.getHead());
    list.displayList();
    list.removeDuplicates(list.getHead());
    list.displayList();
    LinkedList<int> list1;
    list1.insertAtEnd(1);
    list1.insertAtEnd(3);
    list1.insertAtEnd(5);
    list1.insertAtEnd(7);
    list1.insertAtEnd(9);
    LinkedList<int> list2;
    list2.insertAtEnd(2);
    list2.insertAtEnd(3);
    list2.insertAtEnd(5);
    list2.insertAtEnd(9);
    Node<int>* intersection = list.interestLists(list1.getHead(), list2.getHead());
    while (intersection != NULL) {
        std::cout << intersection->data << " ";
        intersection = intersection->next;
    }
    std::cout << std::endl;
    return 0;
}