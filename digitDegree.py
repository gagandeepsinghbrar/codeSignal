def digitDegree(n):
    count=0
    if n<10:
        return 0
    while n>=10:
        count=count+1
        n=sum([int(digit) for digit in str(abs(n))])
    return count
    
    

