def digitDegree(n):
    # let's assume the degree is 0 
    degree=0
    
    while n>9:
        # we came in the loop. So increase the degree
        degree+=1
        
        # add all the digits quickly by converting to string and mapping to integers
        n= sum(map(lambda x: int(x),str(n)))
        
    # if n is one digit we stop adding and give the result back
    return degree
        


