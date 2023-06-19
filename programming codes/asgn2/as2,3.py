#greatestnumber
y=int(input("how many nmbers you want to enter  :"))
l=0
p=0
for a in range(0,y):
    print("enter number",a+1)
    g=int(input(":"))
    if g>l:
        h=g                #for conserving the value of g
        g,p=p,g
        print("greatest no till now is :",p)
        g=h    #in first step on swapping with "p" "g" gets the value 0 in order restore original value which is stored in h we do this 
        g,l=l,g
    else:
        print("greatest number is ",p)
        continue
    