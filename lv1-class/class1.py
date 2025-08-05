# 1. Iterating over a list
# A list is a collection of items. Let's say we have a list of fruits.
fruits = ["apple", "banana", "cherry"]

# We can use a for loop to print each fruit in the list.
for fruit in fruits:
    print(fruit)

# 2. Iterating over a string
# A string is a sequence of characters.
# We can loop over a string to get each character.
greeting = "Hello"

for char in greeting:
    print(char)

# 3. The range() function
# The range() function is a great way to generate a sequence of numbers.
# range(5) will generate numbers from 0 to 4 (5 numbers in total).
for i in range(5):
    print(i)

# You can also specify a starting number.
# range(1, 6) will generate numbers from 1 to 5.
for i in range(1, 6):
    print(i)

# --- For Loop Examples ---

# 1. Simple counting
# We already saw this, but let's do it again to print numbers 1 to 10.
for i in range(1, 11):
    print(i)

# 2. Summing up numbers in a list
# Let's say we have a list of numbers and we want to find their sum.
numbers = [1, 5, 10, 3, 7]
total = 0

for num in numbers:
    total = total + num

print(f"The sum of the numbers is: {total}")

# 3. Finding the largest number in a list
# We can also use a for loop to find the largest number in a list.
numbers = [1, 5, 10, 3, 7]
largest_number = numbers[0] # Start by assuming the first number is the largest

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"The largest number is: {largest_number}")


# --- Nested For Loops ---

# What are nested loops?
# A nested loop is a loop inside another loop.
# This is useful for working with 2D data, like a grid or a matrix.

# Example: printing a grid
# Let's print a 3x3 grid of asterisks.
print("\n--- Printing a 3x3 grid ---")
for i in range(3):  # This is the outer loop (for rows)
    row = ""
    for j in range(3):  # This is the inner loop (for columns)
        row += "* "
    print(row)


# --- Practice Problems ---
'''
# 1. Print the even numbers from 1 to 20.
#    Hint: You can use the modulo operator (%) to check if a number is even.
#    (num % 2 == 0) will be true if num is even.

# 2. Given a list of names, print a greeting for each name.
#    names = ["Alice", "Bob", "Charlie"]
#    Expected output:
#    Hello, Alice!
#    Hello, Bob!
#    Hello, Charlie!

# 3. Calculate the factorial of a number.
#    The factorial of 5 (written as 5!) is 5 * 4 * 3 * 2 * 1 = 120.
#    Write a for loop to calculate the factorial of 5.

'''
