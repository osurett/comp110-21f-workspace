"""Interactive Program That Will Help the User Find The Right Place to Eat in Chapel Hill"""
"""Student PID"""
__author__ = "730530127"


def greet() -> None:
    print("This program will help you choose the best thing for you to eat in Chapel Hill!")
    global player
    player = input("What is your name? ")

def main() -> None:
    global points
    points = 0
    greet()

main()
print(points)

"""meal: str = str(input("To begin, tell us which meal you are looking to eat: breakfast, lunch, dinner or dessert!: "))

if meal == "breakfast" or meal == "Breakfast":
    input("What kind of breakfast food are you looking for? You can say things like “omeletes”,“biscuits”, “pancakes”, “waffles”, or “BLT”: ")
else:
    if meal == "lunch" or meal == "Lunch":
        food: str = str(input("What kind of lunch food are you looking for? You can say things like 'pizza', 'mexican', 'chinese', 'sandwiches', 'salads' or 'burgers': "))
    else:
        if meal == "dinner" or meal == "Dinner":
            food: str = str(input("What kind of dinner food are you looking for? You can say things like 'steak', 'italian', 'chinese', 'japanese', or 'chicken': "))
        else:
            if meal == "dessert" or meal == "Dessert":
                food: str = str(input("What kind of dessert food are you looking for? You can say things like 'cookies', 'bakery', 'cake', or 'ice cream': "))


if __name__ == "__main__":
    main()
    
    define a function for each meal
    """