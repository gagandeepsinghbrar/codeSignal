def isArithmeticProgression(sequence):
    # since min length is 3 we can store the first computation for comparision
    result = sequence[1]-sequence[0]
    
    # loop from the second element till end
    for i in range(1,len(sequence)-1):
            
        # if you see a mismatch 
        if (sequence[i+1]-sequence[i])!=result:
            # not a AP
            return False
    # reached here then AP
    return True
            
        
    
    