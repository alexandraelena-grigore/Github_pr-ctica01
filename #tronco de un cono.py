#Tronco de un cono

import math
PI = math.pi

repetir = True

print("Càlcul de l'àrea i el volum d'un tronc de con")
r = int(input("Introduce el valor del radio menor: r =  "))
R = int(input("Introduce el valor del radio mayor: R =  "))
h = int(input("Introduce el valor de la altura: h =  "))
g = int(input("Introduce el valor de la generatriz: g =  "))

while repetir == True:
    
    A = PI * (g*(r + R) + (r * r)+(R *R ))
    print("L'àrea del tronc d'un con és de: ",round(A,3))
    V = PI * h *((R*R)+(r*r)+R*r)/3
    print ("El volum del tronc d'un con és de: ",round (V,3))
    
r = int(input("Quieres repetir el proceso? [si/no] "))
if (r == "no"):
    repetir = False
