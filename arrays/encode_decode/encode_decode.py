from typing import List
class Solution: 

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    """

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string
    
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str) -> List[str]:
        decoded_string, i = [], 0

        while i < len(str):
            
            j = i
            
            while str[j] != "#":
                j += 1
            
            length = int(str[i:j])

            decoded_string.append(str[j+1 : j+1+length])

            i = j + 1 + length
        
        return decoded_string

def main():
    string_input = ["asdasdas", "asd"]
    object = Solution()
    enc_string = object.encode(string_input)
    dec_string = object.decode(enc_string)
    print(dec_string)

if __name__ == "__main__":
    main()

        