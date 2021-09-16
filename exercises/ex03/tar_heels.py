"""An exercise in remainders and boolean logic."""

__author__ = "730530127"


# Begin your solution here...
entry: int = int(input("Enter an int: "))

if((entry % 2 != 0 and entry % 7 != 0)):
    print("CAROLINA")
else:
    if((entry % 2) == 0 and (entry % 7) == 0):
        print("TAR HEELS")
    else:
        if (entry % 2) == 0:
            print("TAR")
        else:
            if(entry % 7) == 0:
                print("HEELS")
