"""
Q20 ●●●●●○○○○○ 5/10 [scope, global, nonlocal]
Why does x = 1 followed by def f(): print(x); x = 2 raise UnboundLocalError? Write three
counters: with global, with a list, and with a closure using nonlocal.
"""
x = 10

def f():

    x = 20
    print(x)

f()
print(x)

exp="""
if you want make a var in func it is local if you want to use external func 
var then you have to use nonlocal and if you want to use module level or you can say 
external var then you can use global
"""
print(exp)