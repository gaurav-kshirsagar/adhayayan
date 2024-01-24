#Set
#Empty Set:

s1 =set()
print("s1=",s1)
print("type=", type(s1))

#Unordered:
s2 = {10,20,30,40,50,60}
print("s2=",s2)
print("type=", type(s2))

#Hetrogenius
s3 = {10,'Adhayayn',3.14,True}
print("s3=",s3)

#Does not allow duplicate elements:
s4 = {10,20,30,40,10,20,50}
print("s4= ", s4)

#Insertion operations:
s6 = {10,20,30,40,50}
print("s6=", s6)

#Insertion:
s6.add(60)                  #Syntax Set_name.add(element)
print("Insertion operations\ns6.add(60)=",s6)

s6.update({70,80,90})       #Syntax Set_name.update({ele1,ele2,....})
print("s6.update({70,80,90})=",s6)

#Removal:
# pop, remove and clear
print("Removal operations\ns6=", s6)

s6.pop()                #Syntax : Set_name.pop()
print("s6.pop()=",s6)

s6.remove(50)           #Syntax : Set_name.remove(50)
print("s6.remove(50)=",s6)

s6.clear()              #Syntax : Set_name.clear()
print("s6.clear()= ",s6)


#Mathematical Operations : Union, intersection, Differnce

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

#Union:
print("Union= ",s1.union(s2))
print("Union= ",s2.union(s1))

#print(s1|s2)
#print(s2|s1)

#Intersection:
print("Intersection= ",s1.intersection(s2))
print("Intersection= ",s2.intersection(s1))

#print(s1 & s2)
#print(s2 & s1)

#Differnce:
print("Difference= ",s1.difference(s2))
#print(s1-s2)



#Frozenset:
vowels = {'a','e','i','o','u'}

fset = frozenset(vowels)
print(fset)
print(type(fset))

vowls = ['a','e','i','o','u']
fset2 = frozenset(vowls)
print("fset2= ",fset2)
print(type(fset2))

other = {'a','b','i','o','c','d'}
fset3 = frozenset(other)
print("fset3= ",fset3)

#Union in frozenset:
print( fset|fset3)

#Intersection:
print("Intersection: ", fset & fset3)

#Difference:
print("Differ", fset - fset3)


abc = (1,2,3,5,4)
fset5 = frozenset(abc)
print(fset5,type(fset5))
