import string

class Solution:

    def valid_palindrome(self, input: str) -> bool:
        l = 0
        r = len(input) - 1

        while l < r:
            while l < r and not self.alphaNum(input[l].lower()):
                l += 1
            while r > l and not self.alphaNum(input[r]):
                r -= 1
            
            if input[l].lower() != input[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def alphaNum(self, char):
        return ( ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'))

def main():

    s = "madam"
    ob = Solution()
    Palin = ob.valid_palindrome(s)
    print(Palin)



if __name__ == "__main__":
    main()