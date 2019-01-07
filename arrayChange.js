function arrayChange(inputArray) {
    var count=0;
    var i=0;
  while(i<inputArray.length-1){
     while(!(inputArray[i+1]>inputArray[i])){
        inputArray[i+1]++;
        count++;
     }
      i++;
  }
  return count
}
