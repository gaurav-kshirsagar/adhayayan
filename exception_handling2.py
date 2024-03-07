#Finally block:

'''
try:
    print(10/0)
except:
    print('except')
else:
    print('line 2')
finally:
    print('finally')
'''

'''
try:
    print(10/10)
except:
    print('except')
else:
    print('line 2')
finally:
    print('finally')
'''
'''
def functiton():
    try:
        print(10/10)
        #return 100
    except:
        print('except')
        return 200
    else:
        print('line 2')
        return 300
    finally:
        print('finally')
        #return 400
print(functiton())
'''

try:
    raise ValueError('Value error')
except:
    try:
        print(10/0)
        print('except')
    except:
        print('except 2')

'''
class InnvalidAgeException(Exception):
    pass

def check_age(number):
    if number < 18:
        raise InnvalidAgeException('Input value is less than 18')
    else:
        print('Eligible for Vote')

try:
    check_age(17)
except:
    pass
'''
