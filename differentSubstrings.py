def differentSubstrings(inputString):
    
    # total substrings initialization
    totalSubs=0
    
    l = len(inputString)
    
    # check all sized strings
    for length in range(1,l):
        
        # have a storage to keep track of non duplicates
        storage=[]
        
        for traverseIndex in range(0,l-length+1):
            
            # sliced portion
            n = inputString[traverseIndex:traverseIndex+length]
            
            # only add if non duplicate
            if n not in storage:
                storage.append(n)
                
        # count how many strings found for a particular length
        totalSubs+=len(storage)
        
    return totalSubs+1

