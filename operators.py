num1 = 3
num2 = 4
print(type(num1), type(num2))

#Arithmatic operators
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)   # division sometimes may result in float
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder i.e. discarding the numbers after decimal point
print(num2 % num1)   # this is called modulus i.e. the reminder after division
print(3 ** 4)        # exponent (^) ---> 3^2

# Python supports BODMAS rule when multiple operators are in line
print(5 * 4 + 1)          # first multilpication will be executed
print(1 + 5 * 4)          # same as above first multilpication will be executed
print(5 * (4 + 1) )       # first brackets then rest 

#comparison operator
print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS

print(3 != 2)
 
print(3 > 2)
print(3 < 2)
 
print(3 >= 3)
print(3 >= 2)
 
print(3 <= 2)

#Assignment operator
num = 4
print(num)
num += 1   # is equivalent to num = num + 1
print(num) 

num = 4
print(num)
num -= 1   # is equivalent to num = num - 1
print(num)

num = 4
num *= 2
print(num)

#Logical Operator
#AND Operator
print(True and True)
print(True and False)   # same as False and True
print(False & False)    # instead of and, you can use &
# In short, if any one is false then answer is false 

# OR operator
print(True or True)
print(True or False)    #Truse if any one is true
print(True | True)

#NOT operator
print(not True)
print(not False)

#Functions related to int and float

# abs() function gives positive number
print(abs(-2))
print(abs(-2.1))

# round() function rounds off the digits after decimal point
print(round(3.45))
print(round(-3.95))

# round() function with precision
print(round(3.46, 1))   # round the number till 1 decimal place
print(round(3.46, 2))   # round the number till 2 decimal place
print(round(3.469, 1))   # round the number till 1 decimal place
print(round(3.469, 2))   # round the number till 2 decimal place

#Addition  of string and integer
num1 = 'Hello'
num2 = '5'
print(num1 + num2)   # this is simply concatenation of strings
# Python is smart to figure out that one of the variable is string so the output results in string

#Type casting
a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b)   # because this is string + string, the output will be simple concatenation of the digits i.e. output will be 23 instead of 5
print()                     # Leaves a blank space in output
a = int(a)
b = int(b)
print(a, type(a))       # here you'll get output as int
print(b, type(b))       # here you'll get output as int
print('Addition = ', a+b)


# But if you go about typecasting a proper string into int it'll give error
# THIS CELL WILL GIVE ERROR. IT IS MEANT FOR THAT. DON'T WORRY BECAUSE IT IS RED
a = 'hi'
a = int(a)    # this line will throw error (because python cannot convert 'hi' into  integer)
print(a)   


# Float to str
num = 2.0
print(type(num))
num = str(num)
print(type(num))


# You can pass boolean value (True or False) to the condition in if. In that case, you don't need any logical operator like == or !=
is_subscribed = False
if is_subscribed:              # Read it like - if True do THIS else do THAT
    print('Thank you for the subscription!')  
else:
    print('Please subscribe')