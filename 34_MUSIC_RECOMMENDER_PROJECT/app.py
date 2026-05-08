import random

print("MUSIC RECOMMENDER")

genres = {
    "Pop":["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
    "Hip Hop":["Kendrick Lamar", "Drake", "J. Cole"],
    "R&B":["SZA", "The Weeknd", "Usher"],
    "Gospel":["Kirk Franklin", "CeCe Winans", "Maverick City Music"],
    "Jazz":["Miles Davis", "Louis Armstrong", "Nina Simone"],
    "Reggae":["Bob Marley", "Sean Paul", "Shaggy"],
    "Afrobeats":["Burna Boy", "Wizkid", "Tems"],
    "Amapiano":["Kabza De Small", "DJ Maphorisa", "Tyler ICU"]
}

choice = input("What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano):")

if choice not in genres:
    print("Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")   