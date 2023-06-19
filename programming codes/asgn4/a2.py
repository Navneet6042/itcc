d=int(input("enter day :"))
m=int(input("enter month :"))
y=int(input("enter year :"))
if (1<=d<=31 and m in (1,3,5,7,8,10,12) and 1800<=y<=2025):
    if d!=31 :
        print("next day is ",d+1,"/",m,"/",y)
    else:
        print("next day is ",1,"/",m,"/",y)
    print("31 days in the months")
elif (1<=d<=30 and m in (4,6,9,11) and 1800<=y<=2025):
    if d!=30:
        print("next day is ",d+1,"/",m,"/",y)
    else:
        print("next day is :",1,"/",m+1,"/",y)
    print("30 days in the months")

elif (1<=d<=29 and m==2 and 1800<=y<=2025 and y%4==0):
    if d!=29 :
        print("next day is ",d+1,"/",m,"/",y)
    else :
        print("next day is :",1,"/",m+1,"/",y)

    print("its february")
elif (1<=d<=28 and m==2 and 1800<=y<=2025 and y%4!=0) :
    if d!=28 :
        print("next day is ",d+1,"/",m,"/",y)
    else :
        print("next day is :",1,"/",m+1,"/",y)

    print("its february")
else :
    print("enter a valid input")