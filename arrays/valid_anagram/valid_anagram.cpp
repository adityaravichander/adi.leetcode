#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

class Solution{
public:
    bool isAnagram(string s, string t)
    {
        if(s.length()!= t.length())
        {
            return false;
        }

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};

int main()
{
    string p = "abcd";
    string q = "cdba";
    Solution obj;
    bool result = obj.isAnagram(p,q);
    cout << result;
    return 0;
}