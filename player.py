import random
import foods

inv = {}

# Main class-Player
class Player:
    def __init__(self, hunger, water, energy):
        self.hunger = hunger
        self.water = water
        self.energy = energy
        
  # Actions
  
      #Inventory            
    def inventory(self, item):
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
            
        #Hunt
    def hunt(self):
        a = list(foods.fish.keys())
        try:
            if list(inv.keys())[0] == list(foods.fish.keys())[0]:
                b = 0
            elif list(inv.keys())[0] == list(foods.fish.keys())[1]:
                b = 1
            else:
                b = 2
        except:
                pass
        self.inventory(random.choice(a))
        self.hunger -= 10
        self.energy -= 30
        
        #Drink
    def drink(self):
        self.water += 10
        self.energy -= 5
        
        #eat
    def eat(self):
        a = list(foods.fish.keys())
        try:
            if list(inv.keys())[0] == list(foods.fish.keys())[0]:
                b = 0
            elif list(inv.keys())[0] == list(foods.fish.keys())[1]:
                b = 1
            else:
                b = 2
        except:
                pass
        if inv:
            self.hunger += foods.fish[a[b]]
            print(inv[a[b]])
            if inv[a[b]] > 0 and not inv[a[b]] == "":
                inv[a[b]] -= 1
            if inv[a[b]] == 0:
                del inv[a[b]]
        else:
            print("No food")
            
            #sleep
    def sleep(self):
            self.energy+=50
            
 #Actions Selection           
    def action(self, action):
        
        

        if action == "hunt":
            self.hunt()
            
        elif action == "eat":
            self.eat()
            
        elif action == "drink":
            self.drink()
            
        elif action == "sleep":
            self.sleep()
            
        else:
            print("enter a valid choice")
        
    def status(self, cmd=""):
        if cmd == "inv":
            for k, v in inv.items():
                print(k, v)
        else:
            print(f"_____________________________\nStatus:\n\nYou have {self.hunger} hunger!\nYou have {self.water} water!\nYou have {self.energy} energy!")
            print("\nInventory:\n")
            for k, v in inv.items():
                print(k, v)