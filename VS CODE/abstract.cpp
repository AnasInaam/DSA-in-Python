#include <iostream>
#include<vector>
using namespace std;


class A
{
    public:
    virtual void func() = 0;
    void msg(){
        cout<<"This is end";
    }
};

class B : public A
{
public:
    void fun(){
        cout << "This the Begining" << endl;
    }
    void func() override {
        cout << "Implementation of pure virtual function func()" << endl;
    }
};

int main()
{
    B b;
    vector<int> arr;
    vector<vector<int>> arr2;
    b.fun();
    b.func();
    b.msg(); // This will call the msg function from class A
    return 0;
}