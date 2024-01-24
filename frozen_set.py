#Frozenset:
#Syntax: frozenset(iterable) in iterable we can pass string, list, tuple,
#set, dict etc..

vowels = {'a','e','i','o','u'}

fset1 = frozenset(vowels)    
print('fset1= ',fset1)
print(type(fset1))


alpha = {'a','b','i','o','c','d'}
fset2 = frozenset(alpha)
print("fset2= ",fset2)

#Union in frozenset:
print('Union= ', fset1|fset2)

#Intersection:
print("Intersection= ", fset1 & fset2)

#Difference:
print("Difference= ", fset1 - fset2)

#There are no methods like add,update, remove, for frozent set
#if we perform it will throw an error.

print('fset1= ',fset1)
fset1.add('g')
