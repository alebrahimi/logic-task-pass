def charCountInStr(myStr, toCountChar):
    return len(myStr.split(toCountChar)) - 1

def app():
    myStr = input("\nEnter any string : ")
    toCountChar = input("\nEnter any character to count in the string: ")

    print("Character count: ", charCountInStr(myStr, toCountChar))

app()