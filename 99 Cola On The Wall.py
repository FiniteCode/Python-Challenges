coke = 99
from time import sleep
while coke > 0:
    print (str(coke)+" bottles of cola on the wall.")
    print (str(coke)+" bottles of cola take one down, pass it around... \n")
    coke = coke-1
    if coke == 0:
        print ("No more cola on the wall, no more bottles of cola.")
        print ("Go to the store and buy some more, 99 bottles of cola on the wall.")
