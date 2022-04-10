# 875. Koko Eating Bananas -- WIP
import math

piles = [312884470]
h = 312884469
class Solution:
    
    def minEatingSpeed(piles, h) -> int:
        #binary search
        maxNum = max(piles)
        minNum = 1

        while (minNum < maxNum):
            middleNum = (minNum + maxNum) // 2
            count = 0
            for i in piles:
                count += math.ceil(i / middleNum)
            if (count <= h):
                maxNum = middleNum
            else:
                minNum = middleNum + 1
        return minNum

            
        

print (Solution.minEatingSpeed(piles, h))