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
        if TeamValue < 1 :
            bCont = True
            while bCont == True :
                try:
                    TeamValue = int(input("\nERROR: TEAM NOT FOUND, ENTER CORRESPONDING NUMBER FOR TEAM: "))
                    bCont = False
                except :
                    print("\nERROR: INCORRECT INPUT TYPE")                
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
    return sTeamName

