def getRandomPass(availableChars):
    import random

    generatedPassword = ""
    for x in range(8):
        if x == 2:
            generatedPassword += "A"
        elif x == 4:
            generatedPassword += "2"
        elif x == 6 and "#" not in generatedPassword:
            generatedPassword += "#"
        else:
            randNumber = random.randint(0, len(availableChars) - 1)
            generatedPassword += availableChars[randNumber]

    return generatedPassword
