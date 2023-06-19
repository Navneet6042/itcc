#fabonacci series
a=0
b=1
s=0

u=int(input("enter how many members you want :"))
print(a)
print(b)
for g in range(0,u-2):
    s=a+b
    a=b
    b=s
    print(s)