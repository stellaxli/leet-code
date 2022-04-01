# 997. Find the Town Judge
import collections

class Solution:
    def findJudge(n: int, trust) -> int:
        if (len(trust) < n-1):
            return -1
        
        neighbour = collections.defaultdict(list)
        countNeighbour = collections.defaultdict(int)

        for current, trusts in trust:
            neighbour[current].append(trusts)
            countNeighbour[trusts] += 1
            
        for node in range(1, n+1):
            if (not neighbour[node] and countNeighbour[node] == n-1):
                return node
            
        return -1
        
print(Solution.findJudge(3,[[1,3],[2,3]]))
        