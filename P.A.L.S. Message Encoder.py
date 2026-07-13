#P.A.L.S. Message Encoder Ver 1.0
#'Handle this with care as well pls' -- Pat C

number_to_letter = {
"a": 41,
"b": 7,
"c": 54,
"d": 21,
"e": 3,
"f": 46,
"g": 12,
"h": 50,
"i": 17,
"j": 29,
"k": 55,
"l": 8,
"m": 34,
"n": 36,
"o": 2,
"p": 52,
"q": 24,
"r": 31,
"s": 14,
"t": 43,
"u": 19,
"v": 5,
"w": 40,
"x": 26,
"y": 38,
"z": 11,
"A": 53,
"B": 16,
"C": 1,
"D": 25,
"E": 47,
"F": 9,
"G": 45,
"H": 50,
"I": 28,
"J": 22,
"K": 4,
"L": 8,
"M": 34,
"N": 51,
"O": 18,
"P": 35,
"Q": 23,
"R": 31,
"S": 10,
"T": 42,
"U": 15,
"W": 33,
"X": 6,
"Y": 49,
"Z": 20,
",": 37,
".": 32,
" ": 27
}

letter_to_number = {letter: number for letter, number in number_to_letter.items()}

with open(r"F:\ProgramReliantFiles\encode.txt", "r") as f:
    text = f.read().strip("[]")
    letters = text.split("#")

letters = []
for ch in text:
    letters.append(ch)
    
encoded = []
for ch in letters:
    encoded.append(str(letter_to_number.get(ch)))

print("[" + "#".join(encoded) + "]")