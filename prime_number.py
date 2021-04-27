number = int(input("enter a number() :"))
if number >= 2 :
    for i in range(2,number):
        if (number % i) == 0 : 
            print("{} is a prime number".format(number))
            break
        else :
            print("{} is a prime number".format(number))
            break
else:
    print("{} is not a prime number".format(number))
    
