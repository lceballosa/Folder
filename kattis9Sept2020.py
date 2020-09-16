# Kattis 9Sept2020
import math
strin=input()
while(strin!="0.0 0"):
    entrada=strin.split()
    distancias=[]
    sweet=0
    sour=0
    found=False
    for i in range(int(entrada[1])):
        distancias.append(input().split())
        distancias[i]=[float(i) for i in distancias[i]]
    for i in range(len(distancias)):
        found=False
        for j in range(len(distancias)):
            if(found==False):
                dist=math.sqrt((distancias[i][0]-distancias[j][0])**2+(distancias[i][1]-distancias[j][1])**2) 
               # print("(",i,j,")", dist)
                if(i!=j and dist<=float(entrada[0])):
                    sour+=1
                    found=True
                    
    sweet= int(entrada[1])-sour
    print(str(sour) + " sour" + ", "+ str(sweet) + " sweet")
    strin=input()
    

        
            
    

