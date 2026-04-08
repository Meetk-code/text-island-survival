from player import Player
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

you = Player(100, 100, 100)

day = 1
t_days = 2
choices = 5
options = ["hunt", "eat", "drink", "sleep"]
running = True

while day <= t_days:
    print(f"Day: {day}\n")
    for I in range(choices):
        print(f"\nActions remaining : {choices - I}")
        while True:
            print("options are:")
            for I in options:
                print(f"--> {I}")
            choice = input("_____________________________\nWhat do you wanna do---> ")
            if choice in options:
                you.action(choice)
                break
            else:
                print("Not valid")
                
        if you.hunger < 1 or you.water < 1 or you.energy < 1:
             break
        you.status()
        input()
        clear()
    day += 1
    if you.hunger < 1 or you.water < 1 or you.energy < 1:
                 break
    you.status()   
    input()
    clear()
   
        
print("You survived!" if day == t_days + 1 else "You Die")
