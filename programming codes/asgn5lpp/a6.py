g=int(input("enter you number :"))
for i in range(1,g):
    if i==1 or i==g:
        continue
    else:
        if g%i==0:
            print("not a prime number")
            break
        else:
            if g%i!=0 and i+1==g:
                print("its a prime number")
            else :
                continue