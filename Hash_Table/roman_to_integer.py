# 13. Roman to Integer

class Solution:
    def romanToInt(s: str) -> int:
        reference = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        romanNum = list(s)
        number = 0

        for i in range(len(romanNum)):
            if (i+1 <= len(romanNum)-1 and reference[romanNum[i]] < reference[romanNum[i+1]]):

                number -= reference[romanNum[i]]
            else:
                number += reference[romanNum[i]]
        return number

print(Solution.romanToInt("III"))