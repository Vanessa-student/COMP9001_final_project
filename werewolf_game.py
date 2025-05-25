import random
import sys

WEREWOLF = "werewolf"
SEER = "seer"
VILLAGER = "villager"
DOCTOR = "doctor"

class Player:

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.alive = True

    def kill(self) -> None:
        '*** Marks player dead***'
        self.alive = False

    def is_alive(self) -> bool:
        return self.alive

    def get_name(self) -> str:
        return self.name

    def get_role(self) -> str:
        return self.role

    def __str__(self) -> str:
        if self.alive:
            state = "Alive"
        else:
            state = "Dead"
        
        return f"{self.name} - {self.role} - {state}"

    def create_player(max_player: int = 10) -> list["Player"]:
        names = []
        print("Enter player name")
        while len(names) < max_player:
            user = input("Enter your name: ").strip()
            if user.upper() == 'END':
                break
            if not user:
                print("Name cannot be blank")
                continue
            if user.lower() in (n.lower() for n in names):
                print("Duplicate name.")
                continue

            names.append(user)
        
        if len(names) < 4:
            print("Need at least 4 players to play")

        generator = random.Random()
        generator.shuffle(names)

        n_wolves = max(1, len(names) // 5) # 20% wolves
        wolves = set(generator.sample(names, n_wolves))

        remains_wolves = [n for n in names if n not in wolves]
        seer_name = generator.choice(remains_wolves)

        remains_seer = [n for n in remains_wolves if n != seer_name]
        doctor_name = generator.choice(remains_seer)

        # Assigning player's role randomly
        players = []

        for n in names:
            if n in wolves:
                role = WEREWOLF
            elif n == seer_name:
                role = SEER
            elif n == doctor_name:
                role = DOCTOR
            else:
                role = VILLAGER

            players.append(Player(n, role))

        print(f"{len(players)} players added. Roles assigned.\n")
        return players
