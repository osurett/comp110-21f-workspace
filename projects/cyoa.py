"""Interactive Program That Will Help the User Find The Right Place to Eat in Chapel Hill."""
"""Student PID."""
__author__ = "730530127"


points: int
player: str

"""function greet will greet the user upon starting the program"""


def greet() -> None:
    print("This program will help you choose the best place for you to eat at in Chapel Hill!")
    global player
    player = input("What is your name? ")


"""function main will run the main portion of the program"""


def main() -> None:
    global points, player
    points = 0
    greet()

    print("You will start out with " + str(points) + " points. To gain points, use the following interactive game to get a Chapel Hill restaurant reccomendation!")
    meal: str = str(input(player + ", to begin, tell us which meal you are looking to eat: breakfast, lunch, dinner or dessert!: "))

    if meal == "breakfast" or meal == "Breakfast":
        bfood: str = str(input("What kind of breakfast food are you looking for? You can say things like “omeletes”,“biscuits”, “pancakes”, “waffles”, or “BLT”: "))
        if bfood == "biscuits":
            print("You would probably like Sunrise Biscuit Kitchen.")
        if bfood == "BLT":
            print("You should probably try Merritt's.")
        if bfood == "waffles":
            print("Dame's Chicken and Waffles sounds like a good breakfast for you.")
        if bfood == "pancakes":
            print("Breadman's is a good spot for pancakes.")
        if bfood == "omeletes":
            print("Crossroads has some good omeletes")
    else:
        if meal == "lunch" or meal == "Lunch":
            lfood: str = str(input("What kind of lunch food are you looking for? You can say things like 'pizza', 'mexican', 'chinese', 'sandwiches', 'salads' or 'burgers': "))
            if lfood == "pizza":
                print("Pizzeria Mercato in Carrboro has some of the best pizza in the triangle. On days it isn't open, you can try NY Pizza on Franklin Street.")
            if lfood == "mexican":
                print("Que Chula is a very popular mexican food spot.")
            if lfood == "chinese":
                print("A lot of my friends like the food at Shanghai Dumpling.")
            if lfood == "sandwiches":
                print("Bruegger's Bagels has some good sandwiches.")
            if lfood == "salads" or lfood == "salad":
                print("You can try Chopt Creative Salad Company.")
            if lfood == "burgers":
                print("My favorite burger is at Sutton's Drug Store. Supdogs also has good burgers and hot dogs.")
        else:
            if meal == "dinner" or meal == "Dinner":
                dfood: str = str(input("What kind of dinner food are you looking for? You can say things like 'steak', 'italian', 'japanese', or 'chicken': "))
                if dfood == "steak":
                    print("Bin54 is a very popular steakhouse in Chapel Hill.")
                if dfood == "chicken":
                    print("If you want a good fried chicken spot, try Mama Dip's on Rosemary Street.")
                if dfood == "italian":
                    print("Alfredo's Pizza Villa sounds like a good choice for you.")
                if dfood == "japanese":
                    print("You should give Hibachi and Company a try.")
            else:
                if meal == "dessert" or meal == "Dessert":
                    defood: str = str(input("What kind of dessert food are you looking for? You can say things like 'cookies', 'bakery', or 'ice cream': "))
                    if defood == "ice cream":
                        print("You can never go wrong with Ben and Jerry's on Franklin Street.")
                    if defood == "bakery":
                        print("I have heard really good things about Guglhupf Bakery.")
                    if defood == "cookies":
                        print("Insomnia Cookies is a favorite for all UNC Students, and they are open late too!")


if __name__ == "__main__":
    main()