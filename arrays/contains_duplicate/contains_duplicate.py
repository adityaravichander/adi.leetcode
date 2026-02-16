from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if(len(nums)<2):
            return False
        
        index = 1
        while(index < len(nums) and len(nums) >=2 ):
            if nums[index] == nums[index-1]:
                return True
            index+=1
        
        return False
    
def main():
        n = [1,2,3,4,5,5]
        sol = Solution()
        result = sol.hasDuplicate(n)
        print(result)

if __name__ == "__main__":
        main()
    


