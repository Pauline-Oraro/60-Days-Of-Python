import random

print("\n=== GUESS THE WORD! ===")
print("Unscramble the letters to find the word")

words = ["python", "coding", "programming", "computer", "technology", "fun", "learn"]

while True:
    original_word = random.choice(words)

    letters = list(original_word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\n Scrambled word: {scrambled}")

    guess = input("What is the word?: ").lower()

    if guess == original_word:
        print("Congrats you win")
    else:
        print(f"Sorry, the word was: {original_word}")

    again = input("Play again? (y/n): ").lower()
    if not again.startswith("y"):
        print("Goodbye")
        break