import time
import random

rooms = ["You enter the next room and there is three paths Left, Right And Straight which one do you take", "You enter the next room and there is two paths Left And Straight which one do you take", "You enter the next room and there is two paths Right And Straight which one do you take", "You enter the next room and there is two paths Left and Right which one do you take"]
encounterChance = [1,2,3,4,5,6]
guessNumber = [1,2,3]
randomNumbers = [1,2,3,4,5,6,7,8,9,10]
PlayerHP = 1
introText = "You have heard of a mystical weapon in a cave, So you a young barbarian sets out to explore the cave and recover the mystical weapon"

print("==========================")
print("|                        |")
print("|      The Dungeon       |")
print("|                        |")
print("| Press Start When Ready |")
print("|                        |")
print("==========================")

startingInput = input()

if startingInput == "start":
    print("")
    time.sleep(1)
    print("")
    time.sleep(1)
    print(introText)
    time.sleep(1)

def pathSelector(): 
    playerInput = input()
    if playerInput == "forward":
        print("You decide to go forward deeper into the cave")
    elif playerInput == "left":
        print("You decide to turn left deeper into the cave")
    elif playerInput == "right":
        print("You decide to turn right deeper into the cave")

def monsterEncounter():
    print("You enter the next room and you encounter a monster")
    print("To beat the monster you must guess the number the monster is thinking")
    print("The number will be either 1, 2 or 3")
    print("What do you guess")
    playerInput = input()
    if playerInput == random.choice(guessNumber):
        print("you have successfully guess the number and beatened the monster and you are able to continue forward")
    elif playerInput != random.choice(guessNumber):
        print("You have guessed the wrong number and take damage")
        global PlayerHP
        PlayerHP -= random.choice(randomNumbers)
        print("Your HP Is",PlayerHP)

while PlayerHP > 0:
    print(random.choice(rooms))
    pathSelector()
    if random.choice(encounterChance) <= 4:
        print(random.choice(rooms))
        pathSelector()
    else:
        monsterEncounter()
    if randomNumbers == 10:
        print('You encounter a healing shrint you if you guess the right number you restore some of your hp')
        print('Guess the number it can be 1, 2 and 3')
        playerInput = input()
        if playerInput == random.choice(guessNumber):
           print("You guess correctly the shrine glows green and it heals you")
           PlayerHP += random.choice(randomNumbers)
           print("Your HP is now", PlayerHP)
        else:
            print("You guess the wrong number and the shrine crumbles")
    if PlayerHP <= 0:
        print("Your HP has reached zero and you have died thank you for playing my game")
        quit()