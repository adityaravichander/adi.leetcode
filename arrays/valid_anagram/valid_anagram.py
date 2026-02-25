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