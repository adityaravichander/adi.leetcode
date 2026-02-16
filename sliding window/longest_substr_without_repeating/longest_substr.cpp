#include<iostream>
#include<vector>
#include<unordered_set>
#include<string>
using namespace std;

class Solution 
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> charSet;
        int l = 0;
        int res = 0;

        for(int r = 0; r < s.size(); r++)
        {
            while(charSet.find(s[r]) != charSet.end())
            {
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(s[r]);
            res = max(res, r - l + 1);
        }
        return res;
    }
};

int main()
{
    string s = "zxyzxyz";
    Solution obj;
    int result = obj.lengthOfLongestSubstring(s);
    cout << result;
    
    return 0;
}