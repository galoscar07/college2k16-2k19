from src.Operations.operations import addition


def printMainMenuOption():
    string = "\n Available Comamnds: \n"
    string += "\t 1. Arithmetic Operations \n"
    string += "\t 2. Conversion Between Bases \n"
    string += "\t 3. Explications\n"
    string += "\t 0. Exit"
    print(string)

def printArithmeticOperation():
    string = "\n Available Commands: \n"
    string += "\t 1. Addition \n"
    string += "\t 2. Substraction\n"
    string += "\t 3. Multiplication\n"
    string += "\t 4. Division\n"
    string += "\t 0. Back to menu\n"
    print(string)

def printConversionMenu():
    string = "\n Available Commands: \n"
    string += "\t 1. Successive Divisions\n"
    string += "\t 2. Rapid Conversions\n"
    string += "\t 3. Substitution Method\n"
    string += "\t 4. Rapid Conversions\n"
    string += "\t 0. Back to menu\n"
    print(string)

def printExplications():
    string = "So, in order to decide whether an input is in a base or another you should follow this instructions:\n"
    string += "\t For base 2 put at the end of the number b (ex: 101b) \n"
    string += "\t For base 3 put at the end of the number t (ex: 121t) \n"
    string += "\t For base 4 put at the end of the number f (ex: 1232f) \n"
    string += "\t For base 5 put at the end of the number p (ex: 1432p) \n"
    string += "\t For base 6 put at the end of the number s (ex: 15432s) \n"
    string += "\t For base 7 put at the end of the number v (ex: 165432v) \n"
    string += "\t For base 8 put at the end of the number e (ex: 17654e) \n"
    string += "\t For base 9 put at the end of the number n (ex: 18723n) \n"
    string += "\t For base 16 put at the end of the number h (ex: 1A4Dh) \n"
    print(string)

def mainMenu():
    keepAlive = True
    while keepAlive:
        try:
            printMainMenuOption()
            command = int(input("Command: "))
            if command == 1:
                arithmeticMenu()
            elif command == 2:
                conversionMenu()
            elif command == 3:
                printExplications()
            elif command == 0:
                keepAlive = False
            else:
                print("Invalid input: ",command)
        except EnvironmentError as ee:                                               #TODO Change this Error into Error
            print(ee)

def arithmeticMenu():
    printArithmeticOperation()
    command = int(input("Command: "))
    if command == 0:
        None
    elif command == 1:
        uiAddition()
    elif command == 2:
        uiSubstraction()
    elif command == 3:
        uiMultiplication()
    elif command == 4:
        uiDivision()
    else:
        print("Invalid input: ",command)

def conversionMenu():
    printConversionMenu()
    command = int(input("Command: "))
    if command == 0:
        None
    elif command == 1:
        pass
    elif command == 2:
        pass
    else:
        print("Invalid input",command)

def uiAddition():
    print("Give 2 numbers")
    number1 = input("\t Number 1: ")
    number2 = input("\t Number 2: ")
    addition(number1,number2)

def uiSubstraction():
    pass

def uiMultiplication():
    pass

def uiDivision():
    pass