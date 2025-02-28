#Angelee Marshall
#Function 4: Recieves teams scores and doesnt allow for ties. Returns output of L or W
def play_game(home_team, opponent_team):
    # Generate random scores for both teams
    home_score = random.randint(0, 5)
    opponent_score = random.randint(0, 5)
    
    # Make sure there are no ties
    while home_score == opponent_score:
        home_score = random.randint(0, 5)
        opponent_score = random.randint(0, 5)
    
    # Determine win or loss
    if home_score > opponent_score:
        outcome = "W"
    else:
        outcome = "L"
    
    return outcome