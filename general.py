# 1. Sum of Digits
# Task:
# Given a positive integer n, return the sum of its digits.
# Implementation steps:
# Convert the number to a string.
# Loop through each character.
# Convert each character back to a number.
# Add them together.

n = 352
total = 0
for ch in str(n):
    print(f"Number converted to string: {ch}")
    total += int(ch)

print(f"Total Sum of digits: {total}")

# 2. Count Even Numbers
arr = [1, 2, 3, 4, 5, 6]
count = 0

# For loop iterating through the array starting with num = 1
for num in arr:
    # Check if each number in the array is even. if num == 0, it's even
    if num % 2 == 0:
        # Every evan number found is counted
        count += 1
print(count)

n = 56789
stri = str(n)

for ch in stri:
    total = total + int(ch)

print(total)