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
    


