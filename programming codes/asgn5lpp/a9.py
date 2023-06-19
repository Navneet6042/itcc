o=int(input("how many number of words do you want to enter :"))
count=0
ll=[]
for i in range(0,o):
    n=(input("enter the list :"))
    ll.append(n)
w=input("enter word to count is occurence :")

for ini in range(0,o):
    if ll[ini]==w:
        count+=1
    else :
        continue
print(ll)
print("number of occurances of the given word =",count)