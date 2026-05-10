print("COLOR MIXER")

color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
    ("white", "blue"): "light blue",
    ("white", "yellow"): "cream",
    ("white", "green"): "mint",
    ("white", "purple"): "lavender",
    ("white", "orange"): "peach",
    ("white", "black"): "gray",
    ("black", "red"): "maroon",
    ("black", "blue"): "navy",
    ("black", "yellow"): "olive",
    ("black", "green"): "dark green",
    ("black", "orange"): "brown",
    ("black", "purple"): "dark purple",
    ("red", "orange"): "vermillion",
    ("yellow", "green"): "chartreuse",
    ("blue", "purple"): "indigo",
    ("orange", "yellow"): "amber",
    ("orange", "red"): "scarlet",
    ("pink", "purple"): "mauve",
    ("pink", "orange"): "salmon",
    ("yellow", "purple"): "muddy brown",
    ("orange", "blue"): "slate gray",
}

while True:
    color1 = input("\nEnter first color: ").lower().strip()
    color2 = input("Enter second color: ").lower().strip()

    mix = None

    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    elif(color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]

    if mix:
        print(f"When you mix {color1} and {color2}, you get {mix}!")
    else:
        print("I don't know what those colors make when mixed")

    if not input("\nMix more colors? (y/n): ").lower().startswith("y"):
        print("Goodbye")
        break