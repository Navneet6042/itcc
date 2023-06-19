n=int(input("enter number of rows  :"))
def fac(n):
    if n!=0:
        for i in range(n-1,0,-1):
            n=n*i
        return(n)
    else:
        return(1)


print((fac(0)))

def com(m,r):
    w=m-r
    tt=fac(w)
    yy=fac(m)
    zz=fac(r)
    cc=yy//(tt*zz)
    return(cc)

print(com(0,0))

for roww in range(n,0,-1):
    for elements in range(roww-1,0,-1):
        print("_",end="")
    
    
    for dd in range(0,n):
        for mm in range(dd):
            print(com(dd,mm),end=" ")
    print("*",end="")
    print("")
