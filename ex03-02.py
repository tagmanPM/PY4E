# https://www.py4e.com/html3/04-functions
#
# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
#
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
#
# Enter Hours: forty
# Error, please enter numeric input
# ==================================================================================

xh = input("Enter hours:")
try:
    xh = float(xh)
    xh >= 0
    xr = input("Enter rate:")
    xr = float(xr)
    xr >= 0
    if xh <= 40:
        xp = xh * xr
    elif xh > 40:
        xp = (40 * xr) + (xh - 40) * xr * 1.5
    print("Pay:",xp)

except:
    print("Error, please enter numeric input")
