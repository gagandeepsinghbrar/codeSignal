function addBorder(picture) {
  var total= picture.length
  // things needed 
  
  var requiredWidth=picture[0].length+2
  var requiredHeight=total+2
  for(i in picture){
      picture[i]="*"+picture[i]+"*"
  }
  picture.unshift("*".repeat(requiredWidth))
  picture.push("*".repeat(requiredWidth))
  return picture
}