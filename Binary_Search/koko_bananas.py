# 875. Koko Eating Bananas -- WIP
import math

# piles = [3,6,7,11], h = 8
class Solution:
    
    def minEatingSpeed(piles, h) -> int:
        maxNum = max(piles)
        minNum = 1
        k = 0
        print(maxNum)
        print((maxNum + 1) // 2)
        while (minNum <= maxNum):
            print('max = ', maxNum)
            print('min = ', minNum)
            middle = (maxNum + 1) // 2
            count = 0
            for i in piles:
                print(count)
                count += math.ceil(i/middle)

            if (count <= h):
                k = middle
                maxNum = middle - 1
            else:
                minNum = middle + 1
        
        return k

print(Solution.minEatingSpeed([3,6,7,11],8))
            
        