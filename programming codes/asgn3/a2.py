cal=int(input("enter year for checking leap year :"))
if cal%100 and cal%400==0:
    print("it is a leap year")
elif cal%4==0 :
    print("it is a leap year")
else :
    print("entered year is not a leap year")