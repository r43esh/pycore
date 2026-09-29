"""
Q5 ●●●○○○○○○○ 3/10 [is vs ==, small ints]
a = 256; b = 256; c = 257; d = 257. Predict a is b and c is d in a script and in the REPL. Why
must you never rely on this
"""

a=256
b=256
c=257
d=257

if a is b and c is d:
    print("a is b and c is d") 

else:
    print("not same")
"""
both pairs says the values are same and that is because python sees assigns same obj for same value
in the beginning if values are same so we should not use "is" for checking instead
we can use == for values
"""