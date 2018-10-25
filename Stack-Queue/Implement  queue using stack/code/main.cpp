#include <iostream>
#include <stack>

using namespace std;

class Queue{
    private:
        stack <int> s1, s2;
    public:
        void enqueue(int data)
        {
            s1.push(data);
        }
        void dequeue(){
            if(s1.empty() and s2.empty())
            {
                cout<<"not possible\n";
            }
            if(s2.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            while(!s2.empty()) {
                s1.push(s2.top());
                s2.pop();
            }
        }
        void front(){
            if (s2.empty()){
                while(!s1.empty()){
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            if(!s2.empty()){
                cout << "top :" << s2.top() << endl;
            }else{
                cout << "Underflow "<< endl;
            }
        }
    bool isEmpty(){
        if(s1.empty() && s2.empty()){
            cout << "Empty "<< endl;
            return true;
        }
        cout << "Not Empty "<< endl;
        return false;
    }

    // Size
    int size(){
        int s = s1.size() + s2.size();
        cout << "size :" << s << endl;
        return s;
    }
};

// Time complexity:
// Enqueue: O(1)
// Dequeue: O(1)
// front:O(1)
// size: o(1);
// empty:  o(1);

int main() {
    Queue q;
    q.enqueue(5);
    q.enqueue(4);
    q.enqueue(3);
    q.dequeue();
    q.front();
    q.size();
    q.enqueue(10);
    q.front();
    q.dequeue();
    q.dequeue();
    q.dequeue();
    q.dequeue();
    q.size();
    //std::cout << "Hello, World!" << std::endl;
    return 0;
}