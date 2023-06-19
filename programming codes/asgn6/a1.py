def numprft(a):
    stno=[]
    print("your enter number for checking for perfectness is :",a)
    if a<0:
        print("the number is not perfect")
    if a==0:
        print("0 is not a perfect number")
    else:                        #in this else part only the positive integers will come 
        sum=0
        for u in range(1,a+1):
            if a%u==0:
                stno.append(u)          #collectting its positive divisors in list stno
            
        for k in stno :
            sum=sum+k                #taking the sum of its positive divisors
        if a==(sum//2):
            print(a,"is a perfect number")
        else :
            print(a,"is not a perfect number")
            
