"""Gaining a better understanding of relational operators through this straightforward program"""

__author__: str = 730530127

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

leftint: int = int(left)
rightint: int = int(right)

less: bool = bool(leftint < rightint)
greatorequal: bool = bool(leftint >= rightint)
equal: bool = bool(leftint == rightint)
notequal: bool = bool(leftint != rightint)


print(left + " < " + right + " is " + str(less))
print(left + " >= " + right + " is " + str(greatorequal))
print(left + " == " + right + " is " + str(equal))
print(left + " != " + right + " is " + str(notequal))