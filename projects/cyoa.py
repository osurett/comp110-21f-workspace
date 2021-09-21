__author__ = "730530127"

player: str = str(input("What is your name? "))
points: int = 0


def main():
    print(player + ", This program will help you choose the best thing to eat in Chapel Hill!")

if __name__ == "__main__":
    main()

meal: str = str(input("To begin, tell us which meal you are looking to eat: breakfast, lunch, dinner or dessert!: "))

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
