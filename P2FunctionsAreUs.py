# Kenton Harris, Jennica Olsen, Aaron Shumway, Angelee Marshall, Nathan Saez
# Imports functions from files and then runs program to simulate soccer games for various teams and output season results

# Import function files
from function2 import *
from Function3 import *
from fun4 import *
from function1 import *
from funtion5 import displayRecord

# Initialize variables
lstTeams = [ "Arizona", "Arizona State", "Baylor", 
            "BYU", "UCF", "Cincinnati", "Colorado",
            "Houston","Iowa State","Kansas","Kansas State",
            "Oklahoma State", "TCU", "Texas Tech", "Utah", "West Virginia"]
lstGameInfo = []
dctTeamRecords = {}

# Run introudction function
print("\n\n")
sUserName = introduction()

# Enters into main menu and main program loop
choice = 0
while choice !=3:

    # Displays menu and asks for input
    choice = menu()
    if choice == 1:
        
        # Displays list of all available teams
        printTeams(lstTeams)
        bCont = True

        # Gathers and checks user for "home" team
        while bCont == True :
            try :
                iTeamName = int(input(f"\n{sUserName}, enter whole number corresponding to team name: "))
                bCont = False
            except :
                print("\nERROR: INCORRECT INPUT TYPE")

        # Assigns home team variable to output from function
        sHomeTeam = userInputLoop(lstTeams,iTeamName)

        # Checks to see if team has already been stored in dictionary
        if sHomeTeam in dctTeamRecords :
            printTeams(lstTeams)
            print("\nERROR: TEAM ALREADY SIMULATED")
        else :
            # Removes team from list
            lstTeams.remove(sHomeTeam)

            # Asks for length of the season
            bCont = True
            while bCont == True:

                # Loop to make sure integer is inputed
                bC = True
                while bC == True:
                    try :
                        iGameCount = int(input(f"\nHow many games did {sHomeTeam} play? "))
                        bC = False
                    except :
                        print("\nERROR: INCORRECT DATA TYPE")
                
                # Checks to see if season is too long or too short
                if 1<=iGameCount<=15 :
                    bCont = False
                else:
                    print("\nPlease input number between 1 and 15")

            # Loops based on how many games inputed above
            for iCount in range(0,iGameCount):
                
                # Gathers and checks opponent name
                printTeams(lstTeams)
                bCont = True
                while bCont == True :
                    try :
                        iTeamName = int(input(f"\n{sUserName}, enter whole number corresponding to {iCount+1} opponent team name: "))
                        bCont = False
                    except :
                        print("\nERROR: INCORRECT INPUT TYPE")
                
                # Stores opponent name using the same function
                sOpponentTeam = userInputLoop(lstTeams,iTeamName)

                # Removes the opponent name
                lstTeams.remove(sOpponentTeam)

                # Generates the result of the game and then stores in variable
                sResult = play_game()

                # Adds individual game results to overall list
                lstGameInfo.append([sOpponentTeam,sResult])
            
            # Stores overall list into dictionary with home team name as the key
            dctTeamRecords[sHomeTeam] = lstGameInfo

            print("Season data saved!")
            # Runs functions to reset the lists for the next loop
            lstTeams = resetsTeams()
            lstGameInfo = resetsLists()
        
    elif choice == 2:
        # Displays list of all available teams
        printTeams(lstTeams)
        bCont = True

        # Gathers and checks user for "home" team
        while bCont == True :
            try :
                iTeamName = int(input(f"\n{sUserName}, enter whole number corresponding to team name: "))
                bCont = False
            except :
                print("\nERROR: INCORRECT INPUT TYPE")
        
        sHomeTeam = userInputLoop(lstTeams,iTeamName)
        
        # Checks to see if team has been simulated
        if sHomeTeam in dctTeamRecords :
            # Displays final record
            print(f"\n{sHomeTeam} had a final record of {displayRecord(dctTeamRecords[sHomeTeam])}")
        else :
            print("\nTeam has not been simulated yet")

print("Exiting Program: Bye!")
