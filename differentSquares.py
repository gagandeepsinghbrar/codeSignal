def differentSquares(matrix):
    comb=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            sm=str(matrix[i][j])+str(matrix[i][j+1])+str(matrix[i+1][j])+str(matrix[i+1][j+1])
            if sm not in comb:
                comb.append(sm)
                
    return len(comb)

