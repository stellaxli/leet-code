# 704. Binary Search

class Solution:
    
    def search(nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while (left <= right):
            middleNum = (left+right) // 2
            if (nums[middleNum] == target):
                return middleNum
            elif (nums[middleNum] > target):
                right = middleNum - 1
            elif (nums[middleNum] < target):
                left = middleNum + 1
        return -1

print(Solution.search([-1,0,3,5,9,12], 9))