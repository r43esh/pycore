"""
Q19 ●●●●●○○○○○ 5/10 [closures, late binding]
funcs = [lambda: i for i in range(3)]. Predict [f() for f in funcs]. Fix it in two different ways.
"""
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
ans="""
it will print 2,2,2 whyy because it didnt use default arguemnt and now
late binding will happen it means lambda wont keep updating the values instead it will]
use the final value of i here in all cases
"""
print(ans)

func=[lambda i=i: i for i in range(3)]
print([f() for f in func])

print("next fix is helper funciton ")
def h(i):
    return lambda:i

funcs = [h(i) for i in range(3)]
print([f() for f in funcs])






note="""
read about lambda a: e and its use with filter map and sorted()
agar default argument diya hai: iski current value ko use krta hai
vrna : final value ko hi bar bar use kr lega
"""
print(note)