from player import Player
import os

# Clear shortcut as a function
def clear():
    input()
    os.system("cls" if os.name == "nt" else "clear")

# Main Player
you = Player(100, 100, 100)

# Constant Variables
day = 1
t_days = 2
choices = 5
options = ["hunt", "eat", "drink", "sleep"]
running = True
alive = True

# Functions 
def display_options(left):
    print(f"\nActions remaining : {choices - left}")
    print("options are:")
    for I in options:
        print(f"--> {I}")

def get_choice():
    while True:
        choice = input("_____________________________\nWhat do you wanna do---> ")
        if choice in options:
            you.action(choice)
            break
        
        else:
            print("Not valid, Retry!")

# Main Game Loop
while day <= t_days and alive:
       print(f"Day: {day}\n")
       for I in range(choices):
        display_options(I)
        get_choice()
        you.status()
        if you.hunger < 1 or you.water < 1 or you.energy < 1:
            alive = False
        clear()
       day+=1
print("You survived!" if alive else "You Die")
