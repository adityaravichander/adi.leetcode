from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda i: i[0])
        merged = [intervals[0]]
        prevj = intervals[0][1]

        for i, j in intervals[1:]:
            prevj = merged[-1][1]
            if prevj > i:
                merged[-1][1] = max(prevj, j)
            else:
                merged.append(i,j)

        return merged

def main():
    intervals = [[1,3], [2,5], [4,7]]
    obj = Solution()
    print(obj.merge(intervals))


if __name__ == "__main__":
    main()