function swapCase(text) {

    
    // convert the string to list and then map it 
    // use the basic way of uppercasing and comparing with original to check if it is lower case or upper case. If it is upper case
    // you can lower it.
    return text.split("").map(char =>{
        return char== char.toUpperCase() ? char.toLowerCase(): char.toUpperCase()
            
       
        
    }).join("")
}

