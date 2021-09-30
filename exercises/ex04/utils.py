"""List utility functions."""

"""Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int. Example usage:
all([1, 2, 3], 1)
False
all([1, 1, 1], 1)
True
Continue by defining a skeleton function with the following signature:
Name: all
Arguments: A list of integers and an int.
Returns: A bool, True if all numbers match the indicated number, False otherwise or if the list is empty. This algorithm 
should work for a list of any length. Hint: remember you can return from inside of a loop to short-circuit its behavior and return immediately."""

__author__ = "730530127"


# TODO: Implement your functions here.

def all(group: list, one: int) -> bool:
    i: int = 0  
    while i < len(group):
        if group[i] == one:
            i = i + 1
            if i == len(group):
                print("True")
        else:
            print("False")
            i = len(group)


all([2, 2, 2, 2, 2], 2)