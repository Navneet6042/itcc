u=[]
d=[1,2,3,45,-3,44,-23]
for i in d:
    for j in d:
        for k in d:
            if i+j+k==0:
                u.append(i)
                u.append(j)
                u.append(k)
                u.append("==")
                #group of threee number is seperated by ""==""
print(u)
