def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


text = "ATTACKATONCE"
s = 0
while(s<25) :
   print ("Text : " + text)
   print ("Shift : " + str(s))
   print ("Cipher: " + encrypt(text,s))
   s+=1 
   print('\n')