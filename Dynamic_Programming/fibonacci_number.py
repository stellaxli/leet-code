#509. Fibonacci Number

class Solution:
    def fib(n: int) -> int:
        value = {0:0, 1:1} # initialize dictionary of value at index 0 and 1
        for i in range(2,n+1):
            val = value[i-1] + value[i-2]
            value[i] = val # setting newly calculated value 
            
        return value[n]

print(Solution.fib(10)) #55