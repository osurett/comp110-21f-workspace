"""Counting letters in a string."""

__author__ = "730530127"

# Begin your solution here...
letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))

counter: int = 0

while (counter < len(word)):
    if word[counter] == letter:
        counter = (counter + 1)
        print("Count: " + str(counter))
    else:
        counter = (counter + 1)