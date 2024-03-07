print('Line 1')
print('Line 2')

try:
    num1 = int(input('Enter the first number'))
    num2 = int(input('Enter the second number'))
    print(num1/num2)
except (ValueError, TypeError) as e:
    print('Value except')

except ZeroDivisionError as e:
    print('Zero division errror')

except:
    print('except')

print('Line 3')
