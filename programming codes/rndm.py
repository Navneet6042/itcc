def fac(n):
    if n!=0:
        for i in range(n-1,0,-1):
            n=n*i
        return(n)
    else:
        return(1)



def com(m,r):
    w=m-r
    tt=fac(w)
    yy=fac(m)
    zz=fac(r)
    cc=yy//(tt*zz)
    return(cc)



n=int(input('enter no of rows :'))

for gg in range(0,n):
    for hj in range(0,gg+1):
        print(end=" "*(n-gg))
        print(com(gg,hj),end=" ")
    print("")
    

    
    