from typing import List

class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:

        
        result = []

        # solution 1 - brute force
        # for i in range(0, len(nums)):
        #      for j in range(i+1, len(nums)):
        #           if nums[i] + nums[j] == target:
        #                result = [ min(i,j) , max(i,j) ]
        
        # solution 2 - hashmap
        numIndex = {}
        for i in range(0, len(nums)):
            if target - nums[i] in numIndex:
                  minIndex = min(numIndex[target-nums[i]], i)
                  maxIndex = max(numIndex[target-nums[i]], i)
                  result = [minIndex, maxIndex]
            else:
                numIndex[nums[i]] = i

        return result
    

def main():
        input_array = [1,4,6,7]
        target = 10
        obj = Solution()
        result = obj.two_sum(input_array, target)
        print(result)

if __name__ == "__main__":
    main()
    