def validTime(time):
    if time=="24:00":
        return False
    
    return int(time.split(':')[0]) in range(1,24) and int(time.split(':')[1]) in range(0,60)

