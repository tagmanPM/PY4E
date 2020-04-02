# https://www.py4e.com/html3/05-iterations
#
# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and
# except and print an error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
#
# Exercise 2: Write another program that prompts for a list of numbers as above and at
# the end prints out both the maximum and minimum of the numbers instead of the average.
#
# ========================================================================================

total = 0
largest = None
smallest = None
count = 0

while True:
    val_input = input("Enter a number: ")
    if val_input == "done":
        break
    try:
        value = float(val_input)
    except:
        print('Invalid input')
        continue
    total = total + value
    count = count + 1
    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value

print(total, count, largest, smallest)

# =========================================================
# PY4E exercise: a variant of the code above
#
#largest = None
# smallest = None
#
# while True:
#     val_input = input("Enter a number: ")
#     if val_input == "done":
#         break
#     try:
#         value = int(val_input)
#     except:
#         print('Invalid input')
#         continue
#     if largest is None or value > largest:
#         largest = value
#     if smallest is None or value < smallest:
#         smallest = value
#
# print('Maximum is',largest)
# print('Minimum is',smallest)
