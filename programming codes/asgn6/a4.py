def pngm(s):
    print("your entered string is :",s)
    s=s.replace(" ","")
    s=s.lower()
    print(s)
    for i in range(97,113):
        if s.find(chr(i))!=-1:
            if i==112:
                print("is a pangram")
            else:
                continue
            
        else:
            print(chr(i),"is not present")
            print("not a panagram")
            break
        
pngm("a quick brown fox jumps over the  lazy dog")