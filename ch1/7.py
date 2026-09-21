"""
Q7 ●●●○○○○○○○ 3/10 [id(), mutation vs rebinding]
Write three functions that "add x to a list": one using lst += [x], one using lst = lst + [x], one
using lst.append(x). Predict which ones change the caller's list, then verify with id()
"""
def A(x,y):
    x.append(y)
def B(x,y):
    x+=[y]
def C(x,y):
    x=x+[y]

x=[1,2]
A(x,3)
print(x,id(x))
B(x,4)
print(x,id(x))
C(x,5)
print(x,id(x))


