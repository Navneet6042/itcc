j=int(input("how many questions you want to do :"))
for l in range(0,j):
    import random as r 
    d=r.randint(1,9)
    h=r.randint(1,9)
    print(d,"X",h,"=")
    r=int(input(" your answer for above question :"))
    if r==d*h:
        print("yayy ! you got it right :")
    else :
        print("wrong answer .Right answer is :",d*h)
print("thats all you asked for.")