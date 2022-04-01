# 1. Two Sum

class Solution:
    def twoSum(nums, target: int) :
        map = {}
        for index,value in enumerate(nums):
            otherNumber = target - value
            if (otherNumber in map):
                return (index, map[otherNumber])
            
            map[value] = index
            

print(Solution.twoSum([2,7,11,15],9))