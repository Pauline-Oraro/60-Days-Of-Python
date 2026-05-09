import random

print("COIN FLIP GAME")
print("Guess heads or tails")

while True:
    guess = input("\nEnter your guess (heads/tails): ").lower()

    if guess != "heads" and guess != "tails":
        print("Please enter 'heads' or 'tails' ")
        continue

    flip = random.choice(["heads", "tails"])

    print(f"\n Coin shows {flip}")

    if guess == flip:
        print("You won, you guessed correctly")
    else:
        print("Sorry, wrong guess, try again")

    again = input("\nPlay again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye")
        break