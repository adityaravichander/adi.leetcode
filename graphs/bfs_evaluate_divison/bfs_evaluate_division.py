from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        variables not in list of equations -- return -1
        input always valid, no use case of division by 0
        example 1:
        a/b = 4
        b/c = 1
        ab/bc = 3.25

        find
        a/c = 4 when eq1 x eq2
        b/a = 0.25 inverse of eq1
        c/c = 1 both elements same
        ab/a = -1 
        d/d = -1 

        example 2: 
        a/b = 0.5
        find a/b = 0.5
        find b/a = 2

        idea is that after selecting numerator - find the denominator which cancel out 
        a -> b -> c
        a -> d-> e
        visualise as two way directed graph with weights 
        '''

        # updating adjacency matrix using equations and values -- building graph
        adjacency_matrix = defaultdict(list)
        for index, equation in enumerate(equations):
            num, den = equation
            adjacency_matrix[num].append([den, values[index]])
            adjacency_matrix[den].append([num, 1 / values[index]])
        

        def bfs(src, target):
            if src not in adjacency_matrix or target not in adjacency_matrix:
                return -1
            
            if src == target:
                return 1
            # queue - query requests... 
            # visited - mark already visited nodes
            q , visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                nodename, wcarry = q.popleft()
                if nodename == target:
                    return wcarry
                
                for neighbour_node, neighbour_weight in adjacency_matrix[nodename]:
                    if neighbour_node not in visit:
                        q.append([neighbour_node, wcarry * neighbour_weight])
                        visit.add(neighbour_node) 

            return -1

        return [ bfs(q[0], q[1]) for q in queries ]

def main():

    object = Solution()
    equations = [["a","b"],["b","c"],["ab","bc"]]
    values = [4.0,1.0,3.25]
    queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

    calculate = object.calcEquation(equations, values, queries)
    print(calculate)
    
if __name__ == "__main__":
    main()