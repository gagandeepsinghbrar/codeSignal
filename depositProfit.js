function depositProfit(deposit, rate, threshold) {
    var count=1;
    while(true){
        deposit=deposit+(deposit*(rate/100));
       if(deposit>=threshold){
         return count
       }
       else{count++;}
    }
 }
