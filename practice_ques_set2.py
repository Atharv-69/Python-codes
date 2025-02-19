# 1. Write a Python program to make calculator
a =int(input("enter your num 1:"))
b = int(input("enter your num 2:"))
oper = (input("what is operator:"))
if oper=="+":
    print("the sum of a and b is :",a+b)
elif oper=="-":
    print("the subt of a and b is :",a-b)
    
elif oper=="*":
    print("the multiplication of a and b is:",a*b)

elif oper=="/":
    print("the division of a and b is:",a/b)

else:
    print("error")


# 2. Write a Python program to take name as user input and check whether
#   the name contains vowels
def contains_vowels(name):
    vowels = 'aeiouAEIOU'
    for char in name:
        if char in vowels:
            return True
    return False

name = input("Enter your name: ")

if contains_vowels(name):
    print(f"The name '{name}' contains vowels.")
else:
    print(f"The name '{name}' does not contain vowels.")


# 4. Write a Python program that uses sets to store discounts based on
# different customer types. Use a nested if condition to check:
# a. If the customer is a "new" customer, apply a 5% discount.
# b. If the customer is a "loyal" customer, apply a 10% discount.
# c. If the customer is a "VIP" customer, apply a 15% discount.
# d. Calculate the total discount based on the customer's type.
def calculate_discount(customer_type):
    discounts = {
        "new": 0.05,     # 5% discount for new customers
        "loyal": 0.10,   # 10% discount for loyal customers
        "VIP": 0.15      # 15% discount for VIP customers
    }

    if customer_type in discounts:
        discount = discounts[customer_type]
        return discount
    else:
        return 0 

customer_type = input("Enter customer type (new/loyal/VIP): ").lower()

total_amount = float(input("Enter the total purchase amount: "))

discount_percentage = calculate_discount(customer_type)

total_discount = total_amount * discount_percentage

final_amount = total_amount - total_discount

if discount_percentage > 0:
    print(f"As a {customer_type} customer, you get a {int(discount_percentage * 100)}% discount.")
    print(f"Total discount: ${total_discount:.2f}")
    print(f"Final amount to pay: ${final_amount:.2f}")
else:
    print("Invalid customer type or no discount available.")



# 3. Write a ternary operator to check if a string is empty and return
#   “Empty” if true, and “Not Empty” if false.
my_string = input("Enter your string: ")  
result = "Empty" if my_string=="" else "Not Empty"
print(result)