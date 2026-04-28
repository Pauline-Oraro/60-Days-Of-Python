print("STEP COUNTER")

daily_goal = int(input("What is your daily step goal?"))
current_steps = int(input("How many steps have you taken today?"))

remaining_steps = daily_goal - current_steps

if remaining_steps > 0 :
    print(f" You need {remaining_steps} more steps to reach your goal!")
else:
    print(f"Congratulations! You have exceeded your goal by {-remaining_steps} steps!")

# This code is a simple step counter application that prompts the user for their daily step goal and the number of steps they have taken so far. It then calculates the remaining steps needed to reach the goal and provides feedback to the user. If the user has exceeded their goal, it congratulates them and shows how many steps they have exceeded by.

# The code uses basic input and output functions, as well as conditional statements to determine the appropriate message to display based on the user's input.

#The output of the code will depend on the user's input for the daily step goal and the current steps taken. For example, if the user sets a daily goal of 10,000 steps and has taken 7,500 steps, the output will be:
# "You need 2500 more steps to reach your goal!"
# If the user has taken 12,000 steps, the output will be:
# "Congratulations! You have exceeded your goal by 2000 steps!"