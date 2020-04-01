# https://www.py4e.com/html3/04-functions
#
# Exercise 7: Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
#
# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F
# ========================================================================================


score = input("Enter a score between 0.0 and 1.0: ")

def computegrade(score):
    if score <0 or score >1:
        grade = "Invalid score"
    elif score >=0.9:
        grade = "A"
    elif score >=0.8:
        grade = "B"
    elif score >=0.7:
        grade = "C"
    elif score >=0.6:
        grade = "D"
    else:
        grade = "F"
    return grade

try:
    score = float(score)
    finalmark = computegrade(score)
    print(finalmark)
except:
    print("Invalid input")
