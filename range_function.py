#Range:

#range function takes at least 1 argument and atmost 3 arguments.

#range(start = 0, stop, steps = 1)
print("range(10,21,2")
for j in range(10,21,2):
    print(j)    #o/p 10,12,14,16,18..

print("\nrange(10,21)")
for j in range(10,21):  #range(start= 10,stop= 21,1)
    print(j)    #o/p 10,11,12,13,14.....19,20

print("\nrange(21,10)")
for j in range(21,10):  #range(start= 21,stop= 10,1)
    print(j)    #Blank o/p 

print("\nrange(21)")
for j in range(21):  #range(start=0,stop= 21,1)
    print(j)    # o/p  0,1,2,3,4,5,6,7,.....20

print("\nrange()")
for j in range():  #range()
    print(j)    # TypeError: range expected at least 1 argument, got 0

print("range(10,21,2,5")
for j in range(10,21,2,5):
    print(j)    #TypeError: range expected at most 3 arguments, got 4
