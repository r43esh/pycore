"""
Why is x is None preferred over x == None? Build a small class whose == always returns True and
show that is still tells the truth.
"""
ans="""
is : are they point to same object identity
== : are they having same value no matter location
"""
print(ans)

class A:
    def __eq__(self,other):
        return True
x=A()
print(x==None)
print(x is None)

