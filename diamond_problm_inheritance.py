# Diamond problem : One of the exxample of hybrid inheritance specifically 
# when created with Hierarchical + Multiple Inheritance.

class A:
    x = 10
class B(A):
    pass
class C(A):
    x = 20
class D(B,C):
    pass

dobj = D()

print(dobj.x)