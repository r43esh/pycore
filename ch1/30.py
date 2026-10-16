"""
Q30 ●●●●●●●●●○ 9/10 [everything: names, objects, mutation]
Predict the exact output without running:
a = [1, 2, 3]
b = a
c = a[:]
a.append(a)
b = b + [9]
c += a
print(len(a), len(b), len(c))
print(a is a[3], c[3] is a)
"""
ns="""
4 5 7
True False
"""