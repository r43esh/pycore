"""
Q27 ●●●●●●●○○○ 7/10 [reference counts, del]
Using sys.getrefcount, show how an object's count changes as you add names, put it inside a list,
and del names. Why is the printed number one higher than you expect?
"""
import sys

a = []                 
print(sys.getrefcount(a))  
b = a                 
print(sys.getrefcount(a))  

del b                  
print(sys.getrefcount(a))  

ans="""
getrefcount means tell no of referenc plus 1 bcz of getref func itself
del doesnt destroy obj it destroy reference only
"""