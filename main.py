try:
  import random
  import sys
  import os

#Character creation
  class Character:
    def __init__(self, name, health):
      self.name = name
      self.health = health

  name = input("Please enter your name:\n") #User is asked to enter their name to create their character
  p1 = Character(name, 50)
  p2 = Character("Donovan", 80) #Boss/Enemy

#Defining Weapon Class
  class Weapon:
    def __init__(self, name, DMG):
      self.name = name
      self.DMG = DMG
#Weapons available in game
  w1 = Weapon("Colt M1911", 20)
  w2 = Weapon("Ice Pick", 10)
  w3 = Weapon("The Thompson 1928", 30)

  weapons = [w1, w2, w3]
  player_previous_weapon = ['1']
  boss_previous_weapon = ['1']

#Attacking function for player
  def player_attack(self, target):
    print('''Choose a weapon:
  (1) Colt M1911 -> DMG: 20 SPD: 20
  (2) Ice Pick -> DMG: 10 SPD: 30
  (3) The Thompson 1928 -> DMG: 30 SPD: 10''')
    choice = input("Which weapon would you like to use?") #The player chooses which weapon to use
    if choice == '1': #Colt M1911
      damage = weapons[0].DMG
      target.health -= damage
      print(p2.name + " took " + str(damage) + " damage.")
      player_previous_weapon.append('w1')
    elif choice == '2': #In the event of using the ice pick, the user is prompted to use another weapon as a bonus.
      damage = weapons[1].DMG
      another = input("Choose another weapon:")
      if another == '1':
        damage += weapons[0].DMG
      elif another =='2':
        damage += weapons[1].DMG
      elif another == '3': #I wanted to add some unfair properties in this game. If you decide to use The Thompson, it's not possible.
        print("You can't use this weapon. You have squandered your opportunity to deal more damage.")
      else:
        print("You have squandered your opportunity to deal more damage.")
      target.health -= damage
      print(p2.name + " took " + str(damage) + " damage.")
      player_previous_weapon.append('w2')
    elif choice == '3': #The Thompson 1928
      damage = weapons[2].DMG
      target.health -= damage 
      player_previous_weapon.append('w3')
      print(p2.name + " took " + str(damage) + " damage.")
    else:
      while not 0 <= int(choice) < 3: #If the user doesn't input one of the values above, it will repeat.
        print('''Choose a weapon:
  (1) Colt M1911 -> DMG: 20 SPD: 20
  (2) Ice Pick -> DMG: 10 SPD: 30
  (3) The Thompson 1928 -> DMG: 30 SPD: 10''')
        choice = input("Which weapon would you like to use?")
        if choice == '1':
          damage = weapons[0].DMG
          target.health -= damage
          print(p2.name + " took " + str(weapons[0].DMG) + " damage.")
        elif choice == '2':
          damage = weapons[1].DMG
          another = input("Choose another weapon:")
          if another == '1':
            damage += weapons[0].DMG
          elif another =='2':
            damage += weapons[1].DMG
          elif another == '3':
            print("You cannot use this weapon. You have squandered your opportunity to deal more damage.")
          else:
            print("You have squandered your opportunity to deal more damage.")
          target.health -= damage
          print(p2.name + " took " + str(damage) + " damage.")
          player_previous_weapon.append('w2')
        elif choice == '3':
          damage = weapons[2].DMG
          target.health -= damage
          print(p2.name + " took " + str(weapons[2].DMG) + " damage.")
          player_previous_weapon.append('w3')

#Attacking function for boss
  def boss_attack(self, target):
    choice = random.randint(0,3) #Since the opponent is an AI, it will randomly choose a value from 0 to 2. Below is the possible amount of damage it will deal.
    if choice == 0: #Colt M1911
      damage = weapons[0].DMG 
      target.health -= damage
      print(p1.name + " took " + str(weapons[0].DMG) + " damage.")
      boss_previous_weapon.append('w1')
    elif choice == 1: #Ice Pick
      damage = weapons[1].DMG
      another = random.randint(0,3)
      if another == 1:
        damage += weapons[0].DMG
      elif another == 2:
        damage += weapons[1].DMG
      elif another == 3:
        damage += weapons[2].DMG
      target.health -= damage
      print(p1.name + " took " + str(weapons[1].DMG) + " damage.")
      boss_previous_weapon.append('w2')
    else: #The Thompson 1928
      damage = weapons[2].DMG
      target.health -= damage
      print(p1.name + " took " + str(weapons[2].DMG) + " damage.")
      boss_previous_weapon.append('w3')

#Player's turn
  def player_turn():
    if player_previous_weapon[-1] == 'w3':
      boss_attack(p2,p1)
      player_previous_weapon.append('w1')
    elif player_previous_weapon[-1] == 'w2':
      player_previous_weapon.append('w1')
      player_attack(p1,p2)
    else:
      player_attack(p1,p2)
      random_voice()
      player_previous_weapon.append('w1')

#Boss' turn     
  def boss_turn():
    if boss_previous_weapon[-1] == 'w3':
      player_attack(p1,p2)
    elif boss_previous_weapon[-1] == 'w2':
      boss_previous_weapon.append('w1')
      boss_attack(p2,p1)
    else:
      boss_attack(p2,p1)
      boss_previous_weapon.append('w1')

#Voiceline randomizer
  def random_voice():
    voiceline = random.randint(0,3)
    if voiceline == 0:
      print("Your wife made you soft.")
    elif voiceline == 1:
      print("Our father would be disappointed...")
    else:
      print("This wouldn't happen if you stayed in the Mafia.")

#Encounter function
  def battle():
    turn = random.randint(0,2)
    if turn == 0:
      player_turn()
      boss_turn
    else:
      player_turn()
      boss_turn()

  def encounter():
    while p1.health > 0 or p2.health > 0: #While either character's health is over 0, the game will continue.
      battle()
      print(p1.name + "\'s" + " health: " + str(p1.health))
      print(p2.name + "\'s" + " health: " + str(p2.health))
      if p1.health <= 0:
        os.system('clear')
        print("You have died")
        print("Donovan: You should have ran while you had the chance.")
        sys.exit()
      elif p2.health <= 0:
        os.system('clear')
        print("You won!")
        print("Donovan: " + name +", all I wanted was us to be united again.")
        sys.exit()
    
    
#Clears out console
  os.system('clear')

#Backstory (plot)
  print("""You are the son of a former Mafia boss, but decided to leave the world of crime for a normal life. \nAfter working in stocks for a couple of years, you meet the love of your life and marry soon after.\nOne day, you come back home from work to discover your wife dead and a note on the counter. \nYour older brother, who is now the current Mafia boss, disapproved of your decision to leave the gang and is forcing you to come back. \nAs a result, you seek out vengeance to destroy the Mafia by killing your brother.""")

  answer1 = input("(1) Continue:\n(2) Exit:\nWhat would you like to do?\n")
  if answer1 == '1':
    os.system('clear')
    encounter()
  elif answer1 == '2':
    os.system('clear')
    print("You have exited the game.")
  else: #If the user inputs a value that is not 1 or 2, the player will be asked again.
    print("Invalid input, please try again.")
    answer1 = input("(1) Continue:\n(2) Exit:\nWhat would you like to do?\n")
    if answer1 == '1':
      os.system('clear')
      encounter()
    elif answer1 == '2':
      os.system('clear')
      print("You have exited the game.")
    else:
      sys.exit()
except:
  pass