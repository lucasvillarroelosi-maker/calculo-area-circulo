import math
#Paso 1: Solicitaral usuario que ingrese el radio del circulo



circulo = float(input("Ingrese el area del circulo: "))
#Paso 2:Calcular el area del circulo utilizando la formula area = pi *radio^2
area = math.pi * (circulo**2)

#Paso 3:Mostrar al usuario el area calculada 

print("El area del circulo con radio", circulo, "es", area)    