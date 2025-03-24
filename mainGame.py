# Patric Natindim

# Main Game

from player import Player
from chapter1 import chapter1
from chapter2 import chapter2
from chapter3 import chapter3
from chapter4 import chapter4
from chapter5 import chapter5
from gameover import gameover

def main_game():
    print("Welcome to the simulation. Can you escape?")
    name = input("Enter your name to begin: ")
    player = Player(name)

    current_chapter = "chapter1"
    
    while current_chapter != "exit" and player.alive:
        if current_chapter == "chapter1":
            current_chapter = chapter1(player)
        elif current_chapter == "chapter2":
            current_chapter = chapter2(player)
        elif current_chapter == "chapter3":
            current_chapter = chapter3(player)
        elif current_chapter == "chapter4":
            current_chapter = chapter4(player)
        elif current_chapter == "chapter5":
            current_chapter = chapter5(player)
        elif current_chapter == "gameover":
            current_chapter = gameover(player)
        elif current_chapter == "endgame":
            print(f"\nCongratulations, {player.name}! You escaped the simulation!")
            print(f"Final Score: {player.score}")
            break

# Start game
main_game()
