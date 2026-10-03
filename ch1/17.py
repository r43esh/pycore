"""
Q17 ●●●●●○○○○○ 5/10 [isinstance, bool trap]
Write describe(x) returning 'bool', 'int', 'float', 'str', 'list' or 'other'. Why does the order of your
checks matter? What goes wrong with isinstance(True, int)?

"""
def describe(x):
    if isinstance(x,bool):
        return "bool"
    if isinstance(x,int):
        return "int"
    if isinstance(x,float):
        return "float"
    if isinstance(x,str):
        return "string"

    else :
        return "other"

print(describe(True))