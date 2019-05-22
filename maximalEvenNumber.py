def maximalEven(inputArray):
    # assume temp is not known yet
    temp = -1
    
    # start looping over all elements
    for elem in inputArray:
        # make sure it is even and larger than the result so far.
        if elem>temp and elem%2==0:
            # swap temp with new candidate
            temp= elem
            
    
    return temp