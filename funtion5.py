#Nathan Saez
#Display the final record for a team. Receive the home team data and display information.

def displayRecord(season):
    totalWins = 0
    for game in season :
        totalWins = totalWins + game.count("W")
    
    totalLosses = len(season) - totalWins

    record = f"{totalWins}-{totalLosses}"
    return record

