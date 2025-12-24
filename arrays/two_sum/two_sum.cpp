#include <iostream>
#include <vector>
#include <unordered_map>
#include <limits>
using namespace std;

class Solution {
public: 
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int,int> valueIndex;

        for(int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            if(valueIndex.count(diff) && valueIndex[diff] != i)
                return {min(i, valueIndex[diff]), max(i, valueIndex[diff])};
            else
                valueIndex[nums[i]] = i;
        }

    }
};

int main()
{
    cout << "Starting Two_Sum Solution" << endl;
    int target;
    int input;

    vector<int> n = {};
    cout << "Enter numbers (ctrl+D to quit):" << endl;
    while (std::cin >> input && input != -1) {
        n.push_back(input);
    }
    cin.clear(); 
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "You entered " << n.size() << " numbers." << endl;
    cout << "Type integer target: ";
    cin >> target;
    cout << "Integer Target is: "  << target << endl;

    Solution obj;
    vector<int> result = obj.twoSum(n, target);
    
    if(result.size() == 2)
    {
        cout << "Result: Solution Exists as follows \n";
        cout << "Indices: [" << result[0] << ", " << result[1] << "] \n";
        cout << "Values: [" << n[result[0]] << ", " << n[result[1]] << "] \n";
    }
    else    
        cout << "Result: No solution exists. \n";

    return 0;

}

