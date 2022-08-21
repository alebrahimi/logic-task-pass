def removeCharFromStr(myStr, toRemoveChar):
    return myStr.replace(toRemoveChar, '')

def app():
    myStr = input("\nEnter any string : ")
    toRemoveChar = input("\nEnter any character to remove from the string: ")

    print(removeCharFromStr(myStr, toRemoveChar))

app()