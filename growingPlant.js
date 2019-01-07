function growingPlant(upSpeed, downSpeed, desiredHeight) {
   height=0
   count=0
   if(upSpeed>=desiredHeight){return 1}
   while(true){
      count++
      height+=upSpeed
      
      if(height>=desiredHeight){return count}
      
      height-=downSpeed
      
      
      
   }
}
