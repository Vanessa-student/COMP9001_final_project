import random
import sys
from werewolf_game import Player, WEREWOLF, SEER, DOCTOR

def living(players: list[Player]) -> list[Player]:
    return [p for p in players if p.is_alive()]

def counts(players: list[Player]) -> tuple[int, int]:
    wolves = sum(p.is_alive() and p.get_role() == WEREWOLF for p in players)
    villagers = sum(p.is_alive() and p.get_role() != WEREWOLF for p in players)
    return wolves, villagers

def check_win(players: list[Player]) -> str | None:
    wolves, villagers = counts(players)
    if wolves == 0:
        return "villagers"
    if wolves >= villagers:
        return "wolves"
    return None

def night_time(players: list[Player], generator: random.Random) -> None:
    wolves = [p for p in players if p.is_alive() and p.get_role() == WEREWOLF]
    doctor = next((p for p in players if p.is_alive() and p.get_role() != DOCTOR), None)
    
    protect = None
    if doctor:
        protection = random.choice(living(players))
        protect = protection.get_name()
        print(f"(Doctor secretly protects {protect}.)")

    targets = [p for p in players if p.is_alive() and p.get_role()!=WEREWOLF]
    if wolves and targets:
        victim = random.choice(targets)
        if victim.get_name() != protect:
            victim.kill()
            print(f"Night falls... the werewolves have slain {victim.get_name()}")
        else:
            print("Night passes peacefully.")

    seers = [p for p in players if p.is_alive() and p.get_role() == SEER]
    if seers:
        seer = seers[0]
        others = [p for p in players if p != seer and p.is_alive()]
        if others:
            seen = generator.choice(others)
            print(f"(The seer peers into the night and learns "
                  f"{seen.get_name()} is a {seen.get_role()}.)")

def day_time(players: list[Player]) -> None:
    print("\nDay breaks. The living souls gather:")
    print(", ".join(p.get_name() for p in living(players)))
    while True:
        choice = input("Choose someone to eliminate: ").strip()
        target = next((p for p in players if p.get_name().lower() == choice.lower()), None)
        if target is None or not target.is_alive():
            print("Invalid choice - try again.")
            continue
        target.kill()
        print(f"{target.get_name()} has been eliminated.\n")
        break

def main() -> None:
    players = Player.create_player()
    generator = random.Random()

    counting_days = 1
    winner = None

    while True:
        night_time(players, generator)
        winner = check_win(players)
        if winner:
            break

        day_time(players)
        winner = check_win(players)
        if winner:
            break

        print(f"--- End of cycle {counting_days} ---\n")
        counting_days += 1

    print(f"Game over - {winner.capitalize()} win!")

if __name__ == "__main__":
    main()
