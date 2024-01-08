# marks grading:

# marks = int(input("enter your marks :"))


# percent = int(input("Enter the the percent"))
# value = int(input("Enter the value"))
# percentage = (percent/100) * value
# print(percentage)

# total_bill = int(input("Enter the toatl bill: "))
# if total_bill < 100:
#     bill_with_tax = total_bill + (0/100) * total_bill
#     # bill_with_tax = total_bill + tax
#     print(f'bill_with_tax:{bill_with_tax}')
# elif total_bill >= 1000:
#     bill_with_tax = total_bill + (25/100) * total_bill
#     # bill_with_tax = total_bill + tax
#     print(f'bill_with_tax:{bill_with_tax}')
# elif total_bill >= 500:
#     tax = (20/100) * total_bill
#     bill_with_tax = total_bill + tax
#     print(f'bill_with_tax:{bill_with_tax}')
# elif total_bill >= 200:
#     tax = (15/100) * total_bill
#     bill_with_tax = total_bill + tax
#     print(f'bill_with_tax:{bill_with_tax}')
# elif total_bill >= 100:
#     tax = (10/100) * total_bill
#     bill_with_tax = total_bill + tax
#     print(f'bill_with_tax:{bill_with_tax}')


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

