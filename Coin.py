###########################################################################################
# Name: Zach Hoover
# Date: 2-10-19
# Description: Play a game by flipping coins.
###########################################################################################
from random import randint

def game(flips):
    flipA = 0.0
    flipB = 0.0
    flipP = 0.0

    #Flips the coins flip number of times and records the wins
    for i in range(0,flips):
        #0 is heads, 1 is tails
        #flip equals 0 if both coins land on heads
        #flip equals 2 if both coins land on tails
        #flip equals 1 if coins land on different sides
        flip = randint(0,1) + randint(0,1)
        if (flip == 0):
            flipA += 1
        elif (flip == 1):
            flipP += 1
        elif (flip == 2):
            flipB += 1
    #Prints the statistics of the game.
    print "Group A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%)".format\
          (flipA, (flipA/flips*100.0), flipB, (flipB/flips*100.0), flipP, (flipP/flips*100.0))
    #Decides the victor of the game
    #All groups with the highest score get a point in event of a tie.
    winA = 0
    winB = 0
    winP = 0
    if ((flipA >= flipB) and (flipA >= flipP)):
        winA = 1
    if ((flipB >= flipA) and (flipB >= flipP)):
        winB = 1
    if ((flipP >= flipB) or (flipP >= flipA)):
        winP = 1
    return winA, winB, winP
    
####MAIN####

#Ask for game and flip count
flips = input("How many games?  ")
games = input("How many coin tosses per game?  ")

winsA = 0.0
winsB = 0.0
winsP = 0.0

#Runs the game as many times as the user asked and tallies the scores.
for i in range(0, games):
    print "Game {}:".format(i)
    win =[]
    win = game(flips)
    winsA += win[0]
    winsB += win[1]
    winsP += win[2]
#Prints the results of the game.
print "Wins: Group A={} ({}%); Group B={} ({}%); Prof={} ({}%)".format\
      (winsA, (winsA/games*100), winsB, (winsB/games*100), winsP, (winsP/games*100))
