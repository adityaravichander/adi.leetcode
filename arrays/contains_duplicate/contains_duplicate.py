'''
ARRAYS _ CONTAINS DUPLICATE
PSEUDO CODE

A. HASH SET
1. FOR array
2. if nums[i] in set() -- True
3. else add nums[i] to set

B. SORTING
1. sort
2. FOR iterate array
3. if nums[i] = nums[i-1] -- True, else False

C. BRUTE FORCE

1. FOR I  
2. inside that FOR J = i+1
3. if nums[i] = nums[j] -- True, else False

'''
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        for i in range(1, len(nums)):
              if nums[i] == nums[i-1]:
                    return True
        
        return False
    
def main():
        n = [1,2,3,4,5,5]
        sol = Solution()
        result = sol.hasDuplicate(n)
        print(result)

if __name__ == "__main__":
        main()
    


