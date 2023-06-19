s1=int(input("enter side1  :"))
s2=int(input("enter side2  :"))
s3=int(input("enter side3  :"))
d=s1>s2+s3
e=s2>s1+s3
f=s3>s2+s1
while d==True or e==True or f==True:
    print("no")
    break

while d==False and e==False and f==False:
    print("yes")
    break
