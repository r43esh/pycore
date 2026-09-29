"""
Q12 ●●●●○○○○○○ 4/10 [recursion on structures, copying]
Without importing anything, write deep_copy(x) for arbitrarily nested lists, dicts and tuples of ints
and strings. Show it differs from x[:] and dict(x).
"""
def deep_copy(x):
    if type(x) is list:
       return [deep_copy(i) for i in x]
    elif type(x) is dict:
        return {deep_copy(k):deep_copy(v) for k,v in x.items()}
    elif type(x) is tuple:
        return (deep_copy(i) for i in x)
    else:
        return x
    


b=[2,3,4,[4]]
a=deep_copy(b)
#b.append("hiii babes")
print(a,b)