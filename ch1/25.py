"""
Q25 ●●●●●●●○○○ 7/10 [sentinel objects, default args]
Write f(x, default=None) where None is a legitimate value a caller might pass. How do you tell
"argument not passed" from "passed None"?
"""
MISSING= object()
def f(x,default=MISSING):
    if default is MISSING:
        print("argument not passed")
    else:
        print("argument is ",default)

f(3)
f(3,None)