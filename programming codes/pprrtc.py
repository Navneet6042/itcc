o=[2,2,4,1,3,4,3]
pp=[]
for i in o:
    count=0
    for j in range(len(o)):
        if o[j]==i:
            count+=1
        else:
            continue
    print(i,"occured",count,"times")
    pp.append(i)
    