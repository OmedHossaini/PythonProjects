import random

def get_random_joke():
    """Returns a random joke from a predefined list."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the math book look sad? Because it had too many problems.",
        "Why can’t you give Elsa a balloon? Because she’ll let it go!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why don’t eggs tell jokes? They’d crack each other up.",
        "How does a penguin build its house? Igloos it together.",
        "Why couldn’t the bicycle stand up by itself? It was two tired."
    ]
    return random.choice(jokes)

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        user_input = input("Would you like to hear a joke? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            print(get_random_joke())
        elif user_input in ['no', 'n']:
            print("Alright! Have a great day!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
