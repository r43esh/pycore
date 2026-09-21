"""
Q8 ●●●○○○○○○○ 3/10 [default arguments]
Predict the output, then fix the function properly:
def f(x, acc=[]):
 acc.append(x)
 return acc
print(f(1)); print(f(2)); print(f(3, []))
"""
ans="""
the default argument is made only once so output are 
[1],
[1,2],
[3]
...if i want to make only once then it will be :
def(x,acc=None):
    if not acc:
        acc=[]
    acc.append(x)
    return acc
"""
print(ans)