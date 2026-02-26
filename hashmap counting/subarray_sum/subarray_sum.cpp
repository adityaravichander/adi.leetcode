#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k)
    {

        /* brute force solution
        int res = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            int sum = 0;
            for(int j = 0; j < nums.size(); j++)
            {
                sum += nums[j];
                if(sum == k)
                    res++;
            }
        }
        return res;
        */

        // hashmap
        int res = 0;
        int curSum = 0;
        unordered_map<int,int> prefixSums;
        prefixSums[0] = 1;

        for (int num : nums)
        {
            curSum += num;
            int diff = curSum - k;
            res += prefixSums[diff];
            prefixSums[curSum]++;
        }

        return res;

    }

};

int main()
{
    vector<int> n = {2,-1,1,2};
    int a = 2;
    Solution obj;
    int result = obj.subarraySum(n, a);
    return 0;
}