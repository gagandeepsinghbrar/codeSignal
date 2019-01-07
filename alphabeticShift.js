function alphabeticShift(inputString) {
   return inputString.split('').map(x=> x.charCodeAt()+1).map(y=>String.fromCharCode(y)).map(z=> z=='{' ? 'a' : z).join('')
  

   }