#include <vector>
#include <iostream>
#include <numeric>
using namespace std;

int main()
{
    string s;
    cin>>s;
    vector<int> count(26,0);
    for(int i=0;i<s.length();i++)
    {
        count[s[i]-'a'] = 1;
    }
    
    int UNIQUE = accumulate(count.begin(),count.end(),0);
    if(UNIQUE%2==0)
    {
        cout<<"CHAT WITH HER!";
    }
    else
    {
        cout<<"IGNORE HIM!";
    }
    return 0;
}