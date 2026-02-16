#include<iostream>
#include<unordered_map>
#include<vector>
#include<algorithm>

using namespace std;

class Solution{
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        unordered_map<string, vector<string>> sortedstrGroup;

        for(const auto& s: strs)
        {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            sortedstrGroup[sortedS].push_back(s);
        }

        vector<vector<string>> result;

        for(auto& pair:sortedstrGroup)
        {
            result.push_back(pair.second);
        }
        return result;
    }
};

int main()
{
    
    return 0;
}
