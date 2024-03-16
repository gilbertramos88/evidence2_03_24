# suma de numeros
a = (int(input("enter firs number:  ")))
b = (int(input("enter second number:  ")))
c = (a + b)# if a is minor than b
d = (a - b)# if a is greater than b
if  b <= 0:
    if a < b :
        print (c)
    else :
        print (d)
else:
    print ("invalid numbers, some is negative...")        