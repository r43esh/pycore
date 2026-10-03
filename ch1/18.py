"""
Q18 ●●●●●○○○○○ 5/10 [tuple mutability, augmented assignment]
t = (1, [2, 3]). Predict what t[1].append(4) does, then what t[1] += [5] does (it raises AND
modifies). Explain step by step what happens.
"""
t=(1,[2,3])
t[1].append(4)
print(t)
try:
    t[1]+=[5]
finally:
    print(t)
ans="""
first will work bcz it is changing the list without interfereing the tuple 
but second one says you have to assign the tuple element so it will cause 
error specifically typeError although now tuple is (1,[2,3,4,5])
"""