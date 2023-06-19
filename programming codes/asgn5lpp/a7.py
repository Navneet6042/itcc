y=[]
for i in range(1,501):
    if i%7==0 and i%11==0:
        y.append(i)
    else :
        continue
print("required numbers are \n",y)