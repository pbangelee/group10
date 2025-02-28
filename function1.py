#Aaron Shumway
#function 1
#introduce program and get user's name
def introduction():
    print("Welcome to the game!")
    print("In this game, you will choose a team and their opponents, and we will simulate their season!")

#get their name, strip in case they put a space
    sName = input("Enter your name: ").strip()

    print(f'Welcome {sName}, get ready to play!')
    
    return sName

#on main branch, need to syntax the following: sName = introduction()
#^^^that allows the users name to be stored in that file to be used throughout program
