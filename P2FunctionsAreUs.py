# Kenton Harris, Jennica Olsen, Aaron Shumway, Angelee Marshall, Nathan Saez
#MAIN
from function2 import *
from Function3 import *
dctTeamRecords = {}

choice = 0
while choice !=3:
    choice = menu()
    if choice == 1:
        printTeams()
        bCont = True
        while bCont == True :
            try :
                iTeamName = int(input("Enter whole number corresponding to team name: "))
                bCont = False
            except :
                print("Error: incorrect input type")
        sHomeTeam = userInputLoop(iTeamName)
        printTeams()
        iTeamName = int(input("Enter number corresponding to opponent team: "))
        sOpponentTeam = userInputLoop(iTeamName)
    elif choice == 2:
        y =20
