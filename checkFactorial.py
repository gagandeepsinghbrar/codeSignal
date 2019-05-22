def checkFactorial(n):
    # assume the first number to be base case
    assumed = 1
    count = 1
    # while the numbers is less
    while assumed<= n:
        if assumed==n:
            return True
        
        assumed = assumed * count
        count = count + 1
        
    return False