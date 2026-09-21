"""
Q6 ●●●○○○○○○○ 3/10 [aliasing, mutability]
a = [1,2,3]; b = a; b.append(4). What is a? Now repeat with a tuple and a string using +=.
Explain why the results differ.
"""
a=[1,2,3]
b=a
b.append(4)
print(a,b,"they will be same bcz mutable")

try:
    s=(1,3)
    t=s
    t+=(2,)
    print(s,t,"may throw error")
except Exception as e :
    print(e)



st="1,2,4"
ts=st
ts+=",5"
print(st,"",ts)