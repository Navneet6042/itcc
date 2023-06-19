m=int(input("enter your marks  :"))
if m>80:
    print("your got A grade")
if m in range(60,81):
    print("you got B grade")
if m in range(50,61):
    print("you got C grade")
if m in range (45,50):
    print("you got D grade")
if m in range(25,46):
    print("you got E grade")
if m<25:
    print("you got F grade")