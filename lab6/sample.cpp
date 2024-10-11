#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(NULL) {}
};

/**
 * @class LinkList
 * @brief A class to represent a singly linked list.
 * 
 * This class provides functionalities to manipulate a singly linked list,
 * including insertion, deletion, searching, reversing, sorting, and merging lists.
 * 
 * @note The class assumes the existence of a Node class which represents the elements of the list.
 */
class LinkList {
public:
    /**
     * @brief Constructs a new LinkList object.
     * 
     * Initializes the head of the list to NULL.
     */
    LinkList();

    /**
     * @brief Destroys the LinkList object.
     */
    ~LinkList();

    /**
     * @brief Checks if the list is empty.
     * 
     * @return true if the list is empty, false otherwise.
     */
    bool isEmpty();

    /**
     * @brief Inserts a node with value x at the given index.
     * 
     * @param index The position to insert the node.
     * @param x The value to insert.
     * @return A pointer to the newly inserted node.
     */
    Node* insertNode(int index, int x);

    /**
     * @brief Inserts a node with value x at the start of the list.
     * 
     * @param x The value to insert.
     * @return A pointer to the newly inserted node.
     */
    Node* insertAtHead(int x);

    /**
     * @brief Inserts a node with value x at the end of the list.
     * 
     * @param x The value to insert.
     * @return A pointer to the newly inserted node.
     */
    Node* insertAtEnd(int x);

    /**
     * @brief Searches for a node with value x in the list.
     * 
     * @param x The value to search for.
     * @return true if the value is found, false otherwise.
     */
    bool findNode(int x);

    /**
     * @brief Deletes all occurrences of nodes with value x.
     * 
     * @param x The value to delete.
     * @return true if the deletion was successful, false otherwise.
     */
    bool deleteNode(int x);

    /**
     * @brief Deletes the starting node of the list.
     * 
     * @return true if the deletion was successful, false otherwise.
     */
    bool deleteFromStart();

    /**
     * @brief Deletes the last node of the list.
     * 
     * @return true if the deletion was successful, false otherwise.
     */
    bool deleteFromEnd();

    /**
     * @brief Displays the contents of the list.
     */
    void displayList();

    /**
     * @brief Reverses the linked list.
     * 
     * @return A pointer to the new head of the reversed list.
     */
    Node* reverseList();

    /**
     * @brief Sorts the input list.
     * 
     * @param list A pointer to the list to be sorted.
     * @return A pointer to the head of the sorted list.
     */
    Node* sortList(Node *list);

    /**
     * @brief Removes duplicates from the input list.
     * 
     * @param list A pointer    LinkList() { head = NULL; } // constructor
    ~LinkList(); // destructor
    bool isEmpty() { return head == NULL; }
    Node* insertNode(int index, int x); // insert at the given index
    Node* insertAtHead(int x); // insert at start of list
    Node* insertAtEnd(int x); // insert at end of list
    bool findNode(int x); // search for data value x in the list
    bool deleteNode(int x); // delete all occurrences of x
    bool deleteFromStart(); // deletes starting node of list
    bool deleteFromEnd(); // deletes last node of list
    void displayList(void); 
    Node* reverseList(); // reverses the linklist and returns a new list
    Node* sortList(Node *list); // sorts the input-ed list
    Node* removeDuplicates(Node *list); // removes duplicates from list
    Node* mergeLists(Node *list1, Node *list2); // merges two lists
    Node* interestLists(Node *list1, Node *list2); // results contains intersection of two lists

private:
    Node* head;
};

LinkList::~LinkList() {
    Node* current = head;
    Node* next;
    while (current != NULL) {
        next = current->next;
        delete current;
        current = next;
    }
    head = NULL;
}

Node* LinkList::insertNode(int index, int x) {
    if (index < 0) return NULL;
    Node* newNode = new Node(x);
    if (index == 0) {
        newNode->next = head;
        head = newNode;
        return head;
    }
    Node* current = head;
    for (int i = 0; current != NULL && i < index - 1; ++i) {
        current = current->next;
    }
    if (current == NULL) return NULL;
    newNode->next = current->next;
    current->next = newNode;
    return head;
}

Node* LinkList::insertAtHead(int x) {
    Node* newNode = new Node(x);
    newNode->next = head;
    head = newNode;
    return head;
}

Node* LinkList::insertAtEnd(int x) {
    Node* newNode = new Node(x);
    if (head == NULL) {
        head = newNode;
        return head;
    }
    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

bool LinkList::findNode(int x) {
    Node* current = head;
    while (current != NULL) {
        if (current->data == x) return true;
        current = current->next;
    }
    return false;
}

bool LinkList::deleteNode(int x) {
    if (head == NULL) return false;
    Node* current = head;
    Node* prev = NULL;
    bool found = false;
    while (current != NULL) {
        if (current->data == x) {
            found = true;
            if (prev == NULL) {
                head = current->next;
            } else {
                prev->next = current->next;
            }
            Node* temp = current;
            current = current->next;
            delete temp;
        } else {
            prev = current;
            current = current->next;
        }
    }
    return found;
}

bool LinkList::deleteFromStart() {
    if (head == NULL) return false;
    Node* temp = head;
    head = head->next;
    delete temp;
    return true;
}

bool LinkList::deleteFromEnd() {
    if (head == NULL) return false;
    if (head->next == NULL) {
        delete head;
        head = NULL;
        return true;
    }
    Node* current = head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    delete current->next;
    current->next = NULL;
    return true;
}

void LinkList::displayList() {
    Node* current = head;
    while (current != NULL) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

Node* LinkList::reverseList() {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
    return head;
}

Node* LinkList::sortList(Node* list) {
    if (list == NULL || list->next == NULL) return list;
    Node* mid = list;
    Node* fast = list->next;
    while (fast != NULL && fast->next != NULL) {
        mid = mid->next;
        fast = fast->next->next;
    }
    Node* half = mid->next;
    mid->next = NULL;
    return mergeLists(sortList(list), sortList(half));
}

Node* LinkList::removeDuplicates(Node* list) {
    if (list == NULL) return NULL;
    Node* current = list;
    while (current->next != NULL) {
        if (current->data == current->next->data) {
            Node* temp = current->next;
            current->next = current->next->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
    return list;
}

Node* LinkList::mergeLists(Node* list1, Node* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;
    if (list1->data < list2->data) {
        list1->next = mergeLists(list1->next, list2);
        return list1;
    } else {
        list2->next = mergeLists(list1, list2->next);
        return list2;
    }
}

Node* LinkList::interestLists(Node* list1, Node* list2) {
    Node* result = NULL;
    Node** lastPtrRef = &result;
    while (list1 != NULL && list2 != NULL) {
        if (list1->data < list2->data) {
            list1 = list1->next;
        } else if (list1->data > list2->data) {
            list2 = list2->next;
        } else {
            Node* newNode = new Node(list1->data);
            *lastPtrRef = newNode;
            lastPtrRef = &(newNode->next);
            list1 = list1->next;
            list2 = list2->next;
        }
    }
    return result;
}