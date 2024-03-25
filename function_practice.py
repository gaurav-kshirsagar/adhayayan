# function practice

#non- parameterized function:
'''
def add():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = a + b
    print('add= ',c)

add()


def sub():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = a - b
    print('sub= ',c)
sub()
'''

# parameterized function:
'''
def add(a,b):
    c = a + b
    print('addition= ',c)

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

add(a,b)

def sub(a,b):
    c = a-b
    print('Subs= ',c)
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

sub(a,b)
'''

'''
def grade(marks):
    if marks < 35:
        print('Grade = F')
    elif marks >= 90:
        print('Grade = O')
    elif marks >= 80:
        print('Grade = D')
    elif marks >= 35:
        print('Grade = P')

marks = int(input('Enter your marks'))
grade(marks)
'''

a = int(input('Enter a number'))

if a > 0:
    print('Positive number')
elif a < 0:
    print('Negative number')
elif a == 0:
    print('Zeroo')




