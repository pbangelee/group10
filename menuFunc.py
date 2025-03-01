#Jennica Olsen
#2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.

def menu ():
    # Display menu options
    print("\nMenu:\n1. Choose Teams and play a season\n2. View Record\n3. Exit")
    bContinue = True
    while bContinue == True :
        try:
            #Gather user input and makes sure it is correct
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if 1<=choice<=3 :
                bContinue = False
            else :
                print("Please enter whole number between 1 and 4 ")
        except:
            print("Error, enter whole number between 1 and 4 ")
    # Return the output to program
    return choice



