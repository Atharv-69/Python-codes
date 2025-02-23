# # ---------------------------------------------------------------
# #  LAMBDA FUNCTION
# def double(x):
#     return x*2

# double = lambda x: x**2
# cube = lambda x: x**3
# avg = lambda x,y: (x+y)/2

# print(double(5))
# print(cube(5))
# print(avg(2,6))


# # -------------------------------------------------------------------
# # FILTER FUNCTION

# l1 = [1,7,3,19,22,40,3,6,77]

# def filter_function(x):
#     return x>15

# newlist = list(filter(filter_function , l1))
# print(newlist) 


# # Write a program that Filter Even Numbers: Given a list of numbers,
# #  use the filter() function with a lambda function to filter out only 
# #  the even numbers.


# numbers = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)