function commonCharacterCount(s1, s2) {
    r1= s1.split('')
    r2= s2.split('')
    count=0;
    for(i in r1){
        for(j in r2){
          
            if(r1[i]==r2[j]){
                r2.splice(j,1);
                count++;
                break;
            }
           
        }
       
       
    }
    return count
    }