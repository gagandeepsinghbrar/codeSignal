def growingPlant(upSpeed, downSpeed, desiredHeight):
    # current height 
    current = 0
    
    # the count will be zero days 
    count=0
    
    # keep growing the plant forever
    while True:
        
        # increase the current height by once shot
        current+= upSpeed
        # one day has passed !
        count+=1
        
        # if the height has reached the height we like we can stop
        if current >=desiredHeight:
                # tell em how many days it took
                return count
        # if not desired height let is decrease at night
        current-=downSpeed