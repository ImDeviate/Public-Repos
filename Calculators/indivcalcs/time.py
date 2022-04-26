again = True

eqlist6 = '''
Choose an Equation:
    1. vo, v, a/g
    2. xo/yo, x/y, vo, a/g
    3. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq3 = int(input(eqlist6))
        if whicheq3 == 1:
            velonot = float(input("What is your inital velocity?: "))
            velo = float(input("What is your final velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = (velo - velonot) / accgrav
            print("Your answer is: " + str(time))
            eq12 = True
        elif whicheq3 == 2:
            xynot = float(input("What is your initial position?: "))
            xy = float(input("What is your final position?: "))
            velonot = float(input("What is your inital velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time1 = (-velonot + ((velonot ** 2) - 4 * (xynot-xy) * (.5 * accgrav)) ** .5) / accgrav
            time2 = (-velonot - ((velonot ** 2) - 4 * (xynot-xy) * (.5 * accgrav)) ** .5) / accgrav
            print("This equation is quadratic so there are 2 answers, choose the most correct answer for your use.")
            print("Your first answer is: " + str(time1))
            print("Your second answer is: " + str(time2))
            eq12 = True
        elif whicheq3 == 3:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False