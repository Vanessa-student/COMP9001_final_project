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

mkdir WerewolfGame
cd WerewolfGame
touch werewolf_game.py main.py README.md

