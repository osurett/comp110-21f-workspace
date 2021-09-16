"""Finding duplicate letters in a word."""

__author__ = "730530127"

word: str = str(input("Enter a word: "))
dup: bool = False
i: int = 0

while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            print("Found duplicate: True")
            i = len(word)
        else:
            if j == len(word):
                print("Found duplicate: False")

        j += 1
    i += 1
