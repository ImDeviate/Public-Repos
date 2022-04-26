again = True

eqlist2 = '''
Choose an Equation:
    1. xo/yo, vo, a/g, t
    2. xo/yo, vo, v, a/g
    3. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq1 = int(input(eqlist2))
        if whicheq1 == 1:
            xynot = float(input("What is your initial position?: "))
            velonot = float(input("What is your inital velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = float(input("How long did it take?: "))
            xy = xynot + (velonot * time) + ((.5 * accgrav) * (time ** 2))
            print("Your answer is: " + str(xy))
            eq12 = True
        elif whicheq1 == 2:
            xynot = float(input("What is your initial position?: "))
            velonot = float(input("What is your inital velocity?: "))
            velo = float(input("What is your final velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            xy = xynot + (((velo ** 2) - (velonot ** 2)) / (2 * accgrav))
            print("Your answer is: " + str(xy))
            eq12 = True
        elif whicheq1 == 3:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False