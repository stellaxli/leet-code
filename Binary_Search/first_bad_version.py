# 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while (left <= right): # go left
            middleNum = (left + right ) // 2
            
            if (isBadVersion(middleNum) == True):
                right = middleNum-1
            elif (isBadVersion(middleNum) == False):
                left = middleNum + 1
                if (isBadVersion(middleNum+1) == True):
                    return middleNum+1
        return 1