'''
PSEUDO CODE: 

A. HASH TABLE:
1. FOR iterate through list of strings
2. FOR iterate through one string
3. update COUNT map [0] * 26 with key: value as char: count
4. update RESULT map with key:value as tuple(count) : string
5. RETURN LIST(RESULT.VALUES)

'''
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
