# Lesson 8: Logical Operators

# and - both must be True
age = int(input("Enter age: "))
has_license = input("Do you have a license? (yes/no): ") == "yes"
can_drive = age >= 18 and has_license
print("Can drive: ", can_drive)

# or - at least one True
is_student = input("Are you a student? (yes/no): ") == "yes"
is_senior = age >= 60
gets_discount = is_student or is_senior
print("Gets discount: ", gets_discount)

# not - flip a boolean
print("Not a student: ", not is_student)