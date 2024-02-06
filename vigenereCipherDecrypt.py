#CTM YRD OIB SRE SRR RIJ YRE BYL DIY MLC CYQ XSR RML QFS DXF OWF KTC YJR RIQ ZSM X

textFile = open("commonThreeLetterWords.txt", "r")
threeLetterWords = []
for line in textFile:
    threeLetterWords.append(line.strip())

alphabetDict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

cipherText = "CTM YRD OIB SRE SRR RIJ YRE BYL DIY MLC CYQ XSR RML QFS DXF OWF KTC YJR RIQ ZSM"
cipherText = cipherText.split(" ")
def convertLetter(letter):
    return alphabetDict[letter.lower()]

def shiftLetter(letter,amt):
    alphabetNum = alphabetDict[letter.lower()]
    shiftedNum = alphabetNum-amt
    if shiftedNum >=0:
        return chr(ord('`')+ shiftedNum + 1)
    else:
        return chr(ord('`')+ ((shiftedNum%25)+1)+1)

keyResults= open("keyResults.txt","w")

for key in threeLetterWords:
    shiftAmt = []
    sentence = ""
    for cipher in cipherText:
        for letter in key:
            shiftAmt.append(convertLetter(letter))
        for i in range(3):
            letter = cipher[i]
            shift = shiftAmt[i]
            sentence+= shiftLetter(letter,shift)    
    keyResults.write(key+": "+ sentence+"\n")
keyResults.close()
        