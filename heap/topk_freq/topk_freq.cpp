#include<iostream>
#include<vector>
#include<algorithm>
#include <queue>
#include<unordered_map>
using namespace std;

class Solution{

public:
    vector<int> topkFrequent(vector<int> n, int k)
    {

        unordered_map<int,int> itemFreq;
        for (int i = 0; i < n.size(); i++)
        {
            itemFreq[n[i]]+=1;
        }

        using Element = pair<int, int>;
        priority_queue<Element, vector<Element>, greater<Element>> minHeap;

        for (const auto& pair: itemFreq)
        {
            minHeap.push({pair.second, pair.first});
            if(minHeap.size() > k)
                minHeap.pop();
        }

        while(!minHeap.empty())
        {
            cout << minHeap.top().second << ":" << minHeap.top().first << endl;
            minHeap.pop();
        }

    }
};

int main()
{
    vector<int> nums = {1,2,2,3,3,3};
    int m = 2;
    Solution obj;
    vector<int> result = obj.topkFrequent(nums, m);
    cout << "[";
    for(int i = 0; i < result.size(); i++)
    {
        cout << result[i] << ", ";
    }
    cout << "]";

    return 0;
}
