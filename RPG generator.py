#RPG NPC generator
from random import randint

class_list = ["Mage", "Asassin", "Necromancer", "Soldier", "Gladiator", "Farmer", "Merchant", "Priest"]
Strength = 0
Magic = 0
Agility = 0
Block = 0
name_list  = ["John ", "David ", "Old man ", "Harry ", "Jeffrey ", "Alex ", "Joe ", "Alfred ", "Barry "]
surname_list = ["Smith", "Crow", "Hill", "Farmer", "Johnsson", "Franksson"]

#Name Generation
name1 = randint(0, 8)
name2 = randint(0, 5)
name = name_list[name1] + surname_list[name2]

#Class Selection
class_selection = randint(0,7)
player_class = class_list[class_selection]

#Strength Selection
if player_class == "Mage":
    Strength = randint(1, 25)
elif player_class == "Asassin":
    Strength = randint(30, 96)
elif player_class == "Necromancer":
    Strength = randint(0, 10)
elif player_class == "Soldier":
    Strength = randint(57, 82)
elif player_class == "Gladiator":
    Strength = randint(30, 65)
elif player_class == "Farmer":
    Strength = randint(3, 30)
elif player_class == "Merchant":
    Strength = randint(1, 15)
elif player_class == "Priest":
    Strength = randint(6, 23)

#Magic Selection
if player_class == "Mage":
    Magic = randint(50, 70)
elif player_class == "Asassin":
    Magic = randint(4, 30)
elif player_class == "Necromancer":
    Magic = randint(70, 84)
elif player_class == "Soldier":
    Magic = randint(0, 23)
elif player_class == "Gladiator":
    Magic = randint(0, 50)
elif player_class == "Farmer":
    Magic = randint(0, 40)
elif player_class == "Merchant":
    Magic = randint(0, 20)
elif player_class == "Priest":
    Magic = randint(0, 99)

#Agility Selection
if player_class == "Mage":
    Agility = randint(5, 37)
elif player_class == "Asassin":
    Agility = randint(60, 99)
elif player_class == "Necromancer":
    Agility = randint(1, 10)
elif player_class == "Soldier":
    Agility = randint(30, 50)
elif player_class == "Gladiator":
    Agility = randint(70, 75)
elif player_class == "Farmer":
    Agility = randint(13, 40)
elif player_class == "Merchant":
    Agility = randint(5, 30)
elif player_class == "Priest":
    Agility = randint(1, 16)

#Block Chance Selection
if player_class == "Mage":
    Block = randint(0, 40)
elif player_class == "Asassin":
    Block = randint(30, 70)
elif player_class == "Necromancer":
    Block = randint(0, 26)
elif player_class == "Soldier":
    Block = randint(70, 92)
elif player_class == "Gladiator":
    Block = randint(50, 80)
elif player_class == "Farmer":
    Block = randint(20, 50)
elif player_class == "Merchant":
    Block = randint(1, 5)
elif player_class == "Priest":
    Block = randint(0, 17)

#Extras
if player_class == "Necromancer":
    necro = randint(1, 4)
    if necro == 1:
        hasNecromancy = True
    else:
        hasNecromancy = False
elif player_class == "Merchant":
    trading = randint(1, 2)
    if trading ==  1:
        hasTrades = True
    else:
        hasTrades = False
print("Name: " + name)
print("Class: " + player_class)
print("Strength: " + str(Strength))
print("Magic: " + str(Magic))
print("Agility: " + str(Agility))
print("Block Chance: " + str(Block))
