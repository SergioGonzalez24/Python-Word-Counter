#Developed by Sergio Gonzalez
#Text File Word Counter

finishProgram = "y"

while finishProgram == "y":

    Text = input("Insert text path: ")
    readTextFile = open(Text,"r")

    StringTxt = readTextFile.read().replace("\n", " ")
    sepWords = StringTxt.split(" ")

    notValidWords = 0
    for word in sepWords:
        if word == "":
            notValidWords += 1
        else:
            continue

    wordCount = (len(sepWords) - notValidWords)
    readTextFile.close()

    print("\n")
    print("**************************")
    print(f'The file has {wordCount} words')
    print("**************************")
    print("\n")

    finishProgram = input("Do you want to continue? y/n \n")


print("\n")
print("**************************")
print("Thank U for using Word Counter")
print("**************************")
print("\n")

