#reverse 
r=input("enter your string :")
n=""
for i in range(len(r)-1,-1,-1):
    m=r[i]
    n=n+m
print(n)