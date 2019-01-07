function adjacentElementsProduct(inputArray) {
  temp=-Infinity;
  for(var i=0;i<inputArray.length-1;i++){
    if((inputArray[i]*inputArray[i+1])>temp)
    temp=inputArray[i]*inputArray[i+1]
  }
  return temp;
}
