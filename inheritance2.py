#Inheritance Day 2

# Multiple Inheritance:
'''
class A:
    x = 10
class B:
    x = 10
    y = 20
class C(B,A):
    pass

cobj = C()

print(cobj.x)
print(cobj.y)

# Multi - level Inh

class A:
    x =10
class B(A):
    x = 100
class C(B):
    x = 1000
class D(C):
    pass

dobj = D()
print(dobj.x)

print()  
# Hierarchial Inh:

class A:
    x = 10
class B(A):
    y =20
class C(A):
    z = 30

bobj = B()
cobj = C()

print(bobj.x)
print(bobj.y)
#print(bobj.z)

print(cobj.x)
#print(cobj.y)
print(cobj.z)
print()

#issubclass

#bool = issubclass(class1,class2)

class Parentclass:
    pass
class Childclass(Parentclass):
    pass

pobj = Parentclass()
cobj = Childclass()

print(issubclass(Childclass,Parentclass))
print(issubclass(Parentclass,Childclass))

#isinstance
#bool = isinstance(object,class)

print(isinstance(pobj,Parentclass))
print(isinstance(pobj,Parentclass))
print(isinstance(pobj,Parentclass))
print(isinstance(pobj,Parentclass))

#mro Method resoltution order

class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
class E(D):
    pass

print(E.mro())

'''

class A:
    pass
class B:
    pass
class C:
    pass
class D:
    pass
class E:
    pass

class F(A,B,C,D,E):
    pass
class G(E,D,C,B,A):
    pass
    
print(F.mro())
print()
print(G.mro())