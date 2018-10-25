#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

int prec(char c)
{
    if(c=='^') return 3;
    else if(c== '*' or c=='/') return 2;
    else if(c=='+' or c=='-') return 1;
    else return -1;
}

string InfixToPostfix(string str)
{
    std::stack <char> s;
    string ns;
    int l= str.length();
    for(int i=0; i<l; i++)
    {
        if((str[i]>='a' and str[i]<='z') or (str[i]>= 'A' and str[i]<='Z'))
            ns+= str[i];
        else if(str[i]=='(')
            s.push('(');
        else if(str[i]==')')
        {
            while(s.top()!='(' && !s.empty())
            {
                ns+= s.top();
                s.pop();
            }
            if(s.top()=='(') s.pop();
        }
        else
        {
            while(!s.empty() && prec(str[i])<= prec(s.top()))
            {
                ns+= s.top();
                s.pop();
            }
            s.push(str[i]);
        }
    }
    while(!s.empty())
    {
        ns+= s.top();
       s.pop();
    }
    return ns;
}
int main() {
    string str, str2;
    cin>>str;
    str2= InfixToPostfix(str);
    cout<<str2;
    return 0;
}