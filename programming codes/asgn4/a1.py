st=input("entre your string :")
t=input("enter word to be checked in hte entered string :")
if st.find(t)!=-1:
    print("entered word exists in the entered string","no of occurences are",st.count(t))
else :
    print("entered word doesnot exist in the entered string")
