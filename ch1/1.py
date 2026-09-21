"""
Q1 ●●○○○○○○○○ 2/10 [type(), int/float/str/bool, operators]
Predict the type and value of each, before running: 3/2, 3//2, 3.0//2, -3//2, True+True, "3"*3,
[0]*3, "a"+str(1). Explain every result in one sentence.
"""
x=[3/2,3//2,3.0//2, -3//2, True+True, "3"*3,[0]*3, "a"+str(1)]

print([type(u) for u in x])
print("it will say float,int,float,int,int,str,list,str")

print(x)
print("values are 1.5,1,1.0,-2,2,'333',[0,0,0],a1")

