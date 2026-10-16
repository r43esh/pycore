"""
Q24 ●●●●●●○○○○ 6/10 [augmented assignment, __iadd__]
Predict: a = [1,2]; b = a; a += [3]; print(b) and then a = a + [4]; print(b). Explain __iadd__
versus __add__ in plain words.
"""

a = [1, 2]
b = a

a += [3]
print(b)

a = a + [4]
print(b)

ans="""
+= uses augmented assignment ie __iadd__ method 
it means add this in current object inplace

=a+[] means make new list containing contents of a with 4 
then reassign the new list into a

"""
print(ans)