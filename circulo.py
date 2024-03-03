# area de circulo
#parametros de funcionamiento!!!
print ("ingrese parametros")
pi = 3.1416
radio = float(input("ingresa el radio de el circulo:  "))
perimetro = ((2*pi) * radio)
area = str(pi*(radio**2))

if radio > float (0) :
   print (f"el radio de el circulo es {radio}")
   print (f"el area del circulo es {area} cm^2")
   print (f"el perimetro del circulo es {perimetro} ")
else:
   print ("error de parametros")
