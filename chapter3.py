# Patric Natindim
# Milestone 3

# Chapter 3

from hackTerminal import hackTerminal

def chapter3(player):
    print("Chapter 3")
    print("You find a computer terminal.")

    choice = input("Do you (1) Hack the terminal or (2) Ignore it? ")

    if choice == "1":
        success = hackTerminal(player)
        if success:
            return "chapter4"
        else:
            print("GAME OVER!")
            return "gameover"
    elif choice == "2":
        print("You ignore the terminal. Fool. You needed it to escape. GAME OVER!")
        player.game_over()
        return "gameover"
    else:
        print("Invalid choice. Returning to menu.")
        return "chapter3"
