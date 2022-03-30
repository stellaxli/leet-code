#1137. N-th Tribonacci Number

class Solution:
    def tribonacci(n: int) -> int:
        values = {0:0, 1:1, 2:1}
        if (n < 3):
            return values[n]
        for i in range(3,n+1):
            val = values[i-1] + values[i-2] + values[i-3]
            values[i] = val

        return val

print(Solution.tribonacci(5)) # 7 