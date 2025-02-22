# Recursion function - It is a type of function which calls itself in the function body 
# Recursion function has two parts 
#    1- Base case - This condition stops the base case 
#    2- Recursive case - This is where the function calls itself with modified arguments 


# Factorial of a number 
# Factorial of 5 = 5*4*3*2*1
# Factorial of 4 = 4*3*2*1
# Factorial of 3 = 3*2*1
# Factorial of 2 = 2*1
# Factorial of 1 = 1
# Factorial of 0 = 1

# def factorial(x) :
#     if x==0 or x==1:
#         return 1
#     else :
#         return x * factorial(x-1)

# num = int(input("Enter your number : "))
# print(factorial(num))


# write a program to print nth number of fibonacci sequence
# Fibonacci sequence - 0,1,1,2,3,5,8....n


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(3))  



# Q1- Write a program which calculates the sum of 
#   first n integer numbers using recursion 


def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return n + sum(n-1)
    
print(sum(5))