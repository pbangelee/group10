#Nathan Saez
#Display the final record for a team. Receive the home team data and display information.

def displayRecord(season):
    totalWins = 0
    # Loop for every list within the main list inside the dictionary
    for game in season :
        # Tally up total wins
        totalWins = totalWins + game.count("W")
    
    #Calculate total losses
    totalLosses = len(season) - totalWins

    #Store final record in a variable
    record = f"{totalWins}-{totalLosses}"

    # Return the variable to program
    return record

