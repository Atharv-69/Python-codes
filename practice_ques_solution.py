# using class 

# class ATM:
#     def __init__(self, balance=1000):
#         self.balance = balance

#     def check_balance(self):
#         print(f"Your current balance is: ${self.balance}")
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount} deposited successfully. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount.")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance.")
#         elif amount <= 0:
#             print("Invalid withdrawal amount.")
#         else:
#             self.balance -= amount
#             print(f"${amount} withdrawn successfully. Remaining balance: ${self.balance}")
    
#     def exit_atm(self):
#         print("Thank you for using the ATM. Goodbye!")
#         exit()


# def main():
#     atm = ATM()
    
#     while True:
#         print("\nATM Machine")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         try:
#             choice = int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input! Please enter a number between 1 and 4.")
#             continue
        
#         match choice:
#             case 1:
#                 atm.check_balance()
#             case 2:
#                 amount = float(input("Enter deposit amount: "))
#                 atm.deposit(amount)
#             case 3:
#                 amount = float(input("Enter withdrawal amount: "))
#                 atm.withdraw(amount)
#             case 4:
#                 atm.exit_atm()
#             case _:
#                 print("Invalid choice! Please select a valid option.")

# if __name__ == "__main__":
#     main()

# def check_balance(balance):
#     print(f"Your current balance is: ${balance}")
#     return balance

# def deposit(balance, amount):
#     if amount > 0:
#         balance += amount
#         print(f"${amount} deposited successfully!")
#     else:
#         print("Invalid deposit amount!")
#     return balance

# def withdraw(balance, amount):
#     if 0 < amount <= balance:
#         balance -= amount
#         print(f"${amount} withdrawn successfully!")
#     else:
#         print("Invalid withdrawal amount or insufficient balance!")
#     return balance

# def atm_machine():
#     balance = 1000  # Initial balance
#     while True:
#         print("\nWelcome to the ATM")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         choice = input("Enter your choice: ")
        
#         match choice:
#             case "1":
#                 balance = check_balance(balance)
#             case "2":
#                 amount = float(input("Enter deposit amount: "))
#                 balance = deposit(balance, amount)
#             case "3":
#                 amount = float(input("Enter withdrawal amount: "))
#                 balance = withdraw(balance, amount)
#             case "4":
#                 print("Thank you for using the ATM. Goodbye!")
#                 break
#             case _:
#                 print("Invalid choice! Please select a valid option.")

# # Run the ATM machine
# if __name__ == "__main__":
#     atm_machine()

def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    
    largest = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > largest:
            largest = num  # Update the largest number if a bigger one is found
    return largest

# Example usage
numbers_list = [10, 25, 78, 3, 90, 45, 67]
largest_number = find_largest_number(numbers_list)
print(f"The largest number in the list is: {largest_number}")

