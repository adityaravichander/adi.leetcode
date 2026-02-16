#include<vector>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

class Solution{
public:

    int minEatingSpeed(vector<int>& piles, int h)
    {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        int minRate = r;

        while(l <= r)
        {
            int k = (l+r)/2;
            long long totalTime = 0;
            for(int p : piles)
                totalTime += ceil(static_cast<double>(p) / k);

            if(totalTime <= h)
            {
                minRate = k;
                r = k - 1;
            }
            else
                l = k + 1;
        }

        return minRate;
    }

};

int main()
{
    vector<int> piles = {1,4,3,2};
    int hours = 9;
    Solution obj;
    int minK = obj.minEatingSpeed(piles, hours);
    cout << "minK = " << minK;
    return 0;
}