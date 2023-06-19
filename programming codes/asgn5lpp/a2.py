#divchk
r=int(input("enter the range :"))
n=int(input("enter the number to check divisibility by :"))
for i in range(1,r+1):
    if i%n==0:
        print(i)
    else:
        continue