'''
PSEUDO CODE: 

A. SORTING + HASHMAP
1. for nums, update COUNT with key:value as number:count
2. array arr, append all elements from hashmap
3. sort the array arr
4. pop k elements from arr (pop pulls from end)

B. MIN HEAP
1. for nums, update COUNT map with key:value as number:count
2. for n in MAP.KEYS()
3. heapq.heappush(heap, (count[n],n)) -- add count,value to heap
4. if len(heap) > k, pop from heap... heapq.heappop(heap)
5. for i till k, append elements from heap to result array
6. return result array


'''
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
        
        topFreqNum = []
        for i in range(k):
            topFreqNum.append(heapq.heappop(heap)[1])
        
        return topFreqNum

def main():
    n = [1,23,44,32,26,23,44,26]
    k = 2
    obj = Solution()
    print(obj.topkFrequent(n,k))

if __name__ == "__main__":
    main()
