function palindromeRearranging(inputString) {
    var temp=inputString.split('').sort()
    
   for(var i=0;i<temp.length-1;i++){
       
       if(temp[i+1]==temp[i]){
           delete temp[i]
           delete temp[i+1]
       }
   }
   if(temp.filter(x=> x!=undefined).length>1){
       return false;
   }
   return true
}