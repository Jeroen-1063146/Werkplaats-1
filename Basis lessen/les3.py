# simple python game

import random
player = input("Welkom! Wat is je naam? ")
confirm = input("Ben je zeker dat je " + player + " heet? (ja/nee) ")

boot = random.randint(1, 10)

if confirm == "ja":
    print("Ok, " + player + ", ik heb een getal tussen 1 en 10 in mijn hoofd.")
    guess = int(input("Raad je het getal? "))
    if guess == boot:
        print("Goed geraden, " + player + "!")
    else:
        print("Helaas, je hebt het fout. Het getal was " + str(boot) + ".")
        
