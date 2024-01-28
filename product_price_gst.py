# WAP to get price of the product from user and pritn total bill by adding the taxes as followed
#if total bill is less than 100 tax is 0%,
#if total bill is greater than or eaual to 200 tax is 15%
#if total bill is greater than or eaual to 500 tax is 20%
#if total bill is greater than or eaual to 1000 tax is 25%
bill = []

n = int(input("Enter the number of products: "))
for i in range(n):
    price = float(input("Enter the price of the product: "))
    bill.append(price)
    
# print(bill)
total_bill = sum(bill)
print("Total bill: ",total_bill)
if total_bill < 100:
    bill_w_tax = total_bill + (0/100) * total_bill
    print("Bill with tax: ",bill_w_tax)
elif total_bill >= 1000:
    bill_w_tax = total_bill + (25/100) * total_bill
    print("Bill with tax: ",bill_w_tax)
elif total_bill >= 500:
    bill_w_tax = total_bill + (20/100) * total_bill
    print("Bill with tax: ",bill_w_tax)
elif total_bill >= 200:
    bill_w_tax = total_bill + (15/100) * total_bill
    print("Bill with tax: ",bill_w_tax)
elif total_bill >= 100:
    bill_w_tax = total_bill + (10/100) * total_bill
    print("Bill with tax: ",bill_w_tax)

