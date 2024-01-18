#List

#Empty List:
Li1 = []
print("Li1=",Li1)

#Ordered Index:
Li2 = [10,20,30,40,50]
print("Li2=", Li2)

#Hetrogenius:
Li3 = [10,"Adhayan",3.14,True]
print("Li3=",Li3)

#Allows Duplicate Value:
Li4=[10,20,10,30,10,10,40,50,10]
print("Li4=",Li4)


#Supports both positive and negative indexing:

#        0  1  2  3  4  5  6  7  8  9  
marks = [10,20,30,40,50,60,70,80,90,100]
#                       -5 -4 -3 -2  -1

print("marks=", marks)
print("marks[0]=",marks[0])
print("marks[-10]=", marks[-10])
print("marks[5]=", marks[5])
print("marks[7]=", marks[7])
print("marks[-3]=", marks[-3])

#Slicing:

#print(list_name[start:stop:steps])
print("marks[0:5:1]=",marks[0:5:1])
print("marks[3:8:1]=",marks[3:8:1])
print("marks[:5:1]=",marks[:5:1])
print("marks[:8:]=",marks[:8:])
print("marks[::]=",marks[::])
print("marks[::2]=",marks[::2])



#Buil in function:
marks = [100,20,90,30,60,40,50,70,80]

print("marks=", marks)
print("max=", max(marks))
print("min=", min(marks))
print("sum=", sum(marks))
print("len=", len(marks))
print("sorted=", sorted(marks))
print("sorted_rev=", sorted(marks, reverse = True))
