again = True

eqlist4 = '''
Choose an Equation:
    1. vo, a/g, t
    2. xo/yo, x/y, vo, a/g
    3. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq = int(input(eqlist4))
        if whicheq == 1:
            velonot = float(input("What is your inital velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = float(input("How long did it take?: "))
            velo = velonot + (accgrav * time)
            print("Your answer is: " + str(velo))
            eq12 = True
        elif whicheq == 2:
            xynot = float(input("What is your initial position?: "))
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            velo = (velonot ** 2) + ((2 * accgrav) * (xy - xynot))
            velo = velo ** .5
            print("Your answer is: " + str(velo))
            eq12 = True
        elif whicheq == 3:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False