word: str = input("Enter a word: ")

i: int = 0
while i < len(word):
    j: int = 0
    """Inner Loop Starts"""
    while j < len(word):
        print(word[j])
        j += 1
    """Inner Loop Ends"""
    i += 1