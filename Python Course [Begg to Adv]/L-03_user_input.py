# Lesson 3: Taking User Input in Python:

#Get user details:
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter height in cm: "))

# Calculate something simple:
age_next_year = age + 1

# Display with labels:
print("\n--- User Summery ---")
print("Name: ", full_name)
print("Age now: ", age)
print("Age next year: ", age_next_year)
print("Height: ", height, "cm")