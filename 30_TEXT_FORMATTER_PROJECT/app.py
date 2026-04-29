print("TEXT CAPITALIZER")

text = input("Enter some text:")
print("1. UPPERCASE")
print("2. lowercase")
print("3. Title case")
print("4. Sentence case")

choice = input("Choose a format (1-4): ")

if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())