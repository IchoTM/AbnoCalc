def riskClassCalc(dmg,diff,bp):
    if dmg <= 2 and diff <= 4 and bp <= 2:
        print("This Abno has a Risk Class of:  Zayin")
    elif dmg <= 2 and diff <= 6 and bp <= 2:
        print("This Abno has a Risk Class of:  Teth")
    elif dmg <= 3 and diff <= 6 and bp <= 3:
        print("This Abno has a Risk Class of:  He")
    elif dmg <= 3 and diff <= 7 and bp == 4:
        print("This Abno has a Risk Class of:  Waw")
    elif dmg == 4 and diff >= 8 and bp == 4:
        print("This Abno has a Risk Class of:  Aleph")
    else:
        print("something went wrong")
def getBreachPotential():
    bp = int(input("How likely is it for the Abno to breach? 1) Not Likely 2) Possible 3) Likely 4) Very Likely: "))
    return bp
def getDmgReach():
    dmg = int(input("In the event of a breach will the Abno's damage reach? 1) Single Target 2) Room Wide 3) Deparment Wide 4) Facility Wide: "))
    return dmg
def workDiffTotal():
    diff = int(input("On a scale of 1 to 10 what is the work success rate of this Abno?: "))
    return diff
def main():
    diff = workDiffTotal()
    dmg = getDmgReach()
    bp = getBreachPotential()
    risk = riskClassCalc(dmg,diff,bp)

main()
