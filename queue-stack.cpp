#include <iostream>

using namespace std;

class Stack
{
private:
    int arr[100];
    int top;

public:
    Stack()
    {
        top = 0;
    }

    void push(int x)
    {
        if (top == 100)
        {
            cout << "Stack đầy\n";
            return;
        }
        top++;
        arr[top] = x;
        return;
    }

    void pop()
    {
        if (top == 0)
        {
            cout << "Stack rỗng\n";
            return;
        }
        arr[top] = 0;
        top--;
        return;
    }

    void printStack()
    {
        if (top == 0)
        {
            cout << "Stack rỗng\n";
            return;
        }
        for (int i = 1; i <= top; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
        return;
    }
};

class Queue
{
private:
    int arr[100];
    int head;
    int tail;

public:
    Queue()
    {
        head = tail = 0;
    }

    void push(int x)
    {
        if (tail == 100)
        {
            cout << "Queue đầy\n";
            return;
        }
        tail++;
        arr[tail] = x;
        return;
    }

    void pop()
    {
        if (head == tail)
        {
            cout << "Queue rỗng\n";
            return;
        }
        head++;
        arr[head] = 0;
        return;
    }

    void printQueue()
    {
        if (head == tail)
        {
            cout << "Queue rỗng";
            return;
        }
        for (int i = head + 1; i <= tail; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
        return;
    }
};

int main()
{
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(10);
    stack.push(7);
    stack.push(6);
    stack.pop();
    stack.printStack(); // 1 2 10 7

    Queue queue;
    queue.push(1);
    queue.push(2);
    queue.push(10);
    queue.push(7);
    queue.push(6);
    queue.pop();
    queue.printQueue(); // 2 10 7 6

    return 0;
}