
# 
a= (int(input("insert dividend:  ")))
b = (int(input("insetr divisor:  ")))
c = (a // b)
d = (a % b)
if  b >  1 :
    if a > b:
          print ("the quotient is: ", (c))
          print ("the residue is: ",  (d))
    else:
         print (a/b)      
else:
    print ("invald numbers")
    
if b == 0:
    print ("invald numbers")
