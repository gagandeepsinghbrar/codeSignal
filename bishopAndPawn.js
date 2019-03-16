function bishopAndPawn(bishop, pawn) {
	// added first random to avoid indexing naturality
    charArr=['XXX','a','b','c','d','e','f','g','h']
    
     var bsh= charArr.indexOf(bishop[0])+bishop[1]
     var pwn= charArr.indexOf(pawn[0])+pawn[1]
     return Math.abs(bsh[0]-pwn[0])==Math.abs(bsh[1]-pwn[1])
   
}
