from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            startA, endA = firstList[i]
            startB, endB = secondList[j]

            start = max(startA, startB)
            end = min(endA, endB)

            if start <= end:
                ans.append([start,end])
            
            if endA < endB:
                i+=1
            else:
                j+=1
                
        return ans
    
def main():
    list1 = [[0,2],[5,10],[13,23],[24,25]]
    list2 = [[1,5],[8,12],[15,24],[25,26]]
    obj = Solution()
    print(obj.intervalIntersection(list1, list2))
    return 0

if __name__ == "__main__":
    main()