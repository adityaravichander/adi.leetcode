from typing import List

class Solution:

    def asteroid_collison(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] >0:
                diff = ast + stack[-1]

                if diff < 0:
                    stack.pop()
                
                elif diff > 0:
                    ast = 0
                
                else:
                    ast = 0
                    stack.pop()

            if ast:
                stack.append(ast)
        
        return stack

    
def main():

    asteroids_input = [2,4,-4,-1]
    obj = Solution()
    print(obj.asteroid_collison(asteroids_input))
if __name__ == "__main__":
    main()