#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;
class Solution {
public: 
    bool hasDuplicate(vector<int>& nums)
    {
        if(nums.size() < 2)
            return false;

        sort(nums.begin(), nums.end());
        
        int index = 1;
        while(index < nums.size() && nums.size() >= 2)
        {
            if(nums[index] == nums[index-1])
            {
                return true;
            }
            index++;
        }
        return false;
    }
};

int main()
{
    vector<int> n = {12,12,34,33,56,67};
    Solution obj;
    bool result = obj.hasDuplicate(n);
    cout << result;
    return 0;
}