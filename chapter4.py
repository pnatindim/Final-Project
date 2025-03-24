# Patric Natindim
# Milestone 3

# Chapter 4

def chapter4(player):
    print("Chapter 4")
    print("You enter a control room with two buttons: one green and one red.")
    
    while True:
        choice = input("Do you press (1) Green button or (2) Red button? ")
        
        if choice == "1":
            print("The green button opens a door to the exit.")
            player.add_score(10)
            return "chapter5"
        elif choice == "2":
            print("The red button triggers an alarm! GAME OVER!")
            player.game_over()
            return "gameover"
        else:
            print("Choose 1 or 2.")
