"""
Q13 ●●●●○○○○○○ 4/10 [short-circuit, or/and]
Predict: 0 or "" or [] or "hi", 1 and 2 and 0 and 3, None or 0, [] and 5. State the rule in one
sentence, then write a one-line first_non_empty(a, b, c).
"""
x=0 or "" or [] or "hi"
y= 1 and 2 and 0 and 3
z=None or 0
w= [] and 5
print(x,y,z,w)

ans="""
 or : first truthy return
 and: first false return


"""
def first_non_empty(a,b,c):
    return a or b or c