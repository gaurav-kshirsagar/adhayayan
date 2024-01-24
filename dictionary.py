#Dictionary

#Empty Dictionary:

di = {}
print('di= ',di)
print('type of di= ', type(di))

#Ordered:
di1 = {1:10,2:20,3:30,4:40,5:50}
print('di1= ',di1)

#Heterogeneous Keys:
di2 = {1:10,'Adhyayan':20,3.14:30,False:40}
print('di2= ',di2)

#Heterogeneous Values:

di3 = {1:10,2:'Pune',3:98.30,4:True}
print('di3= ',di3)

#Does not allow duplicate keys:
di4 = {1:10,1:20,1:30,1:40,1:50}
print('di4= ',di4)

#Duplicate values are allowed:

di5 = {1:10,2:10,3:10,4:10}
print('di5= ',di5)


#Does not support any type of indexing :
#print(di5[0])  KeyError:0
#print(di5[-1]) KeyError:-1

#Dictionary does not support slicing operations:
#print(di5[0:4:1])      TypeError

#In Dictionary we can fetch the values using keys.

di6 = {1:10,'Adhyayan':20,3.14:30,False:40}
print('di6[1]=',di6[1])
print("di6['Adhyayan']=",di6['Adhyayan'])

# Insertion operations:

di8 = {1:10,2:20,3:30,4:40,5:50}
print("di8= ",di8)

#Dict_name[key] = value
di8[6]= 60
print("di8= ",di8)

#Dict_name.update({k:v,k:v,....})
di8.update({7:70,8:80})
print("di8= ",di8)

# Removal operations:
#dict.popitem()          Removes the last item

di8.popitem()
print("di8= ",di8)

#dict.pop(item)          Removes the specific item
di8.pop(5)
print("di8= ",di8)

#dict.clear()           Removes all items
di8.clear()
print("di8= ",di8)

#Built in functions:

di7 = {1:10,2:20,3:30,4:40,5:50}

print("max= ",max(di7))
print("min= ",min(di7))
print("sum= ",sum(di7))
print("len= ",len(di7))
print("sorted= ",sorted(di7))
print("sorted_rev= ",sorted(di7, reverse = True))
