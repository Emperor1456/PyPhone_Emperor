# ═══════════════════════════════════
#   PyPractise  ·  Module 1 Set
#   L-01 → L-13 : Fundamentals
# ═══════════════════════════════════

# 1. Variables & User Input
name = input("Full name: ")
year = int(input("Birth year: "))
age = 2026 - year
print("Record: " + name + " | Age: " + str(age))

# 2. Arithmetic + Typecasting
num = int(input("\nEnter a number: "))
print("Square: " + str(num ** 2))
print("Remainder % 10: " + str(num % 10))

# 3. Comparison & Logical
has_id = input("Has ID? (y/n): ") == "y"
can_vote = age >= 18 and has_id
print("Can vote: " + str(can_vote))

# 4. Assignment Operators
balance = 1000
dep = int(input("\nDeposit: "))
balance += dep
print("After deposit: " + str(balance))
wd = int(input("Withdraw: "))
balance -= wd
print("Final balance: " + str(balance))

# 5. Escape Sequences in output
print("\n--- Summary ---")
print("Name:\t" + name)
print("Age:\t" + str(age))
print("ID:\t" + str(has_id))

# 6. Bitwise Operations
print("\n--- Bitwise quick test ---")
a = 5
b = 3
print("a & b: " + str(a & b))
print("a | b: " + str(a | b))
print("a ^ b: " + str(a ^ b))
print("~a   : " + str(~a))
print("a<<1 : " + str(a << 1))
print("b>>1 : " + str(b >> 1))