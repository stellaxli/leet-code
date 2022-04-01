# 35. Search Insert Position
class Solution:
    def searchInsert(nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        middle = -1
        while (left <= right):
            middle = (left + right) // 2
            
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle - 1
            elif (nums[middle] < target):
                left = middle + 1
        if (target > nums[middle]):
            return middle + 1
        return middle

print(Solution.searchInsert([1,3,5,6],5))