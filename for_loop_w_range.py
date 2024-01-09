'''
WAP to print 1,2,3,4,5....100

for i in range(1,101,1):
    print(i)


#WAP to print 10,9,8,7,6...1

for i in range(10,0,-1):
    print(i)


print('PROGRAM STARTS')
for var in range(10,21,1):
    print("Hello",var)
print('PROGRAM ENDS')


#WAP TO print  table of 5:

for i in range(5,51,5):
    print(i)


for j in range(1,11,1):
    print(j*5)


#Q4 WAP to pritn "Adhayan" 50 times.

for i in range(1,51,1):
    print("Adhyayan")


#Q WAP TO finds even numbers range between 1 to 20

for i in range(2,21,2):
    print(i)


#WAP TO create a table which is entered by user:

a = int(input("Enter the numbner the table which you want: "))

for i in range(1,11):
        print(a*i)


for i in range(1,21):
    if i%2 == 0:
        print(i)


# Q WAP to print odd number range between 1 to 20

for i in range(1,21,2):
    print(i)


# WAP to print 1 to n numbers.(n value is taken by user)
n = int(input("Enter the number: "))
for i in range(1,n,1):
    print(i)


# WAP to print n to 1 numbers.(n value is taken by user)
n = int(input("Enter the number: "))
for i in range(n,0,-1):
    print(i)


# WAP to get price of the product from user and pritn total bill by adding the taxes as followed
#if total bill is less than 100 tax is 0%,
#if total bill is greater than or eaual to 200 tax is 15%
#if total bill is greater than or eaual to 500 tax is 20%
#if total bill is greater than or eaual to 1000 tax is 25%

#WAP to get year from the user and check whether it is a leap year or not

year = int(input("enter year: ")) #year = 2200

if year % 4 == 0: #if 2200 %4 ==0: #if 0==0: #if true:
    print("might be a leap year1")
    if year % 100 == 0: # if 2200 % 100 == 0 :# if 0==0: if True:
        print("might be a leap year")
        if year % 400 == 0: #if 2200%400 == 0 : if 220==0: #if false
            print("Leap year")
        else:
            print("Not a leap year1")
    else:
        print("Leap year")
else:
    print("Not a leap year2")


# Check whether the number entered by user is 1 digit,2 digit or 3 digit

num = int(input("Enter the number: "))

if num < 10:
    print("It is One digit number")
elif num <= 99:
    print("It is a Two digit number")
elif num <=999:
    print("It is Three digit number")

'''

# Except the following from the user and calculate the percentage of a class attend.
#1) Total number of working days
#2) Total number of absent days.

#After calculating the percentage if the percentage is less than 75 then student will
#not able for exam.

w_days = int(input("Enter the working days: "))
a_days = int(input("Enter the absent days: "))
pt_days = w_days - a_days

percentage = (pt_days/w_days) * 100

print('Attendance is:', percentage, 'percent')

if percentage >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")


