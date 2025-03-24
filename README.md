Simulation Escape Game
Technical Documentation

Where the Code Is Hosted
GitHub Repository:  
https://github.com/YourUsername/SciFi-Virtual-Escape (Replace with your actual GitHub link)

Languages and Technologies
- Python 3.10+
- Standard Python libraries:
  - random

System Requirements and Supported Applications
OS:
- Windows 10/11
- MacOS
- Linux

Python Version:
- Python 3.10 or later recommended

Hardware:
- Anything capable of running Python 3

IDE/Editor (Optional):
- Visual Studio Code
- PyCharm
- Basic text editor 

Coding / Naming Conventions
Language: English

Variables and Functions:
- snake_case naming (ex. chapter1(), add_score())

Class Names:
- PascalCase naming (ex. Player)

How to Run / Build / Deploy the Program
Running the game:
- Install Python 3.10+
- Clone or download the repository from GitHub  
- Navigate to the project folder
- Run the program

Overview of the Architecture
Structure:
- Player Class:
  - Stores player information (name, alive status, score)
- Chapter Functions:
  - chapter1(player) - chapter5(player)
  - Handle the player’s decision-making and game flow
- Mini-Game:
  - hack_terminal(player) in Chapter 3
- Game Over and Restart:
  - gameover(player)
- Main Game Loop:
  - Controls the flow of the game
  - Starts with main_game()

main_game() - chapter1 - chapter2/3 - chapter4 - chapter5 - gameover


How to Start the Program (Start the Game)
After running the game in your terminal:  
python game.py

The program starts with a welcome message and prompts for the player’s name.  
You navigate through the chapters by entering numbers based on the choices you make.  
The goal is to escape the simulation before the system shuts down.
