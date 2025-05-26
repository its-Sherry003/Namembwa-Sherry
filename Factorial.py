#Assignment 2: find the factorial of the number 5 (five), 5!
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")