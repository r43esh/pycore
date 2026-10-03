"""
Q16 ●●●●●○○○○○ 5/10 [big ints, digits]
Find the digit sum of 2**1000. Then find the number of trailing zeros of 100! two ways: by brute
force and by a formula. Why does Python not overflow here?
"""
x=2**1000
sum=0
for i in str(x):
    sum+=int(i)
#print(sum)
print(sum)
def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n

f=fact(100)
count=0
while f%10==0:
    f//=10
    count+=1
print(f"no of zeros = {count}")

# now with formula
# we just have to calculate no of 5 in 100 fact because
# it will tell us the no of 10s so just this 
