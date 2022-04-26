again = True

eqlist5 = '''
Choose an Equation:
    1. vo, v, t
    2. xo/yo, x/y, vo, v
    3. xo/yo, x/y, vo, t
    4. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq4 = int(input(eqlist5))
        if whicheq4 == 1:
            velonot = float(input("What is your inital velocity?: "))
            velo = float(input("What is your final velocity?: "))
            time = float(input("How long did it take?: "))
            accgrav = (velo - velonot) / time
            print("Your answer is: " + str(accgrav))
            eq12 = True
        elif whicheq4 ==2:
            xynot = float(input("What is your initial position?: "))
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            velo = float(input("What is your final velocity?: "))
            accgrav = ((velo ** 2) - (velonot ** 2)) / (2 * (xy - xynot))
            print("Your answer is: " + str(accgrav))
            eq12 = True
        elif whicheq4 == 3:
            xynot = float(input("What is your initial position?: "))
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            time = float(input("How long did it take?: "))
            accgrav = 2 * ((xy - xynot - (velonot * time)) / (time ** 2))
            print("Your answer is: " + str(accgrav))
            eq12 = True
        elif whicheq4 == 4:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False