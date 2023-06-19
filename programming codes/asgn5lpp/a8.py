a=[]
b=[]
c=[]
d=[]
lno=[]
for i in range(0,10):
    print("number",i+1)
    y=int(input(" :"))
    lno.append(y)
    if y>0:
        a.append(y)
    if y<0:
        b.append(y)
    if y%2==0:
        c.append(y)
    if y%2!=0:
        d.append(y)
print("positive numbers",a)
print("negative numbers",b)
print("even numbers",c)
print("odd numbers",d)
for oi in range(0,len(lno)):
    mn=lno.count(lno[oi])
    print('number of times',lno[oi],"repeated =",mn)
