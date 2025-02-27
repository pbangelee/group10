# Kenton Harris
# Gathers inputs from user on team name and number of games, gathers inputs about those games, then displays game info and season stats

# Imports random functions
import random

# Prompt user for team and number of games
sTeamName = input("\nWhat is your team's name? ")
iGameCount = int(input("\nHow many games did " + sTeamName + " play? "))

# Initialize variables
dictTeam = {}
lstGameInfo = []
iWinTotal = 0
iLossTotal = 0

# Let's get Pretty
print("\n")

# Enter loop to repeat based on number of games
for iCount in range(0,iGameCount) :
    
    # Gather opponent name
    sOpponentName = input(f"Enter name of opponent for game {iCount+1}:   ")
    
    # Set scores equal to 0 to enter loop
    iTeamSore = 0
    iOpponentScore = 0

    # Assigns random scores and repeats until scores do not equal eachother
    while iTeamSore == iOpponentScore :
        iTeamSore = random.randint(0,5)
        iOpponentScore = random.randint(0,5)

    # Checks to see if match is win or loss and tallies the outcome
    if iTeamSore > iOpponentScore :
        sGameOutcome = "W"
        iWinTotal += 1
    else :
        iLossTotal += 1
        sGameOutcome = "L"
    
    # Stores match info list in another list
    lstGameInfo.append([sOpponentName,iTeamSore,iOpponentScore,sGameOutcome])
    
    

# Assigns list to dictionary
dictTeam[sTeamName] = lstGameInfo

# Let's get pretty
print("\n")

# Prints out all games and their info
for iGames in range(0,iGameCount) :
    print(f"{sTeamName}'s score: {dictTeam[sTeamName][iGames][1]} {dictTeam[sTeamName][iGames][0]}'s score: {dictTeam[sTeamName][iGames][2]} {dictTeam[sTeamName][iGames][3]}")

# Calculates the win Pctg
fWinPctg = iWinTotal/iGameCount

# Prints season record
print(f"\nFinal season record: {iWinTotal}-{iLossTotal}")

# Print appropriate prompt based on him percentage
if fWinPctg >= .75 :
    print("Qualified for the NCAA Women's Soccer Tournament!")
elif fWinPctg >= .5 :
    print("You had a good season!")
else :
    print("Your team needs to practice!")