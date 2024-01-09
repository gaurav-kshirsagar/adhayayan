# sum = 0
# for i in range(2,21,2):
#     print(i)
#     sum = sum + i
# print("sum:", sum)

# sum = 0
# for i in range(1,21,2):
#     print(i)
#     sum = sum + i
# print("Sum = ", sum)

# n = int(input("Enter the number: "))
# if n <= 9:
#     print("1")
# elif n <= 99:
#     print("2")
# elif n <= 999:
#     print("3")

num = int(input("Enter the number which you want to fimd the factorial:"))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
        print(factorial)
    print("Factorial of", num, "is", factorial)