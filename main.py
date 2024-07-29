import random
phealth = 5 #This variable stores the players health
dhealth = 0 #This variable stores the dragon's health
foodcount = 5 #This variable sores the amount of food the player has
turn = 0 #This variable stores what turn the player is on
move = "y" #This variable asks if the player wants to move
dragchance = 0 #This variable is the chance of a dragon spawning
foodchance = 0 #This variable is the chance of food spawning
def playerhealth(damage,health): #This method calculates the players health 
  health = health-damage
  return health
def eating(food,health): #This method calculates the amount of food and the players health after eating
  food = food-1
  heal = random.randrange(1,5)
  heal = heal*(-1)
  health = playerhealth(heal,health)
  print ("You have",health,"health")
  print ("You have",food,"food")
  return food,health
def attack(dragonhealth): #This method calculates the dragon's health after the player attacks
  attack = random.randrange(1,4)
  dragonhealth = dragonhealth-attack
  print("The dragon has",dragonhealth,"health") 
  return dragonhealth
def dragonattack(health): #This method calculates the player's health after the dragon attacks
  attack = random.randrange(1,3)
  health = playerhealth(attack,health)
  print("You have",health,"health")
  return health
def startfight(): #This method starts the fight with a dragon
  dragonhealth=random.randrange(5,7)
  print("A dragon has been found with",dragonhealth,"health")
  return dragonhealth
def found(food): #This method calculates the food amount after the player finds food
  found=random.randrange(1,3)
  food = food+found
  print("You found",found,"food")
  return food
def fight(dragonhealth,food,playerhealth): #This method deals with the players choices during a fight
  playerchoice=int(input("Enter 1 to attack and 2 to eat\n"))
  if (playerchoice == 1):
    dragonhealth = attack(dragonhealth)
  elif (playerchoice == 2):
    food,playerhealth = eating(food,playerhealth)
  return dragonhealth,food,playerhealth

print("Welcome to Dragon Slayer where you, the golden knight, will have to get from one city to another without dying!")
while (move!="no") and (phealth>0) and (turn<20):
  move = input("Do you want to move? yes to move, no to end the game\n")
  if (move == "yes"):
    turn = turn+1
    print("You have",phealth,"health")
    print("You have",foodcount,"food")
    print("You have",20-turn,"turns left")
    dragchance = random.randrange(1,10)
    foodchance = random.randrange(1,10)
    if (dragchance > 7):
      dhealth = startfight()
      dhealth,foodcount,phealth = fight(dhealth,foodcount,phealth)
      phealth = dragonattack(phealth)
      while (dhealth>0) and (phealth>0):
        dhealth,foodcount,phealth = fight(dhealth,foodcount,phealth)
        phealth = dragonattack(phealth)
      if (dhealth<=0):
        print("You defeated the dragon!")
    if (foodchance > 6):
      foodcount = found(foodcount)
if (move == "no") or (phealth<=0):
  print("Game Over")
elif (turn>=20) and (phealth>0):
  print("You made it to the other city!")