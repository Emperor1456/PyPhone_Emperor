# Lesson 9: Assignment Operators

balance = 5000
print("Starting balance: ", balance)

# Deposit
deposit =int(input("Enter deposit amount: "))
balance += deposit
print("After deposit: ", balance)

# Withdrawal
withdraw = int(input("Enter withdrawal amount: "))
balance -= withdraw
print("Final Balance: ", balance)