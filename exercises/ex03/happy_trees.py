"""Drawing forests in a loop."""

__author__ = "730530127"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
TREEnew: str = str(TREE)

depth: int = int(input("Depth: "))
counter: int = 0

while counter < depth:
    TREEnew = TREE + TREEnew
    counter = counter + 1
    print(TREEnew)