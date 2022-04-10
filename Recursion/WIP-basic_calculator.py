# 224. Basic Calculator
from string import punctuation


s = "-2+ 1"
class Solution:
    def calculate( s: str) -> int:
        answer = 0
        temp = "+"
        newString = ""
        for i in range(len(s)):
            if (s[i] != " " and s[i] != "(" and s[i] != ")"):
                if (s[i] == "+" or s[i] == "-"):
                    if (newString == ""):
                        temp = s[i]
                        continue
                    if (temp == "+"):
                        answer += int(newString)
                    else:
                        answer -= int(newString)
                    temp = s[i]
                    newString = ""
                else:
                    newString += s[i]
        if (newString != ""):
            if (temp == "+"):
                answer += int(newString)
            else:
                answer -= int(newString)
        return answer
                    
print(Solution.calculate(s))
