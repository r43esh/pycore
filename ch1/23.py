"""
Q23 ●●●●●●○○○○ 6/10 [references inside containers]
a = [1, 2]; b = [a, a]; b[0].append(3). Predict b. Then create a list that contains itself, print it,
and explain what Python prints and why it does not loop forever.
"""

a=[1,2]
b=[a,a]
b[0].append(3)
print(a,"  ",b)
ans="""
they print same bcz a is mutable and thus b[0] and b[1] point to 
same location obviously changing one is directly affecting other
"""
print(ans)
x=[]
x.append(x)
print(x)

ans="""
it prints [[... ]] to represent recursive list bcz if not this .. then it will run infinitely and crash
so python detects it and shows this representation
"""