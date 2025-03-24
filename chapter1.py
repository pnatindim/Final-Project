# Patric Natindim
# Milestone 3

# Chapter 1

def chapter1(player):
    print(f"Chapter 1 -- Welcome, {player.name}!")
    print("You wake up in a glowing room. Three doors appear in front of you.")
    
    while True:
        choice = input("Choose a door (1, 2, or 3): ")
        
        if choice == "1":
            print("You open Door 1 and step into a hallway of floating platforms.")
            player.add_score(10)
            return "chapter2"
        elif choice == "2":
            print("You open Door 2 and find a terminal room.")
            player.add_score(10)
            return "chapter3"
        elif choice == "3":
            print("You open Door 3 and fall through a trap door. GAME OVER!")
            player.game_over()
            return "gameover"
        else:
            print("Please select 1, 2, or 3.")
