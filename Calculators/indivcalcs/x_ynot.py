again = True

eqlist1 = '''
Choose an Equation:
    1. x/y, vo, a/g, t
    2. x/y, vo, v, a/g
    3. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq2 = int(input(eqlist1))
        if whicheq2 == 1:
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = float(input("How long did it take?: "))
            xynot = xy - (velonot * time) - ((.5 * accgrav) * (time ** 2))
            print("Your answer is: " + str(xynot))
            eq12 = True
        elif whicheq2 == 2:
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            velo = float(input("What is your final velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            xynot = xy - (((velo ** 2) - (velonot ** 2)) / (2 * accgrav))
            print("Your answer is: " + str(xynot))
            eq12 = True
        elif whicheq2 == 3:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False