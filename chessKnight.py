def chessKnight(cell):
    # has char ascii
    x=ord(cell[0])
    y=int(cell[1])
    print(x,y)
    count=0
    rangeX=range(97,105)
    rangeY=range(1,9)
    if x-1 in rangeX:
        
        if y+2 in rangeY:
            count=count+1
        if y-2 in rangeY:
            count=count+1
    if x+1 in rangeX:
        
        if y+2 in rangeY:
            
            count=count+1
        if y-2 in rangeY:
            count=count+1
            
    if x+2 in rangeX:
        if y+1 in rangeY:
            count=count+1
        if y-1 in rangeY:
            count=count+1
    if x-2 in rangeX:
        if y+1 in rangeY:
            count=count+1
        if y-1 in rangeY:
            count=count+1
    return count

