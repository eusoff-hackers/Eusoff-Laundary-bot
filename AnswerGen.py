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

    returnStr = block + " Block \n  \n"
    for x in range(5):
        returnStr += "Washing Machine " + str(x + 1)  + " : " + defector(blockarr[x]) + "\n"

    return returnStr


def defector(num):
    if(num == 1):
        return "Avilable"
    else:
        return "Occupied"