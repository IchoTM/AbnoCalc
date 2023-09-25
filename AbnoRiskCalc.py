def riskClassCalc():
    print("dosen't work yet")
def getBreachPotential():
    bp = int(input("How likely is it for the Abno to breach? 1) Not Likely 2) Possible 3) Likely 4) Very Likely: "))
    return bp
def getDmgReach():
    dmg = int(input("In the event of a breach will the Abno's damage reach? 1) Single Target 2) Room Wide 3) Deparment Wide 4) Facility Wide: "))
    return dmg
def workDifTotal(r,s,c,a):
    print("dosen't work yet")
def getRepWorkDiff():
    while r != 1 and r != 2 and r != 3 and r != 4 and r != 5 and r != 6 and r != 7 and r != 8 and r != 9 and r != 10:
        r = int(input("Enter the success rate of Repression work (on a scale from 1 to 10): "))
        if  r != 1 and r != 2 and r != 3 and r != 4 and r != 5 and r != 6 and r != 7 and r != 8 and r != 9 and r != 10:
            print("Please Enter a Vaild Value")
        else:
            return r
def getInsWorkDiff():
    i = int(input("Enter the success rate of Insight work (on a scale from 1 to 10): "))
    return i
def getIncWorkDiff():
    i = int(input("Enter the success rate of Instinc work (on a scale from 1 to 10): "))
    return i
def getAttWorkDiff():
    a = int(input("Enter the success rate of Attachment work (on a scale from 1 to 10): "))
    return a


def main():
    r = getRepWorkDiff()
    s = getInsWorkDiff()
    c = getIncWorkDiff()
    a = getAttWorkDiff()
    diff = workDifTotal(r,s,c,a)
    dmg = getDmgReach()

main()
