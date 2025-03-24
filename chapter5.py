# Patric Natindim
# Milestone 3

# Chapter 5

def chapter5(player):
    print("Chapter 5")
    print("You stand before a bright light. This is the exit.")
    
    while True:
        choice = input("Do you (1) Step into the light or (2) Celebrate? ")
        
        if choice == "1":
            print("You step into the light and escape! YOU WIN!")
            player.add_score(50)
            return "endgame"
        elif choice == "2":
            print("Your celebration took too long. The system shuts down. GAME OVER!")
            player.game_over()
            return "gameover"
        else:
            print("Choose 1 or 2.")
