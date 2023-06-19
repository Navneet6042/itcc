n=int(input("enter no of enements you want to put in list  :"))
p=[]
for i in range(0,n):
    print("enter number",i+1,)
    t=int(input(":"))
    p.append(t)
piv=p[len(p)-1]

for i in range(0,len(p)):
    for j in range(len(p)-2,0,-1):
        if p[i]>piv and p[j]<piv and i<=j:
            p[i],p[j]=p[j],p[i]
        if p[j]<piv and p[i]>piv and j<i:
            p[i],piv=piv,p[i]
            piv=p[len(p)-1]
        else :
            continue
        print(p,"qw",i+1)
print(p)



