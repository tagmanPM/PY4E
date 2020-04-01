# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate)
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# ===============================================================================

def computepay(hours, rate):
    otrate = rate * 1.5
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40*rate)+(hours-40)*otrate
    return pay

try:
    hours = input("Enter Hours:")
    hours = float(hours)
    hours >= 0
    rate = input("Enter Rate:")
    rate = float(rate)
    rate >= 0
except:
    print("Error, please enter numeric input")
    quit()

wages = computepay(hours, rate)
print("Pay:",wages)
