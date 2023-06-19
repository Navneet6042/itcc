w=int(input("how many numbers you want to enter"))
sum=0
for e in range (0,w):
    print("enter your",e+1,"number ")
    y=int(input(":"))
    sum=y+sum
print("average of ",w,"numbers is",sum/w)