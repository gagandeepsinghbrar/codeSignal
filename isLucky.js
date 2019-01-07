function isLucky(n) {
  var left=0;
  var right=0;
  var temp=String(n).split('').map(x=>Number(x))
  for(i in temp){
    if(i<temp.length/2){
      left+=temp[i]
    }
    else{
      right+=temp[i]
    }
  }
  if(left==right){
    return true;
  }
  else{
    return false
  }
}