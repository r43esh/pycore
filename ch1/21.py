"""
Q21 ●●●●●●○○○○ 6/10 [hashing, immutability]
Why can a tuple be a dict key but a list cannot? Make a tuple that still fails as a key. Then write
freeze(x) that converts nested lists/dicts/sets into hashable equivalents.
"""
ans=""" 
a key must be hashable and immutable so we can use tuple but not a list as key
tuple that cant be key :(1,[43,23]) because list can change here

"""
def freeze(x):
    if type(x)==list:
        return tuple([freeze(i) for i in x])
    if type(x)==dict:
        return frozenset((freeze(k),freeze(v)) for k,v in x.items())
    if type(x)==set:
        return frozenset(i for i in x)
    return x