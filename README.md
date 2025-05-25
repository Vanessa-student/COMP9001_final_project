# Werewolf Game 

A one-command setup, secretly shuffled roles, and tense day-night turns with non-stop suspicion. It is an intuitive and challenging game activating player's psychology to outsmart friends and win in the group-based game.

# Features

- Add a new game session with interactive player entry (type END to finish).
- Automatic random role assignment (≈20 % Werewolves, exactly 1 Seer, 1 Doctor, rest Villagers).
- Night-time phase:
  - Werewolves choose a victim.
  - Doctor secretly protects one player.
  - Seer receives a private revelation about another player’s role.
- Day-time phase:
  - All living players vote to eliminate a suspect.
- Win-condition checks after every night and day cycle (Villagers win if no Werewolves remain; Werewolves win once they equal or outnumber Villagers).
- Clear console output showing phase changes, deaths, protections and end-game result.
- Basic input validation (prevents blank or duplicate names and invalid votes).

# Project Structures

```text
WerewolfGame/
├── werewolf_game.py   # Player class, role constants, and core helper functions
├── main.py            # Entry point running the night/day game loop
└── README.md          # Project documentation
```

# How to run

1. Save werewolf_game.py and main.py
2. Run the following command in your terminal:

```text
python3 Run.py
```
# Demo

```text
Enter player name
Enter your name: Alice
Enter your name: Bob
Enter your name: Carol
Enter your name: Dave
Enter your name: END
4 players added. Roles assigned.

Night falls...
(Doctor secretly protects Carol.)
(The seer peers into the night and learns Bob is a werewolf.)
The werewolves have slain Alice

Day breaks. The living souls gather:
Bob, Carol, Dave
Choose someone to eliminate: Bob
Bob has been eliminated.

--- End of cycle 1 ---

Night falls...
Night passes peacefully.

Day breaks. The living souls gather:
Carol, Dave
Choose someone to eliminate: Dave
Dave has been eliminated.

Game over - Villagers win!

```
Perfect to build intuitive thoughts while having fun with friends

