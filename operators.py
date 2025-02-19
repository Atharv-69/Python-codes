# # # Aritmetic operators
# # #Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

# # #variables

# # a = 20
# # b = 67
# # # Variables
# # # a = 15
# # # b = 4

# # # Addition
# # print("Addition:", a + b)  

# # # Subtraction
# # print("Subtraction:", a - b) 

# # # Multiplication
# # print("Multiplication:", a * b)  

# # # Division
# # print("Division:", a / b) 

# # # Floor Division
# # print("Floor Division:", a // b)  

# # # Modulus
# # print("Modulus:", a % b) 

# # # Exponentiation
# # print("Exponentiation:", a ** b)  

# #In Python Comparison of Relational operators compares the values. It either returns True or False according to the condition.

# c = 13
# d = 10.9

# print(c > d)
# print(c < d)
# print(c == d)
# print(c != d)
# print(c >= d)
# print(c <= d)

#Logical Operators in Python
#Perform the operation such as Logic Gates

#logical AND - Perform AND operation(all of these inputs are high/true then output will true)
#logical OR -  Perform OR Operation(any one input is true output will true)
#logical NOT - Perform invert/complement operation 

x = 101110
y = 110000

print(x and y)
print(x or y)
print(not x)
print(not y)

# #Prectice Question
# #Find the binary numbers of any two numbers and perform logical AND and OR operation

# dec_num1 = int(input("Enter a num1 :  "))
# dec_num2 = int(input("Enter a num2 :  "))
# binary1 = bin(dec_num1)
# binary2 =  bin(dec_num2)

# # bin function used to calculate binary number of any number passing as parameter

# print(binary1)
# print(binary2)
# print(binary1 and binary2)
# print(binary1 or binary2)

# #Bitwise Operators
# #Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

# # Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

# # Bitwise Operators in Python are as follows:

# # Bitwise NOT
# # Bitwise Shift
# # Bitwise AND
# # Bitwise XOR
# # Bitwise OR

# i = 10
# j = 4

# print(i & j)
# print(i | j)
# print(~i)
# print(i ^ j)
# print(i >> j )
# print(i<< 2)

#Identity Operators in Python
#In Python, is and is not are the identity operator both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
# is     =     True if the operands are identical 
# is not  =    True if the operands are not identical 

l = 10
k = 20
w = l

print(l is not k)
print(l is w)

# Membership Operators in Python
# In Python, in and not in are the membership operator  that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

# m = 24
# n = 20
# list = [10, 20, 30, 40, 50]

# if (m not in list):
#     print("m is NOT present in given list")
# else:
#     print("m is present in given list")

# if (n in list):
#     print("n is present in given list")
# else:
#     print("n is NOT present in given list")

# g, h = 10, 20
# min = g if g < h else h

# print(min)

