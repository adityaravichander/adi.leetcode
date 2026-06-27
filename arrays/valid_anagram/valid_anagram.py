'''
PSEUDO CODE: 

A. SORT
1. SORT BOTH INPUTS
2. COMPARE IF THEY ARE EQUAL

B. HASHMAP
1. FOR i len(input)
2. UPDATE TWO HASHMAPS for TWO INPUTS
3. COMPARE TWO HASHMAPS

C. HASHTABLE USING ARRAY
1. COUNT ARRAY [0] *26
2. FOR i len(input)
3. count[char] +1 if in input1, count[char] -1 if in input2
4. FOR count 
5. if value != 0, return False, else True


'''
import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        
        # 1 - brute force - sorted() function
        # return sorted(s) == sorted(t)
    
        # 2 - hashmap solution
        
        cS, cT = {}, {}
        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0)
            cT[s[i]] = 1 + cT.get(t[i], 0)     
        return cS == cT


    
def main():
    p = "abcde"
    q = "a"

    obj = Solution()

    result = obj.isAnagram(p,q)
    print(result)

if __name__ == "__main__":
    main()
