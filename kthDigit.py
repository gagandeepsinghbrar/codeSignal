def kthDigit(n, k):
    
    # check if number is too large to index the position
    if k>len(str(n)):
        return -1
    
    return int(str(n)[k-1])


