def plndrm():
    r=input("enter your word for palindrome checking :")
    s=r.replace(" ","")
    l=s.lower()
    print(l)
    if l==l[::-1]:
        print(r," is  palindrome")
    else :
        print(" is not a palindrome")
plndrm()