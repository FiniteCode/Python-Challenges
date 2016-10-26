range_max = int(input("Maximum: "))
num1 = 0
num2 = 1
num = 0
print ("0")
print ("1")
while num <= range_max:
    num = num1+num2
    num1 = num2
    num2 = num
    if num <= range_max:
        print (num)
