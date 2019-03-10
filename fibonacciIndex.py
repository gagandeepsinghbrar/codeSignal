def inRange(num,sum):
    
    # target range << Special case >>
    if num==2:
        return sum>=10 and sum<100
    # otherwise just figure out the range
    else:
        
        return sum>=10**(num-1) and sum<(1000**(num+1))

def fibonacciIndex(n):
    # left side number
    first=0
    # right side number
    second=1
    
    # if i'm asked for the 1 decimal number
    if n==1:
        return 0
    
    # keep track of index we are checking
    index=1
    
    # current sum 
    sum=0
    
    while True:
        
        # temporarily save the left side number
        t= first
        # find next number
        sum= first + second
        
        # if the number is in the range
        if inRange(n,sum):
            
            # stop and give the index
            return index
        
        # put the sum as left side for next turn
        first = sum
        
        # put the left side we preserved earlier on right side
        second = t
        
        # update the index for next turn
        index+=1




