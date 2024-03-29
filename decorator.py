# DECORATOR

'''
def mydeco(func):
    def inner():
        print('*'*10)
        func()
        print('*'*10)
    return inner



@mydeco
def foo():
    print('Hello')

foo()

'''


#######
'''
def outer(func):
    def inner(string1):
        res = func(string1)
        return res[::-1]
    return inner

@outer
def upper_case(string1):
    return string1.upper()
print(upper_case('gsk'))
'''
#########

'''
def discount(func):
    def inner(grocery):
        total_bill = func(grocery)
        return total_bill - total_bill * 0.20
    return inner


grocery = {'milk':40,'tea':30,'soap':30}

@discount
def grocery_bill(grocery):
    res = 0
    for k,v in grocery.items():
        res += v
    return res
    
print(grocery_bill(grocery))
'''


valid_user = {
    "user1": {"username":"abc","password":"abc123"},
    "user2": {"username":"pqr","password":"pqr123"}
    }


def return_user_or_None(user,pwd):
    for k,v in valid_user.items():
        if v['username'] == user and v['password']== pwd:
            return k
        else:
            print('User not found!!!')

def login_required(func):
    def inner():
        user = input("Enter username: ")
        pwd = input('Enter password: ')
        res = return_user_or_None(user,pwd)
        if res:
            print('Access Granted')
            func()
        else:
            print("Permission Denied")
    return inner
            
@login_required
def imp_function():
    print('imp function accessed')

imp_function()



































