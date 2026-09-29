"""
Q10 ●●●○○○○○○○ 3/10 [bool is int, arithmetic]
Count how many numbers in a list are even without an if statement and without a loop body,
using the fact that True == 1.
"""
l=[1,2,3,4,5,6,7,8,9]
l2=l.copy()
s=[bool(not (i%2)) for i in l]
print(sum(s))