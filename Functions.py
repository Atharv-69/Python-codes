#Functions are of two types 
# Built in functions
# Self defined function 

# Built in functions


#len()
# fruits = ["apple", "banana", "cherry"]
# length = len(fruits)  # Returns the number of items in the list
# print(length)


#type()
# name = "Atharv"
# length = len(name)
# print(length)
# print(type(name))  


# # str(), int(), float()
# marks_recieved = "33"
# total_marks = 100
# percentage = (int(marks_recieved)/total_marks)*100
# print(percentage)


# # min() max()
# numbers = [5, 8, 2, 10]
# print(max(numbers)) 
# print(min(numbers))  


# # sum()
# numbers = [5, 8, 2, 10]
# total = sum(numbers) 
# print(total)

# # split()
# # Splitting a string by spaces
# text = "Python is amazing"
# split_text = text.split()
# print(split_text)


# # Splitting a string by comma
# data = "apple,banana,cherry"
# split_data = data.split(',')
# print(split_data)


# # replace()
# # Replacing a word in a string
# text = "I love Python"
# new_text = text.replace("Python", "Java")
# print(new_text)


# # slicing()
# # Slicing a string to get a part of it
# text = "Hello, World!"
# sliced_text = text[0:5:1]  # Get the first 5 characters
# # Negative slicing
# sliced_text = text[0:-1]  
# print(sliced_text)
# _________________________________________________________________________________________

#range function
#syntax of range function 
# range(start , stop , step)
# for i in range(1,9,1):
#     print( i)

# for i in range(5):
#     print(i)

# # User defined functions 
# Function is a block of reusable code which performs a specific task
#syntax of user defined function 
# def function_name(parameters):
    # Function body (code to execute)
    # return result 

def sum(a,b):
    return a+b

print(sum(1,2)) 


# def greet():
    # print("Hello guys")

# greet()


# create a function which takes three numbers as 
#  input and return the largest number 
