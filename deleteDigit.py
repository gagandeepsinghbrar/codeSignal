def deleteDigit(n):
    convr=list(map(lambda x: int(x),str(n)))
    assumed=0
    for i in range(len(convr)):
        tocheck=convr[:]
        tocheck.pop(i)
        tocheck=int("".join([str(j) for j in tocheck]))
        if tocheck > assumed:
            assumed=tocheck

    return assumed
        
