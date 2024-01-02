

# Importing the pandas library for data manipulation
import pandas as pd

# Basic Data Types in Python
a = 10        # Integer
b = "DY"      # String
c = 3.14      # Floating Point Number
d = True      # Boolean
e = [1, 2, 3, 4] # List

# Dictionary with mixed key types
g = {"a": 10, "b": 20, "c": 40, 15: "DY"}

# Creating DataFrames using pandas (similar to data frames in R)
name = ["JV", "DY", "Bob", "Jose"]
age = [1, 2, 3, 4]
city = ["toronto", "north york", "new york", None]
df = pd.DataFrame({
    "name": name,
    "age": age,
    "city": city,
})

# Uncomment to print DataFrame type and contents
# print(type(df))
# print(df)

# Demonstrating variables with and without values
has_value = ""
no_value = None

# Lists and Looping
f = ["a", "b", "c", "d", 10, 13, 1.30, 2.40]

# Uncomment to print elements using a range-based loop
# for i in range(10):
#     print(f[i])

# Uncomment to print each element in list using a simple for loop
# for element in f:
#     print(element)

# Length of list and iterating over it
# print()
# print("Length of f", len(f))
# for i in range(len(f)):
#     print(f[i])

# Enumerate: Getting both index and value
# print()
# for i, x in enumerate(f):
#     print(i, x)

# Concatenation of strings and lists
a_str = "A"
b_str = "B"
my_str = a_str + b_str  # String concatenation

a_list = [1, 2, 3, 4]
b_list = [5, 6, 7, 8]
my_list = a_list + b_list  # List concatenation

# Uncomment to print concatenated strings and lists
# print(my_str)
# print(my_list)

# Adding elements to a list
my_list.append(9)  # Append a single element
# print(my_list)

c_list = [10, 11, 12]
my_list.extend(c_list)  # Extend list with another list
# print(my_list)

# Exercise - Looping and List Comprehensions
# Example 1: Using for loop to generate a list of even numbers
output = []
iterate = 10
for i in range(iterate):
    output.append(2 * (i + 1))

# Example 2: Using while loop for the same purpose
output = []
iterate = 0
max_iterate = 10
while iterate < max_iterate:
    output.append(2 * (iterate + 1))
    iterate += 1

# Uncomment to print the output list
# print(output)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension examples
output_alt = [2 * (i + 1) for i in range(iterate)]  # Alternative with list comprehension
# print(output_alt)

# More list comprehensions with mathematical operations
powers_of_two = [2 ** i for i in range(iterate)]  # Powers of 2
xor_example = [2 ^ i for i in range(iterate)]     # XOR operation
# print(powers_of_two)
# print(xor_example)

# Conditional Statements
x = 77
# Multiple conditions using 'or' and 'and'
if 5 < x < 10 or x == 77:
    # print(x)
    pass
elif x == 2:
    print("That's a two!")
elif x == 3:
    pass
elif x == 4:
    pass
else:
    # print(x + 10)
    pass

test_string = "A"
# Conditional checks on strings
if test_string == "A":
    # pass  # 'pass' is a placeholder word meaning do nothing
    print(test_string)
elif test_string == "B":
    pass
elif test_string == "C":
    pass
elif test_string == "D":
    pass
else:
    print("no cases matched")
    # pass

# Modulo operation example
modulo_example = 10 % 4
# print(modulo_example)

# FizzBuzz Exercise
# Print "Fizz" for multiples of 3, "Buzz" for multiples of 5,
# "FizzBuzz" for multiples of both 3 and 5, and the number otherwise.

# Function definition for FizzBuzz
def fizzbuzz(n=100):
    for i in range(1, n + 1):
        output_str = ""

        if i % 3 == 0:
            output_str += "Fizz"

        if i % 5 == 0:
            output_str += "Buzz"

        if i % 7 == 0:
            output_str += "Wuzz"

        if i % 11 == 0:
            output_str += "Bizz"

        if output_str == "":
            print(i)
        elif output_str != "":
            print(output_str)

# Function to add one to a number
def add_one(x):
    ret = x + 1
    return ret

# Example calls to the functions
print(add_one(10))  # Expected Output: 11
add_one_list = [add_one(x) for x in range(10)]  # Using list comprehension with a function
print(add_one_list)  # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output = []
# iterate = 10
# for i in range(iterate):
#     output.append(2*(i+1))

# print(output)

# Fizz is a multiplier of 3
# Buzz is a multiplier of 5
# FizzBuzz is a common multiplier of 3 and 5
# a = 10 % 5
# print(a)
n = 100
for k in range(n):
    i = k+1
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz") 
    else : print(i)
