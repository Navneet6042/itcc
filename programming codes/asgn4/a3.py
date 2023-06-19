count=0
f=[]
u=int(input("enter number of inputs you want to enter :"))
while True:
    i=int(input("enter number for finding square :"))
    b=(i,i**2)
    
    f.append(b)
    count+=1
    if count==u:
        break
    else:
        continue
print(f)