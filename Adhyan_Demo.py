# print("Hello world")

# a = 10
# b =  5
# print(a+b)

# a = int(input("Enter your age: "))
# if a > 18:
#     print("you are eligible to vote")
# else:
#     print("Not eligible")

# marks = int(input("Enter your marks: "))
# if marks > 90 :
#     print("Grade is A")
# elif marks > 70:
#     print("Grade is B")
# elif marks > 50:
#     print("Grade is C")
# elif marks > 35:
#     print("Grade is D")
# elif marks < 35:
#     print("Failed!")

# +,-.*,/,//,%,
# non parameterized function:

def add():
    print('non para')
add()

#parameterized function:

# def gmean1(a,b):
#     gmean1 = (a+b)/(a/b)
#     print(gmean1)
# gmean1(20,19)

def add():
    a=int(input("Entyer 1st number : "))
    b=int(input("Enter 2nd number :"))
    c = a+b
    print(c)

def sub():
    a= 10
    b= 5
    c = a-b
    print(c)

def mul(a,b):
    # a = 10
    # b = 5
    c = a * b
    print(c)

def div(a ,b):
    # a = 10
    # b = 2
    c = a / b
    print(c)

a = int(input("Enter the 1st no:"))
b = int(input("enter 1nd no:"))

add()
sub()
mul(a,b)
div(a,b)



