#herons
import math as m
a=int(input("enter side 1 :"))
b=int(input("enter side 2 :"))
c=int(input("enter side 3 :"))
s=(a+b+c)/2
l=s*((s-a)*(s-b)*(s-c))
b=m.sqrt(l)
print("area of triangle is ",b)
