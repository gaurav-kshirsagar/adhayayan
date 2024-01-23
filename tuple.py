#Tuple:

#Empty Tuple
tup = ()
print("tup= ",tup)
print(type(tup))

#Orderd , Heterogeneous allows duplicate elements:
tup2 = (10,20,30,'Adhyayan',True,3.14,30)
print("tup2= ",tup2)

#Tuple supports both positive and negative indexing:

print("tup2[0]= ",tup2[0])
print("tup2[-1]= ",tup2[-1])


#Tuple Supports slicing operations:
print("tup2[1:4:1]= ",tup2[1:4:1])

#Buil in Functions:

tup3 = (10,20,30,40,50,60)
print("max=",max(tup3))
print("min=",min(tup3))
print("sum=",sum(tup3))
print("len=",len(tup3))
print("sorted=",sorted(tup3))
print("sorted_rev=",sorted(tup3,reverse=True))

print("tup3 count(50)=",tup3.count(50))

print("tup3 index(50)=",tup3.index(50))

