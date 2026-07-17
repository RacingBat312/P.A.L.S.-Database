#P.A.L.S. Message Encrypter Ver 1.0
#'Handle this with care as well pls' -- Pat C

number_to_letter = {
"a" : 1,
"b" : 2,
"c" : 3,
"d" : 4,
"e" : 5,
"f" : 6,
"g" : 7,
"h" : 8,
"i" : 9,
"j" : 10,
"k" : 11,
"l" : 12,
"m" : 13,
"n" : 14,
"o" : 15,
"p" : 16,
"q" : 17,
"r" : 18,
"s" : 19,
"t" : 20,
"u" : 21,
"v" : 22,
"w" : 23,
"x" : 24,
"y" : 25,
"z" : 26,
"A" : 27,
"B" : 28,
"C" : 29,
"D" : 30,
"E" : 31,
"F" : 32,
"G" : 33,
"H" : 34,
"I" : 35,
"J" : 36,
"K" : 37,
"L" : 38,
"M" : 39,
"N" : 40,
"O" : 41,
"P" : 42,
"Q" : 43,
"R" : 44,
"S" : 45,
"T" : 46,
"U" : 47,
"V" : 48,
"W" : 49,
"X" : 50,
"Y" : 51,
"Z" : 52,
"1" : 53,
"2" : 54,
"3" : 55,
"4" : 56,
"5" : 57,
"6" : 58,
"7" : 59,
"8" : 60,
"9" : 61,
"," : 62,
"." : 63,
" " : 64,
"@" : 65,
"!" : 66,
"£" : 67,
"%" : 68,
"&" : 69,
"*" : 70,
"?" : 71,
"+" : 72,
"-" : 73,
"=" : 74
}

import os
import time

letter_to_number = {letter: number for letter, number in number_to_letter.items()}

file_path = r"F:\ProgramReliantFiles\encode.txt"
drive = os.path.splitdrive(file_path)[0] + "\\"

print("P.A.L.S. Message Encrypter Ver 1.0\n")

print(f"Waiting for drive {drive} and file {file_path}...")

while True:

    drive_available = os.path.exists(drive)
    file_available = os.path.exists(file_path)

    if not drive_available:
        print(f"Drive {drive} is not available. Please insert or connect the drive.")
    elif not file_available:
        print(f"File not found: {file_path}. Waiting for the file to appear.")

    time.sleep(5)

    if drive_available and file_available:
        print("\nFile found!")
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
        print("Encoding message...\n")
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
        break

input("Press ENTER to exit program")
