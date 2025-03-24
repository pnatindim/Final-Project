# Patric Natindim
# Milestone 3

# Game Over

def gameover(player):
    print("GAME OVER")
    
    choice = input("Would you like to restart? (y/n): ")
    if choice.lower() == "y":
        player.alive = True
        player.score = 0
        return "chapter1"
    else:
        print("Thanks for playing!")
        return "exit"
