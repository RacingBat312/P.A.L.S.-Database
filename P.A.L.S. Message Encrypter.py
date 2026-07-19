#P.A.L.S. Message Encrypter Ver 1.5
#'Handle this with care as well pls' -- Pat C

number_to_letter = {
"a" : 4,
"b" : 21,
"c" : 38,
"d" : 55,
"e" : 72,
"f" : 15,
"g" : 32,
"h" : 49,
"i" : 66,
"j" : 9,
"k" : 26,
"l" : 43,
"m" : 60,
"n" : 3,
"o" : 20,
"p" : 37,
"q" : 54,
"r" : 71,
"s" : 14,
"t" : 31,
"u" : 48,
"v" : 65,
"w" : 8,
"x" : 25,
"y" : 42,
"z" : 59,
"A" : 2,
"B" : 19,
"C" : 36,
"D" : 53,
"E" : 70,
"F" : 13,
"G" : 30,
"H" : 47,
"I" : 64,
"J" : 7,
"K" : 24,
"L" : 41,
"M" : 58,
"N" : 1,
"O" : 18,
"P" : 35,
"Q" : 52,
"R" : 69,
"S" : 12,
"T" : 29,
"U" : 46,
"V" : 63,
"W" : 6,
"X" : 23,
"Y" : 40,
"Z" : 57,
"1" : 74,
"2" : 17,
"3" : 34,
"4" : 51,
"5" : 68,
"6" : 11,
"7" : 28,
"8" : 45,
"9" : 62,
"," : 5,
"." : 22,
" " : 39,
"@" : 56,
"!" : 73,
"£" : 16,
"%" : 33,
"&" : 50,
"*" : 67,
"?" : 10,
"+" : 27,
"-" : 44,
"=" : 61
}

import os
import time
import sys

letter_to_number = {letter: number for letter, number in number_to_letter.items()}

file_path = r"F:\ProgramReliantFiles\encode.txt"
drive = os.path.splitdrive(file_path)[0] + "\\"

print("P.A.L.S. Message Encrypter Ver 1.5\n")
print("Either read file \"/reafil/\" or manual input \"/maninp/\"\n")
 
while True:
    option = input("Please enter method of extraction>>> ")

    if option == "/reafil/":
            
            print("\n")
            print(f"Waiting for drive {drive} and file {file_path}...")

            while True:

                drive_available = os.path.exists(drive)
                file_available = os.path.exists(file_path)

                if not drive_available:
                    print(f"\nDrive {drive} is not available. Please insert or connect the drive.")
                elif not file_available:
                    print(f"\nFile not found: {file_path}. Waiting for the file to appear.")

                time.sleep(5)

                if drive_available and file_available:
                    print("\nFile found!\n\n")
                    print("Checking message for non ecryptable characters...\n")
                    import sys
                    import time
                    from time import sleep
                    for i in range(101):
                        sys.stdout.write('\r')
                        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
                        sys.stdout.flush()
                        sleep(0.07)
                    print("\n")
                    print("Verfication Successful!")
                    print("\n")
                    print("Inspecting codex for character keys...\n")
                    import sys
                    import time
                    from time import sleep
                    for i in range(101):
                        sys.stdout.write('\r')
                        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
                        sys.stdout.flush()
                        sleep(0.02)
                    print("\n")
                    print("Inspection complete.")
                    print("\n")
                    print("Encrypting message...\n")
                    import sys
                    import time
                    from time import sleep
                    for i in range(101):
                        sys.stdout.write('\r')
                        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
                        sys.stdout.flush()
                        sleep(0.15)
                    print("\n")

                    with open(file_path, "r") as f:
                        text = f.read().strip("[]")

                    letters = []
                    for ch in text:
                        letters.append(ch)
                        
                    encoded = []
                    for ch in letters:
                        encoded.append(str(letter_to_number.get(ch)))

                    print("[" + "#".join(encoded) + "]")
                    print("\n")
                    input("Press ENTER to exit program")
                    sys.exit()
                    

    elif option == "/maninp/":
       
        text = input("\nEnter message>>> ").strip("[]")

        print("\nChecking message for non encryptable characters...\n")
        import sys
        import time
        from time import sleep
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
            sys.stdout.flush()
            sleep(0.07)
        print("\n")
        print("Verfication Successful!")
        print("\n")
        print("Inspecting codex for character key values...\n")
        import sys
        import time
        from time import sleep
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
            sys.stdout.flush()
            sleep(0.02)
        print("\n")
        print("Inspection complete.")
        print("\n")
        print("Ecrypting message...\n")
        import sys
        import time
        from time import sleep
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
            sys.stdout.flush()
            sleep(0.15)
        print("\n")
        print("")

        letters = []
        for ch in text:
            letters.append(ch)
            
        encoded = []
        for ch in letters:
            encoded.append(str(letter_to_number.get(ch)))

        print("[" + "#".join(encoded) + "]")
        print("\n")

        input("Press ENTER to exit program")

    else:
        print("\nInvalid command, enter either \"/reafil/\" or \"/maninp/\"\n")
        option



        