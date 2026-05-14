def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    print("\nSIMPLE CALCULATOR")
    print("Select operation:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

    while True:
        choice = input("\nEnter choice (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4")
        else:
            break

    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
    except ValueError:
        print("Error! Please enter valid numbers!")
        return

    if choice == "1":
        print(f"\n{number1} + {number2} = {add(number1, number2)}")
    elif choice == "2":
        print(f"\n{number1} - {number2} = {subtract(number1, number2)}")
    elif choice == "3":
        print(f"\n{number1} * {number2} = {multiply(number1, number2)}")
    elif choice == "4":
        print(f"\n{number1} / {number2} = {divide(number1, number2)}")
    
    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye")
        return
    else:
        main()

main()
    