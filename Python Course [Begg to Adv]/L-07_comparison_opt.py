# Lesson 7: Comparison Operators

a = 15
b = 20

# Compare a and b
print("a =", a, "| b=", b)
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b", a > b)
print("a < b", a < b)
print("a >= b", a >= b)
print("a <= b", a <= b)

# Compare user age against a threshold
age = int(input("\nEnter your age"))
can_vote = age >= 18
print("Eligible to vote: ", can_vote)