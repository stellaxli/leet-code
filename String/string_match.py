#1408. String Matching in an Array

words = ["leetcoder","leetcode","od","hamlet","am"]

subword = []
for i in words:
    for j in words:
        if (i == j):
            continue
        elif (i in j):
            if (i not in subword):
                subword.append(i)
print(subword)