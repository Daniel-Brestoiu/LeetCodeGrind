#ToDo:
#Change XVals and YVals
#Change the formula.

x_vals = [0,1,2]
y_vals = [0,1]


def printProbs(x_vals, y_vals):
    ExpectedValX = 0
    ExpectedValY = 0
    ExpectedValXY = 0


    print("   ", end = " ")
    for x in x_vals:
        print(str(x).center(25), end = " ")

    print()
    for y in y_vals:
        print("Y=" + str(y), end = " ")
        sum = 0
        for x in x_vals:
            formula = 1/(x+y)
            print(str(formula).center(25), end = " ")
            sum+=formula
            ExpectedValX += formula*x
            ExpectedValY += formula*y
            ExpectedValXY += formula*x*y
        print("Sum=" + str(sum))
    
    print("   ", end = " ")

    for x in x_vals:
        sum = 0
        for y in y_vals:
            formula = 5/9*x
            sum+=formula
        print(str(sum).center(25), end = " ")

    print()
    print("E(X):" + str(ExpectedValX))
    print("E(Y):" + str(ExpectedValY))
    print("E(XY):" + str(ExpectedValXY))
    if (ExpectedValXY == ExpectedValX * ExpectedValY):
        print("E(XY) ==  E(X) * E(Y) - May (or may not be) independent!")
    else:
        print("E(XY) !=  E(X) * E(Y)")
            

printProbs(x_vals, y_vals)