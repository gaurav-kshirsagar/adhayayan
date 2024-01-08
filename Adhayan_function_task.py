# perform arithmetic operations using function parameter and non parameter:
# Arthematic operations Without parameter 

a=int(input("Entyer 1st number : "))
b=int(input("Enter 2nd number :"))

def add():
    # a=int(input("Entyer 1st number : "))
    # b=int(input("Enter 2nd number :"))
    c = a+b
    print(f'addition is: {c}')

def sub():
    # a=int(input("Entyer 1st number : "))
    # b=int(input("Enter 2nd number :"))
    c = a-b
    print(f'substraction is {c}')

def mul():
    c = a*b
    print(f'multiplication is {c}')

def div():
    c = a/b
    print(f'Division is {c}')

def mod():
    c = a%b
    print(f'mod of the number is {c}')

add()
sub()
mul()
div()
mod()

# #Arthematic operations With Parameter  
# a=int(input("Enter 1st number : "))
# b=int(input("Enter 2nd number : "))
    
# def add(a,b):
#     c = a+b
#     print(f'addition is: {c}')
# add(a,b)

# def sub(a,b):
#     c = a-b
#     print(f'substraction is: {c}')
# sub(a,b)

# def mul(a,b):
#     c = a*b
#     print(f'multiplication is: {c}')
# mul(a,b)

# def div(a,b):
#     c = a/b
#     print(f'division is: {c}')
# div(a,b)