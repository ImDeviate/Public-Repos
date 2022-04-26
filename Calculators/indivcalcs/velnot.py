again = True

eqlist3 = '''
Choose an Equation:
    1. v, a/g, t
    2. xo/yo, x/y, a/g, t
    3. Exit

'''

while again:
    eq12 = False
    while not eq12:
        whicheq2 = int(input(eqlist3))
        if whicheq2 == 1:
            velo = float(input("What is your final velocity?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = float(input("How long did it take?: "))
            velonot = velo - (accgrav * time)
            print("Your answer is: " + str(velonot))
            eq12 = True
        elif whicheq2 == 2:
            xynot = float(input("What is your initial position?: "))
            xy = float(input("What is your final position?: "))
            accgrav = float(input("What is your acceleration/gravity?: "))
            time = float(input("How long did it take?: "))
            velonot = ((xy - xynot - ((.5 * accgrav) * (time ** 2))) / time)
            print("Your answer is: " + str(velonot))
            eq12 = True
        elif whicheq2 == 3:
            again = False
            eq12 = True
        else:
            print("Invalid Choice, Choose again")
            eq12 = False