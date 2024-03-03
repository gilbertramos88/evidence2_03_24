# parametros
altura = (float(input("ingresar altura  :")))
base =  (float(input("ingrese base:  ")))
radio = (float(input("ingrese radio:  ")))
pi = (3.1415)
v =  (pi * (radio**2) * altura)
area = (2 * pi * (radio**2)+(2*pi)*radio*altura)

if altura or base or radio < 0 :

    print (F"el volumen del cilindro es {v}")
    print (f"el area del cilindro es {area}")
else: 

  print ("parametros invalidos")


