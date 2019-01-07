function arrayMaximalAdjacentDifference(inputArray) {
   var temp= inputArray.indexOf(Math.max(...inputArray))
   var toSub= inputArray[temp-1]< inputArray[temp+1] ? inputArray[temp-1] : inputArray[temp+1]
  if(inputArray[temp+1]==undefined){
   toSub= inputArray[temp-1]
  }
   return inputArray[temp]-toSub
   
}
