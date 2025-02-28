#Kenton Harris

lstTeams = [ "Arizona", "Arizona State", "Baylor", 
            "BYU", "UCF", "Cincinnati", "Colorado",
            "Houston","Iowa State","Kansas","Kansas State",
            "Oklahoma State", "TCU", "Texas Tech", "Utah", "West Virginia"]

def resetsTeams():
    lstTeams = ["Arizona", "Arizona State", "Baylor", 
            "BYU", "UCF", "Cincinnati", "Colorado",
            "Houston","Iowa State","Kansas","Kansas State",
            "Oklahoma State", "TCU", "Texas Tech", "Utah", "West Virginia"]
    
    return lstTeams

def printTeams():
    for iCount in range(len(lstTeams)) :
        print(f'{iCount+1}. {lstTeams[iCount]}')

#TODO: create a loop that will continully call print teams and get some user input
#def userInputLoop(): TODO: This will call the printTeams function and look for user input and then call print teams again
def userInputLoop(TeamValue = None):
    
    if TeamValue != None :
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = lstTeams[TeamValue-1]
                bContinue = False
            except :
                printTeams()
                TeamValue = int(input("Error, team not found enter corresponding number for team: "))
        
        lstTeams.remove(sTeamName)
    else :
        print("Error: No data supplied please input corresponding number")
        bContinue = True
        while bContinue == True:
            try :
                sTeamName = lstTeams[TeamValue-1]
                bContinue = False
            except :
                printTeams()
                TeamValue = int(input("Error, team not found enter corresponding number for team: "))
        
        lstTeams.remove(sTeamName)
    return sTeamName


