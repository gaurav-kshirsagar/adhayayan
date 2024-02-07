#return statement

'''
def greet():
    print("Good morning")
    return 5
print(greet())


def cal_bill(prod1,prod2):
    total_bill = prod1 + prod2
    return total_bill

tot = cal_bill(100,200)
print("total_bill = ",tot)
print("Discount = ",tot/2)
print("with GST =",tot * 1.18)


'''

def fun():
    print("fun starts")
    return 10
    return 20
    return 30
    print("fun ends")
print(fun())
