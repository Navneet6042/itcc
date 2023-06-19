g=int(input("enter your grade point :"))
if g in range (4,11):
    if g==4:
        print("Your Grade is ‘D’ and poor Performance.")
    if g==5:
        print("Your Grade is ‘C’ and below average Performance.")
    if g==6:
        print("Your Grade is ‘C+’ and average Performance.")
    if g==7:
        print("Your Grade is ‘B’ and good  Performance.")
    if g==8:
        print("Your Grade is ‘B+’ and very good Performance.")
    if g==9:
        print("Your Grade is ‘A’ and exxcellent Performance.")
    if g==10:
        print("Your Grade is ‘A+’ and outstanding Performance.")
else :
    print("ERROR :please enter a valid input")