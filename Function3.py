#Kenton Harris


def resetsTeams():
    listT = ["Arizona", "Arizona State", "Baylor", 
            "BYU", "UCF", "Cincinnati", "Colorado",
            "Houston","Iowa State","Kansas","Kansas State",
            "Oklahoma State", "TCU", "Texas Tech", "Utah", "West Virginia"]
    return listT
    
def resetsLists():
    listG = []
    return listG

def printTeams(listP):
    for iCount in range(len(listP)) :
        print(f'{iCount+1}. {listP[iCount]}')

#TODO: create a loop that will continully call print teams and get some user input
#def userInputLoop(): TODO: This will call the printTeams function and look for user input and then call print teams again
def userInputLoop(listP, TeamValue = None):
    
    if TeamValue != None :
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = listP[TeamValue-1]
                bContinue = False
            except :
                printTeams(listP)
                try:
                    TeamValue = int(input("Error, team not found enter corresponding number for team: "))
                except :
                    print("ERROR: INCORRECT INPUT TYPE")
        
    else :
        print("Error: No data supplied please input corresponding number")
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = listP[TeamValue-1]
                bContinue = False
            except :
                printTeams(listP)
                try:
                    TeamValue = int(input("Error, team not found enter corresponding number for team: "))
                except :
                    print("ERROR: INCORRECT INPUT TYPE")
    return sTeamName

