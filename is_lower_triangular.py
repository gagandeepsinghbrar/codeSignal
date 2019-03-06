def isLowerTriangularMatrix(matrix):
    bound=len(matrix[0])
    
    for i in range(bound):
        
        for j in range(i+1,bound):
            
            if matrix[i][j] != 0:
                return False
            
    return True
        


