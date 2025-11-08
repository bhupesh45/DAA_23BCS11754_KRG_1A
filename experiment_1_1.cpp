#include <iostream>
using namespace std;

#define MAX 5  

class Stack {
    int arr[MAX];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(int data) {
        if (isFull()) {
            cout << "Stack Overflow! Cannot push " << data << endl;
            return;
        }
        arr[++top] = data;
        cout << data << " pushed into stack." << endl;
    }

    void pop() {
        if (isEmpty()) {
            cout << "Stack Underflow! Cannot pop." << endl;
            return;
        }
        cout << arr[top--] << " popped from stack." << endl;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty, no top element!" << endl;
            return -1;
        }
        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }

    bool isFull() {
        return top == MAX - 1;
    }
};

int main() {
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);
    cout << "Top element is: " << s.peek() << endl;

    s.pop();
    s.pop();
    s.pop();
    s.pop(); 

    cout << (s.isEmpty() ? "Stack is empty" : "Stack is not empty") << endl;

    return 0;
}
