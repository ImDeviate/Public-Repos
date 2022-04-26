again = True
validchoice = False

while again:
    while not validchoice:
        selection = input("Choose one of the following: Addition, Subtraction, Multiplication, Division: ")
        if (selection == "Addition") or (selection == "addition") or (selection == "Subtraction") or (selection == "suubtraction") or \
        (selection == "Division") or (selection == "division") or (selection == "Multiplication") or (selection == "multiplication"):
            validchoice = True
        else:
            print("Invalid Choice")
            validchoice = False
    if (selection == "addition") or (selection == "Addition"):
        numbera1 = float(input("Enter your first number: "))
        numbera2 = float(input("Enter your second number: "))
        adsum = float(numbera1+numbera2)
        print("The sum is: " + str(adsum))
    elif (selection == "Subtraction") or (selection == "subtraction"):
        numbers1 = float(input("Enter your first number: "))
        numbers2 = float(input("Enter your second number: "))
        susum = float(numbers1-numbers2)
        print("The sum is: " + str(susum))
    elif (selection == "multiplication") or (selection == "Multiplication"):
        numberm1 = float(input("Enter your first number: "))
        numberm2 = float(input("Enter your second number: "))
        mpproduct = float(numberm1*numberm2)
        print("The product is: " + str(mpproduct))
    elif (selection == "division") or (selection == "Division"):
        numberd1 = float(input("Enter your first number: "))
        numberd2 = float(input("Enter your second number: "))
        diproduct = float(numberd1/numberd2)
        print("The product is: " + str(diproduct))
    doneyet = False
    while not doneyet:
        question = input("Are you done?: ")
        if (question == "Yes") or (question == "yes"):
            again = False
            doneyet = True
        elif (question == "No") or (question == "no"):
            validchoice = False
            doneyet = True
        elif (question != "Yes") or (question != "yes") or (question != "No") or (question != "no"):
            print("Invalid Response")
            validchoice = True