def generateAnswer(arr, block):
    blockarr = []
    if block == "A":
       blockarr = arr[0]
    elif block == "B":
        blockarr = arr[1]
    elif block == "C":
        blockarr = arr[2]
    elif block == "D":
        blockarr = arr[3]
    elif block == "E":
        blockarr = arr[4]

    returnStr = ""
    for each in blockarr:
        returnStr += each + " "

    return returnStr