def sudoku(grid):
    print(validRow(grid))
    print(validCol(grid))
    print(validGrids(grid))
    return validRow(grid) and validCol(grid) and validGrids(grid)
    
    
    
def validRow(grid):
    return len(grid)==len(list(filter(lambda row: all([(i in row) for i in range(1,10)]) ,grid)))
    

def validCol(grid):
    return validRow([[grid[j][i] for j in range(0,len(grid))]for i in range(0,len(grid))])
    

def validGrids(grid):
    #took me forever to come up -.-
    gridData=[[grid[j][i:i+3]+grid[j+1][i:i+3]+grid[j+2][i:i+3]for j in [0,3,6]]for i in [0,3,6]]
    gridData=gridData[0]+gridData[1]+gridData[2]
    return validRow(gridData)
    