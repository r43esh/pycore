"""
Q4 ●●○○○○○○○○ 2/10 [assignment, swap]
Swap two variables in three different ways: with a temp, with tuple unpacking, and with
arithmetic. Why does the arithmetic way fail for strings and can it overflow in Python?
"""
a,b=2,4
print(a,b,end=" ")
a,b=b,a
print(a,b)

temp=float("inf")
print(a,b,end=" ")
temp=a
a=b
b=temp


print(a,b)
print(a,b,end=" ")
a=a+b
b=a-b
a=a-b
print(a,b)

"""
in python we cant use arithmetic way for strings because it will
create concatanation and when you subtract will will throw an error

and also int wont overflow easily in python because it has dynamic size
"""