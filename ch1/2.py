"""
Q2 ●●○○○○○○○○ 2/10 [truthiness, filter]
List every kind of value that is falsy in Python (at least 8). Then write one line that takes a list of
mixed values and prints only the truthy ones.
"""
x=[None,0,False,0.0, [],(),{},set(),0j]
print("the checker is : if y")

print(*(y for y in x if y))