print("VOWEL COUNTER")

while True:
    text = input("\nEnter some text (or quit): ")

    if text.lower() == "quit":
        print("Goodbye")
        break

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels!")