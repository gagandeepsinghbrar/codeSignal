function longestDigitsPrefix(inputString) { 
    if(!isNaN(Number(inputString))){
        if(inputString[0]==" "){return ""}
      else{return inputString}
    }
    var t=inputString.match(/[a-zA-Z]/)
    console.log(t)
    if(t){
   if(t['index']==0){return ""}
    }
    if(inputString.indexOf(t)==0){return ""}
   //inputString.slice(0,inputString.match(/[a-zA-Z]/).index)
   if(!t){
       return inputString
   }
   if(!Number(inputString.slice(0,inputString.match(/[a-zA-Z]/).index))){
       return ""
   }
    else{
        return inputString.slice(0,inputString.match(/[a-zA-Z]/).index)
    }
}