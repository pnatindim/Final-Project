import random

def hackTerminal(player):
    print("Hacking the Terminal")
    print("You access the terminal. You need to guess the correct passcode (1-5).")
    
    passcode = random.randint(1, 5)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess (attempts left: {attempts}): "))
            
            if guess == passcode:
                print("Access Granted! The door unlocks.")
                player.add_score(20)
                return True
            else:
                print("Access Denied.")
                attempts -= 1
        
        except ValueError:
            print("Enter a valid number (1-5).")

    print("Too many failed attempts! The terminal locks you out.")
    player.game_over()
    return False
