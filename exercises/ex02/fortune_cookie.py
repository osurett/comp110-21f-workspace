"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730530127"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
rand: str = str(randint(1, 4))
if rand == "1":
    print("You will learn something new today.")
else:
    if rand == "2":
        print("Your life will improve today. ")
    else:
        if rand == "3":
            print("You will meet someone that will be beneficial to your career today.")
        else:
            print("Today will be your most prouductive day of the month.")

print("Now, go spread positive vibes!")