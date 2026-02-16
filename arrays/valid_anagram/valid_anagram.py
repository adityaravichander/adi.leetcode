import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        return sorted(s) == sorted(t)
    
def main():
    p = "abcde"
    q = "a"

    obj = Solution()

    result = obj.isAnagram(p,q)
    print(result)

if __name__ == "__main__":
    main()