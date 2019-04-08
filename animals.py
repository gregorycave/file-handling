# Reading from a file

def readFile():
    with open("new_animals.txt", mode="r", encoding="utf-8") as myFile:
        for eachLine in myFile:
            print(eachLine.rstrip("\n"))

def readFile2():
    with open("new_animals.txt", mode="r", encoding="utf-8") as myFile:
        animals= myFile.read().splitlines()
    for each in animals:
        print(each)
    animalToFind=input("What are you looking for?")
    if animalToFind in animals:
        print("{0} found in file new_animals.txt".format(animalToFind))
    else:
        print("{0} not found in file new_animals.txt".format(animalToFind))
