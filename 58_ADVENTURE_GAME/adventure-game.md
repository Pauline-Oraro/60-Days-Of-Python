# 🌲 Forest Adventure

A terminal-based text adventure game written in Python where you explore a forest, battle enemies, collect treasure, and manage your resources to survive.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Run](#how-to-run)
- [Gameplay](#gameplay)
  - [Starting the Game](#starting-the-game)
  - [Locations](#locations)
  - [Combat](#combat)
  - [Items & Shop](#items--shop)
- [Game Mechanics](#game-mechanics)
  - [Stats](#stats)
  - [Enemies](#enemies)
  - [Random Encounters](#random-encounters)
- [Project Structure](#project-structure)

---

## Overview

Forest Adventure is a single-player, turn-based RPG that runs entirely in the terminal. You take on the role of an adventurer starting in a small town with 100 health and 50 gold. Your goal is to explore the forest, defeat enemies, loot treasure, and grow strong enough to survive whatever the wilderness throws at you.

---

## Features

- 🗺️ **Multiple locations** — Town, Forest, and Shop, each with unique actions
- ⚔️ **Turn-based combat** — Fight enemies, use potions, or attempt to flee
- 🛒 **Shop system** — Buy items to boost your survivability and damage output
- 🎲 **Random encounters** — Every forest exploration has a chance of battle, treasure, or nothing
- 💀 **Game Over & Replay** — Die and choose to start fresh without restarting the script
- 🖨️ **Typewriter text effect** — Atmospheric character-by-character printing for immersion

---

## How to Run

1. **Clone or download** the script to your local machine.

2. **Open a terminal** and navigate to the directory containing the file:
   ```bash
   cd path/to/your/folder
   ```

3. **Run the script:**
   ```bash
   python forest_adventure.py
   ```

4. Enter your adventurer's name when prompted and the game begins!

---

## Gameplay

### Starting the Game

When the game launches, you are prompted to enter your name. You then begin in the **Town** with the following starting stats:

| Stat   | Starting Value |
|--------|---------------|
| Health | 100           |
| Gold   | 50            |
| Items  | None          |

---

### Locations

#### 🏘️ Town

The central hub of the game. From here you can:

- Visit the **Shop** to buy items
- Enter the **Forest** to explore and fight
- **Rest at the inn** to fully restore health (costs 10 gold)
- **Quit** the game

#### 🌲 Forest

A dangerous area where encounters happen. From here you can:

- **Explore deeper** — triggers a random encounter (enemy, treasure, or nothing)
- **Set up camp** — restores 10 health for free
- **Return to town**

#### 🛒 Shop

A store run by a friendly shopkeeper. Available for purchase:

- **Health Potion** — 20 gold
- **Sword** — 50 gold
- **Return to town**

---

### Combat

When you encounter an enemy, a turn-based battle begins. Each turn you can:

1. **Attack** — Deal damage to the enemy. Base damage is **5**; equipping a sword adds **+10** damage (15 total).
2. **Use Health Potion** — Restore **30 health** (only if you have one in your inventory). The enemy still attacks you on this turn.
3. **Run Away** — 50% chance to escape successfully. On failure, the enemy deals damage.

After your action (if you don't run), the enemy attacks you. If your health drops to **0 or below**, the game ends.

Defeating an enemy rewards you with gold.

---

### Items & Shop

| Item          | Cost    | Effect                          | Notes                              |
|---------------|---------|---------------------------------|------------------------------------|
| Health Potion | 20 gold | Restores 30 health when used    | Consumed on use; can hold only one |
| Sword         | 50 gold | +10 damage per attack           | Permanent; can only be bought once |

Health potions can also be found inside treasure chests in the forest.

---

## Game Mechanics

### Stats

- **Health** — Starts at 100, capped at 100. Reaches 0 → Game Over.
- **Gold** — Currency for the shop and inn. Earned by defeating enemies and finding treasure.
- **Items** — Inventory list displayed in the HUD. Currently supports Health Potion and Sword.

---

### Enemies

Three enemy types can be encountered in the forest:

| Enemy  | Health | Damage per Turn | Gold Reward |
|--------|--------|-----------------|-------------|
| Goblin | 30     | 5               | 15 gold     |
| Wolf   | 20     | 7               | 10 gold     |
| Bandit | 40     | 8               | 25 gold     |

Enemies are selected randomly at the start of each encounter.

---

### Random Encounters

Each time you **Explore** the forest, the outcome is determined by weighted probability:

| Outcome  | Probability |
|----------|-------------|
| Enemy    | 60%         |
| Treasure | 30%         |
| Nothing  | 10%         |

**Treasure** rewards you with 10–30 random gold. There is also a **20% chance** the chest contains a free Health Potion (only if you don't already have one).

---

## Project Structure

```
forest_adventure.py
│
├── player            # Dict storing player name, health, gold, and items
├── locations         # Dict describing each location and its available options
├── items             # Dict of purchasable/usable items and their stats
├── enemies           # List of enemy dicts with health, damage, and gold values
│
├── slow_print()          # Prints text character-by-character for atmosphere
├── display_stats()       # Prints the player's current HUD
├── start_game()          # Initialises player state and starts the game loop
├── town()                # Main town loop and navigation hub
├── shop()                # Shop browsing and purchase loop
├── buy_item()            # Handles item purchasing logic
├── forest()              # Forest navigation loop
├── explore()             # Triggers a random encounter
├── enemy_encounter()     # Full combat loop against a random enemy
├── treasure_encounter()  # Handles treasure chest rewards
├── rest()                # Inn rest logic (costs 10 gold, full health restore)
└── game_over()           # Handles death, displays final stats, prompts replay
```
