from typing import List

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        # best solution
        self.ops = []

    def updateSubRectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:

        # best solution
        for row1, col1, row2, col2, val in reversed(self.ops):
            if row >= row1 and col1 >= col1 and row <= row2 and col <= col2:
                return val
        
        # brute force
        return self.rectangle[row][col]
    
def main():
    
    object = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
    print(object.getValue(0, 0)) # return 1
    object.updateSubRectangle(0, 0, 2, 2, 100)
    print(object.getValue(0, 0)) # return 100
    print(object.getValue(2, 2)) # return 100
    object.updateSubRectangle(1, 1, 2, 2, 20)
    print(object.getValue(2, 2)) # return 20
    
if __name__ == "__main__":
    main()