#GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICACGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCGBCGQOEVSHUNSUGKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGBSLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAENNSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQGKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKREHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKGSZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCAUSOEGCKGCEUQCGAEUGKCUSZUEGBHSKGEHBCUGERPKHEHKHNSZKGGKAD
def decryptSimpleSubCipher(cipherText):
    letterDict = {}
    for letter in cipherText:
        if letter not in letterDict:
            letterDict[letter] = 1
        else:  
            letterDict[letter]+=1

    #items returns [key,value], lambda accesses the value and returns it
    letterDict = dict(sorted(letterDict.items(), key=lambda x:x[1],reverse=True))
    print("Letter Frequency from Most to Least:")
    print(letterDict)
    replacementDict = {}
    for letter in letterDict:
        guess = input("Guess what "+ str(letter).lower()+ " is: ").upper()
        replacementDict[letter] = guess

    decryptedMessage = ""
    for letter in cipherText:
        decryptedMessage+= replacementDict[letter]
    return decryptedMessage

encryptedMessage = input("Put in your cipherText \n")
print("Your decrypted message is:\n", decryptSimpleSubCipher(encryptedMessage))
