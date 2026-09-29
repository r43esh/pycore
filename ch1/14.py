"""
Q14 ●●●●○○○○○○ 4/10 [chained comparison]
Predict: 1 < 2 < 3, 3 > 2 > 2, 1 == 1 == 1, 1 < 2 > 1, 1 < 3 < 2. Then write is_between(x, lo, hi)
without using and.
"""
a=1 < 2 < 3
b=3 > 2 > 2
c= 1 == 1 == 1
d=1 < 2 > 1
e=1 < 3 < 2

print("values are true false true true flase")

def is_between(x,lo,hi):
    return lo<x<hi