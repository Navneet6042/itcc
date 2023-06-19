import math as m 
for i in range(0,346,15):
    snvl=round(m.sin(i),4)
    csvl=round(m.cos(i),4)
    print(i,"----",snvl," ",csvl)