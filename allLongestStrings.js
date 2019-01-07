function allLongestStrings(inputArray) {
 return inputArray.filter(i=> i.length)==Math.max.apply(null,inputArray.map(n=> n.length))
}
