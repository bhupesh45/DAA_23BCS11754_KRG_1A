#include <iostream>
using namespace std;

class DoublyNode {
public:
    int data;
    DoublyNode* prev;
    DoublyNode* next;
    DoublyNode(int val) {
        data = val;
        prev = next = NULL;
    }
};

class DoublyLinkedList {
    DoublyNode* head;
public:
    DoublyLinkedList() { head = NULL; }

    void insertAtBegin(int val) {
        DoublyNode* n = new DoublyNode(val);
        if (!head) {
            head = n;
            return;
        }
        n->next = head;
        head->prev = n;
        head = n;
    }

    void insertAtEnd(int val) {
        DoublyNode* n = new DoublyNode(val);
        if (!head) {
            head = n;
            return;
        }
        DoublyNode* temp = head;
        while (temp->next) temp = temp->next;
        temp->next = n;
        n->prev = temp;
    }

    void deleteAtBegin() {
        if (!head) return;
        DoublyNode* temp = head;
        head = head->next;
        if (head) head->prev = NULL;
        delete temp;
    }

    void deleteAtEnd() {
        if (!head) return;
        if (!head->next) {
            delete head;
            head = NULL;
            return;
        }
        DoublyNode* temp = head;
        while (temp->next) temp = temp->next;
        temp->prev->next = NULL;
        delete temp;
    }

    void display() {
        DoublyNode* temp = head;
        while (temp) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};


class CircularLinkedList {
    struct Node {
        int data;
        Node* next;
        Node(int val) { data = val; next = NULL; }
    };
    Node* head;
    Node* tail;

public:
    CircularLinkedList() { head = tail = NULL; }

    void insertAtBegin(int val) {
        Node* n = new Node(val);
        if (!head) {
            head = tail = n;
            tail->next = head;
            return;
        }
        n->next = head;
        head = n;
        tail->next = head;
    }

    void insertAtEnd(int val) {
        Node* n = new Node(val);
        if (!head) {
            head = tail = n;
            tail->next = head;
            return;
        }
        tail->next = n;
        n->next = head;
        tail = n;
    }

    void deleteAtBegin() {
        if (!head) return;
        if (head == tail) {
            delete head;
            head = tail = NULL;
            return;
        }
        Node* temp = head;
        head = head->next;
        tail->next = head;
        delete temp;
    }

    void deleteAtEnd() {
        if (!head) return;
        if (head == tail) {
            delete head;
            head = tail = NULL;
            return;
        }
        Node* temp = head;
        while (temp->next != tail) temp = temp->next;
        temp->next = head;
        delete tail;
        tail = temp;
    }

    void display() {
        if (!head) return;
        Node* temp = head;
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != head);
        cout << endl;
    }
};

int main() {
    cout << "Doubly Linked List Operations:" << endl;
    DoublyLinkedList dll;
    dll.insertAtBegin(10);
    dll.insertAtEnd(20);
    dll.insertAtEnd(30);
    dll.display();
    dll.deleteAtBegin();
    dll.display();
    dll.deleteAtEnd();
    dll.display();

    cout << "\nCircular Linked List Operations:" << endl;
    CircularLinkedList cll;
    cll.insertAtBegin(1);
    cll.insertAtEnd(2);
    cll.insertAtEnd(3);
    cll.display();
    cll.deleteAtBegin();
    cll.display();
    cll.deleteAtEnd();
    cll.display();

    return 0;
}
