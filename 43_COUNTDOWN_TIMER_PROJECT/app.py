import time

print("\n=== COUNTDOWN TIMER ====")
print("Count down from your chosen seconds!")

while True:
    try:
        seconds = int(input("\nEnter seconds to countdown from:"))

        if seconds <=0:
            print("Please enter a positive number.")
            continue

        print(f"Starting countdown from {seconds} seconds!")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("\nCOUNTDOWN COMPLETE!")

        again = input("\nStart another countdown? (yes/no): ").lower()
        if not again.startswith("y"):
            print("Goodbye!")
            break
    except ValueError:
        print("Please enter a number.")