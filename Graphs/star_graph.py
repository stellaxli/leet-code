# 1791. Find Center of Star Graph

class Solution:
    def findCenter(edges) -> int:
        dict = {}
        for i in edges:
            for index in i:
                if (index in dict):
                    dict[index] += 1
                else:
                    dict[index] = 1

        for i in dict:
            if (dict[i] == len(edges)):
                return i

print(Solution.findCenter([[1,2],[5,1],[1,3],[1,4]]))