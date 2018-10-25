#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

int eval_postfix(char exp[])
{
    int ans=0;
    stack<int> s;
    for(int i=0; exp[i]; i++)
    {
        if(isdigit(exp[i]))
        {
            s.push(exp[i]-'0');
        }
        else
        {
            int op2= s.top(); s.pop();
            int op1= s.top(); s.pop();
            if(exp[i]=='*') s.push(op2*op1);
            else if(exp[i]=='/') s.push(op1/op2);
            else if(exp[i]=='+') s.push(op2+op1);
            else if(exp[i]=='-') s.push(op1-op2);
        }
    }
    return s.top();
}

int main() {
    char exp[100];
    cin>>exp;
    int ans= eval_postfix(exp);
    cout<<ans;
    return 0;
}