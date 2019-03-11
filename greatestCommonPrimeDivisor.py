def greatestCommonPrimeDivisor(a, b):
    # try possibilities till 150 due to constraints
    for num in range(3,150):
        
        # well it has to give 0 remainder with a and b and it is a prime number
        if a%num==0 and b%num==0 and isPrime(num):
            
            # that's our guy!
            return num
        
    # otherwise it doesn't exist
    return -1



def isPrime(n):
    # check if the number is prime or not
    for i in range(2,n):
        # well if it divides any number perfectly from 2 till n-1 we say it's not dude.
        if n%i==0:
            # ok stop it
            return False
    # yup found it !
    return True