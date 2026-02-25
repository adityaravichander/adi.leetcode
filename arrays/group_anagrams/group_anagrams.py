from typing import List
import string
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26    
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s) 
                

        return list(result.values())


def main():
    input = ["act","pots","tops","cat","stop","hat"]
    obj = Solution()
    answer = obj.groupAnagrams(input)
    print(answer)

if __name__ == "__main__":
    main()