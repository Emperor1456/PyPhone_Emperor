# Lesson 2: Typecasting in python

#Start with different types
age = 25
height_cm = 167.5
id_code = "4521"

# Convert and check types:
age_str = str(age)
height_int = int(height_cm)
id_int = int(id_code)

# Print results with labels:
print("Original age: ", age_str, "-->", type(age))
print("Convert to string: ", age_str, "-->", type(age_str))
print()

print("Original height: ", height_cm, "-->", type(height_int))
print("Convert to int: ", height_int, "-->", type(height_int))
print()
print("Original id_code: ", id_code, "-->", type(id_code))
print("Converted to int: ", id_int, "-->", type(id_int))