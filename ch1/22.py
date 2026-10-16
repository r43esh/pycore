"""
Q22 ●●●●●●○○○○ 6/10 [strings immutable, performance]
Build a string of 100,000 characters (a) with += in a loop and (b) with join. Time both with
time.time(). What does string immutability imply, and why is += sometimes fast anyway?
"""
import time

n=100_000

start= time.time()
s=""
for _ in range(n):
    s+="a"

print(len(s))
print("time taken is ",time.time()-start)

start= time.time()

s=""
s="".join(['a'])*100_000
print(len(s))
print("time taken is ",time.time()-start)
