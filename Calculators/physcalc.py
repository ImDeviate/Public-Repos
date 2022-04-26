again = True
validchoice = False

varilist = '''
Which variable is unknown?: 
    1. xo/yo
    2. x/y
    3. vo
    4. v
    5. a
    6. t
    7. Exit
    
'''

eqlist1 = '''
Choose an Equation:
    1. x/y, vo, a/g, t
    2. x/y, vo, v, a/g

'''

eqlist2 = '''
Choose an Equation:
    1. xo/yo, vo, a/g, t
    2. xo/yo, vo, v, a/g

'''

eqlist3 = '''
Choose an Equation:
    1. v, a/g, t
    2. xo/yo, x/y, a/g, t

'''

eqlist4 = '''
Choose an Equation:
    1. vo, a/g, t
    2. xo/yo, x/y, vo, a/g

'''

eqlist5 = '''
Choose an Equation:
    1. vo, v, t
    2. xo/yo, x/y, vo, v
    3. xo/yo, x/y, vo, t

'''

eqlist6 = '''
Choose an Equation:
    1. vo, v, a/g
    2. xo/yo, x/y, vo, a/g

'''

def exec_operation(equation):
    eq12 = False
    if equation == 1:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    elif equation == 2:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    elif equation == 3:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    elif equation == 4:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    elif equation == 5:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    elif equation == 6:
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
            else:
                print("Invalid Choice, Choose again")
                eq12 = False
    return False

while again:
    while not validchoice:
        operation = int(input(varilist))
        if (operation >= 1) and (operation < 7):
            validchoice = exec_operation(operation)
        elif operation == 7:
            again = False
            validchoice = True
        else:
            print("Invalid Choice, Choose again")
            validchoice = False