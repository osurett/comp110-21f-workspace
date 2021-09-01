"""Gaining a better understanding of numeric operators by having the user input 2 numbers to run the given operation on."""

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

leftint: int = int(left)
rightint: int = int(right)

expo: str = str(leftint ** rightint)
slash: str = str(leftint / rightint)
twoslash: str = str(leftint // rightint)
remainder: str = str(leftint % rightint)

print(left + " ** " + right + " is " + expo)
print(left + " / " + right + " is " + slash)
print(left + " // " + right + " is " + twoslash)
print(left + " % " + right + " is " + remainder)