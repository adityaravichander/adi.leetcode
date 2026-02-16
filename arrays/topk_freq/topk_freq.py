from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topkFrequent(self, nums: List[int], k:int) -> List[int]:

        itemFreq = defaultdict(int)

        for n in nums:
            itemFreq[n]+=1
        
        heap = []

        for item, freq in itemFreq.items():
            heapq.heappush(heap, (freq,item))

            if(len(heap) > k):
                heapq.heappop(heap)
        
        return [ item for freq, item in sorted(heap, reverse=True)]

def main():
    n = [1,23,44,32,26,23,44,26]
    k = 2
    obj = Solution()
    print(obj.topkFrequent(n,k))

if __name__ == "__main__":
    main()
