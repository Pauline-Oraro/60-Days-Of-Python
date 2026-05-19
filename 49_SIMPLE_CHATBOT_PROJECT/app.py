import random
import time

def chatbot():
    greetings = ["Hello there! 👋", "Hi friend! ☺️",
                "Hey! Nice to meet you! 🎉", "Howdy! 😃"]
    farewells = ["Goodbye! 👋", "See you later! 🚀",
                "Bye bye! 😊", "Until next time! ✨"]
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 🤣",
        "What do you call a fake noodle? An impasta! 🍝",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
        "What do you call a bear with no teeth? A gummy bear! 🐻"
    ]
    facts = [
        "Honey never spoils! Archaeologists found 3000-year-old honey that's still good! 🍯",
        "Octopuses have three hearts! 🐙",
        "A day on Venus is longer than a year on Venus! ☀️",
        "The Hawaiian alphabet has only 12 letters! 🏝️"
    ]

    bot_name = "ChatBot"
    print(f"{bot_name}: is starting up...")
    time.sleep(1)

    print(f"""
        Welcome to {bot_name}! 
        I can chat about:
        'joke' - Hear a funny joke
        'fact' - Learn something new
        'color' - My favorite color
        'bye' - End our chat
        """)
    chatting = True
    user_name = input("What is your name: ").lower().strip()
    print(f"{bot_name}: Nice to meet you, {user_name}! How can I help you today?")

    while chatting:
        user_input = input("You: ").strip()

        if user_input in ["hi","hello","hey","howdy"]:
            print(f"{bot_name}: {random.choice(greetings)}")

        elif "joke" in user_input:
            print(f"{bot_name}: {random.choice(jokes)}")

        elif "fact" in user_input:
            print(f"{bot_name}: {random.choice(facts)}")

        elif "color" in user_input:
            print(f"{bot_name}: My favourite color is robot blue! What's yours?")
            color = input("You:").strip()
            print(f"{bot_name}: {color} is a great color!")
            
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"{bot_name}: It was fun chatting with you, {user_name}")
            chatting = False

        else:
            responses = [
                "That's interesting! Tell me more.",
                "I'm not sure I understand. Can you try again?",
                "Hmm, let's talk about something else. Try asking for a joke or fact!",
                "Beep boop! My robot brain is processing that... 🤔"
            ]
            print(f"{bot_name}: {random.choice(responses)}")
    print("Thanks for chatting! Run the program again to talk to me later! 👋")

chatbot()