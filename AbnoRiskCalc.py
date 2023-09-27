def riskClassCalc(dmg,diff,bp):
    if dmg <= 2 and diff <= 4 and bp <= 2:
        print("This Abno has a Risk Class of:  Zayin")
    elif dmg <= 2 and diff <= 6 and bp <= 2:
        print("This Abno has a Risk Class of:  Teth")
    elif dmg <= 3 and diff <= 6 and bp <= 3:
        print("This Abno has a Risk Class of:  He")
    elif dmg <= 3 and diff <= 7 and bp <= 4:
        print("This Abno has a Risk Class of:  Waw")
    elif dmg <= 4 and diff <= 8 and bp <= 4:
        print("This Abno has a Risk Class of:  Aleph")
    else:
        print("something went wrong")
def getBreachPotential():
    print("How likely is it for the Abnormality to breach its containment?")
    print("1) Not Likely")
    print("2) Possible")
    print("3) Likely")
    print("4) Very Likely")
    bp = int(input(">"))
    return bp
def getDmgReach():
    print("In the event of a breach will the Abnormality's damage reach?")
    print("1) Single Target")
    print("2) Room Wide")
    print("3) Deparment Wide")
    print("4) Facility Wide")
    dmg = int(input(">"))
    return dmg
def workDiffTotal():
    diff = int(input("On a scale of 1 to 10 what is the work success rate of this Abnormality?: "))
    return diff
def varCheck(w,g,b):
    error = int()
    error = 0
    if w not in range(1,11):
        error = 1
        print("W fail")
        return error
    elif g not in range(1,5):
        error = 1
        print("G fail")
        return error
    elif b not in range(1,5):
        error = 1
        print("B fail")
        return error
    else:
        return error
def main():
    diff = workDiffTotal()
    dmg = getDmgReach()
    bp = getBreachPotential()
    vc = varCheck(diff,dmg,bp)
    if vc == 1:
        print("Something is wrong")
    else:
        risk = riskClassCalc(dmg,diff,bp)

main()
