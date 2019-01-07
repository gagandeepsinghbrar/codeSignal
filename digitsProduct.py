def digitsProduct(product):

    store = []
    answer = 0
    #cases that have to predecided
    if product == 0:
        return 10

    if product == 1:
        return 1

    # rest of the cases
    for divisor in range(9, 1, -1):
        
        
        while product % divisor == 0:
            product /= divisor
            store.append(divisor)
    result="".join(map(lambda n: str(n) ,(sorted(store))))
    
    if product > 1:
        return -1

    
    return int(result)