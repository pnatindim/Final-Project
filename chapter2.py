# Patric Natindim
# Milestone 3

# Chapter 2

def chapter2(player):
    print("Chapter 2")
    print("You enter a hallway filled with floating platforms.")
    
    while True:
        choice = input("Do you (1) Jump or (2) Sprint? ")
        
        if choice == "1":
            print("You carefully jump across the platforms and make it safely.")
            player.add_score(10)
            return "chapter4"
        elif choice == "2":
            print("You ran too fast and fell through! GAME OVER!")
            player.game_over()
            return "gameover"
        else:
            print("Choose 1 or 2.")
