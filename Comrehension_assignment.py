# Comrehension_assignment
#1. Strings to Integers
#You are given a list of numeric strings.

#lis = ["1", "2", "3", "4", "5"]
#Write a list comprehension to convert all the string numbers to integers. Assume every element in the list can be converted into integers without error. Expected output:
#[1, 2, 3, 4, 5]
'''
lis = ["1", "2", "3", "4", "5"]
new_list = [int(i) for i in lis]
print('new_list= ',new_list)
'''

'''               
2. Numbers greater than 10
You are given a list of integers.
lis = [1,5,13,4,16,7]
Write a list comprehension to extract all integers in this list that are greater than 10. Expected output:

[13, 16]

'''
'''
lis= [1,5,13,4,16,7]

out= []

for i in lis:
    if i > 10:
        out.append(i)
print('out=',out)

#with comprehension
output = [i for i in lis if i > 10]
print('output=',output)
'''

'''
3. Greater than 10 AND divisible by 3
You are given a list of integers.
lis = [1,12,13,14,15,2,3]
Write a list comprehension to extract all integers in this list that are greater than 10 AND that are divisible by 3. Expected output:

[12, 15]


lis = [1,12,13,14,15,2,3]
out = []
for i in lis:
    if i > 10 and i % 3 == 0:
        out.append(i)
print('out',out)

new_lst = [i for i in lis if i > 10 and i % 3 == 0]
print('new_lst= ',new_lst)
'''

#4. Adding 1 to even numbers only
#You are given a list of integers.

#lis = [1,2,4,5,7]
#Write a list comprehension that adds 1 to even numbers but keeps odd numbers as they are. Hint — use the ternary operator. Expected output:
#[1,3,5,5,7]
'''
lis = [1,2,4,5,7]

even = []
for i in lis:
    if i % 2 == 0:
        even.append(i+1)
    else:
        even.append(i)
print(even)

#with comprehension:

even_list = [i+1 if i%2 == 0 else i for i in lis]
print('even= ',even)
'''
#5. Numbers containing digit 1
#Write a list comprehension that returns all numbers between 1 and 100 (inclusive) that contains the digit 1. Expected output:

#[1,10,11,12,13,14,15,16,17,18,19,21,31,41,51,61,71,81,91,100]

one_list=[]
for i in range(1,101):
    if "1" in str(i):
        one_list.append(i)
print('one_list= ',one_list)

number_w_1 = [i for i in range(1,101) if "1" in str(i)]
print('number_w_1= ',number_w_1)


    
