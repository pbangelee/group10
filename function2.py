#Jennica Olsen
#2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.

def menu ():
    global choice
    print("\nMenu:\n1. Choose Teams\n2. Play a Match\n3. View Record\n4.Exit")
    bContinue = True
    while bContinue == True :
        try:
            choice = int(input("Enter your choice (1, 2, 3 or 4): "))
            bContinue = False
        except:
            print("Error, enter whole number between 1 and 4")
    return choice



