from pathlib import Path
import sys

print("P.A.L.S Weapon Creations Program Ver 1.0")
print("Licensed by P.A.L.S Co Ltd")
print("All rights reserved")
print("DO NOT ACCESS THIS PROGRAM WITHOUT PROPER PERMISSION FROM A P.A.L.S. ADMINISTRATOR")
print("Weapon data last reviewed: 06/12/2025\n")

# This section of the code typically has issues, monitor regulary to ensure functionality \/

with open ("users.txt" , "r") as F:   # Opens the user data file
    users = F.read().splitlines()

# Section end /\

logins = {}
for user in users:
    un = user.split(',')[0] # Extract username
    pw = user.split(',')[1] # Extract password
    logins[un] = pw         # Populate the dictionary

username = input("Enter Username: ") # Removing the space from the 'for user in users' section takes these two commands out of the 'for' loop. 
password = input("Enter Password: ") # P.S. It was a pain finding this bug XD

def new_func(logins, username, password):
    if username not in logins.keys():
        print("\nThis user has not been found in the user list for said program...\n")
        print("Try again")
    elif logins[username] != password:
        print(f"\nThe password that has been entered does not match the password for {username}...\n")
        print("\nTry different username or enter correct password\n")

    # Prompt the user to re-enter
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username

def new_func1(logins, username, password, new_func):
    username = new_func(logins, username, password)
    return username

while username not in logins.keys() or logins[username] != password:
    username = new_func1(logins, username, password, new_func)

print("\nAccess granted!\n")
# Rest of the program goes from here

print(f"\nWhat would you like to view today, {username}?")
print("Enter help for more details")      # Main command input

# This section is the library for the weapon creations program, it will be updated as more weapons are created
# The program will check for weapon names + details and misc commands like 'help' and 'quit'
# Each weapon will have 3 sub commands, 0 for description, 1 for materials needed, 2 for uses and overall rating

loop = True
while loop == True:
    command = input("\nEnter command: ")     # Main command input

    # Help command, this will provide the user with details on how to use the program and what commands to enter to view the weapon details, this is a safety measure to ensure the user can easily navigate the program and find the information they need without having to guess or try random commands

    if command == "help":
        print("\nFor weapon details, first enter weapon name then enter")
        print("0 For description, 1 For materials needed, 2 For uses and overall rating. Type quit to exit program\n")
    
    # Quit command, this will exit the program when the user is done viewing the weapon details or if they want to exit for any reason, this is a safety measure to prevent the user from having to force quit the program or close the terminal window

    elif command == "quit":
        print("\nExiting program...")
        sys.exit()
    
    # This section is for the description of the A-Type Scrap Phone Holding Gauntlet

    elif command == "A-Type Scrap Phone Holding Gauntlet0":    
        print("\nThe A-Type Scrap Gauntlet is a makeshift gauntlet designed to securely hold a mobile phone.")
    elif command == "A-Type Scrap Phone Holding Gauntlet1":
        print("\nMaterials Needed: 1/ Thick Cardboard Roll  2/ Small Fridge Magnet  3/ Clear Tape")
    elif command == "A-Type Scrap Phone Holding Gauntlet2":
        print("\nUses: 1/ Arm Protection, barely adequate  2/ Barely holds phone in place  3/ Does its job at the skill of the creator//  Final Rating: C ") 

    # This section is for the description of the B-Type Scrap Protective Gauntlet

    elif command == "B-Type Scrap Protective Gauntlet0":    
        print("\nThe B-Type Scrap Protective Gauntlet is gauntlet simitar to its A-Type counterpart but with the removal of the phone holding module, it provides basic protection to light blows to the area it covers.") 
    elif command == "B-Type Scrap Protective Gauntlet1":
        print("\nMaterials Needed: 1/ Thick Cardboard Roll  2/ Clear Tape 3/ Spare peices of cardboard or any item that fits on the roll")
    elif command == "B-Type Scrap Protective Gauntlet2":
        print("\nUses: 1/ Arm Protection, adequate  2/ Light Blows or blunt objects only  3/ Does its job at the skill of the creator//  Final Rating: C+")
    
    # This section is for the description of the 'Smoke' Egg(Mk I)
    
    elif command == "Smoke Egg(Mark I)0":    
        print("\nThe Smoke Egg(Mark I) is an egg ridden of its normal contents and washed to ensure no remains are left,. then filled with a mixture of flour and pepper, but can have other daily condiments added as well.")    
    elif command == "Smoke Egg(Mark I)1":
        print("\nMaterials Needed: 1/ Empty Egg shell  2/ Eye irritant in powder form. THIS SHOULD NOT BE STICKY// Powder can contain: Garlic powder, Paprika, Pepper, Cajun, Chilli Flakes or Powder, Any other eye irritants")
    elif command == "Smoke Egg(Mark I)2":
        print("\nUses: 1/ VERY fragile  2/ Throw to release eye irritating smoke  3/ Easy and very efficient to make // Final Rating: A- ")
    
    # Invalid command section, this will be used to catch any typos or invalid commands and prompt the user to try again or ask for help

    else:  
        print("\nInvalid command, try again or type 'help' for more details")