# leap year
year = (int(input("what year is? on number! ")))
a =  ( year % 4)
if a == 0:
    print ("leap year")
elif a > 1:
    print ("no year leap")
