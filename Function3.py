# Kenton Harris
# Collection of various functions used throughout the program

# Function to reset list of all Big12 teams
def resetsTeams():
    listT = ["Arizona", "Arizona State", "Baylor", 
            "BYU", "UCF", "Cincinnati", "Colorado",
            "Houston","Iowa State","Kansas","Kansas State",
            "Oklahoma State", "TCU", "Texas Tech", "Utah", "West Virginia"]
    return listT
    
# Function to rest lists used to store data for a team
def resetsLists():
    listG = []
    return listG

# Function to print teams based on what is available
def printTeams(listP):
    for iCount in range(len(listP)) :
        print(f'{iCount+1}. {listP[iCount]}')

# Function to take user input for team and convert it into a string while also ensuring that input meets necessary requirements
def userInputLoop(listP, TeamValue = None):
    
    if TeamValue != None :
        # Checks to see if user input will cause negative indexing
        if TeamValue < 1 :
            bCont = True
            while bCont == True :
                try:
                    TeamValue = int(input("\nERROR: TEAM NOT FOUND, ENTER CORRESPONDING NUMBER FOR TEAM: "))
                    bCont = False
                except :
                    print("\nERROR: INCORRECT INPUT TYPE")                
        
        # Checks to see if team name is in the list and if not loop until you get the right input
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = listP[TeamValue-1]
                bContinue = False
            except :
                try:
                    TeamValue = int(input("\nERROR: TEAM NOT FOUND, ENTER CORRESPONDING NUMBER FOR TEAM: "))
                except :
                    print("\nERROR: INCORRECT INPUT TYPE")
        
    else :
        print("\nError: No data supplied please input corresponding number")
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = listP[TeamValue-1]
                bContinue = False
            except :
                try:
                    TeamValue = int(input("\nERROR: TEAM NOT FOUND, ENTER CORRESPONDING NUMBER FOR TEAM: "))
                except :
                    print("\nERROR: INCORRECT INPUT TYPE")
    # Returns string team name back to program
    return sTeamName

