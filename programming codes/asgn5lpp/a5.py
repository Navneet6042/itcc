y=int(input("enter number of rows :"))
k=65
for i in range(1,y+1):
    for u in range(0,i):
        print(chr(k),end="")
        if 65<=k<=89:
            k=k+1
        else:
            k=65
    print('')