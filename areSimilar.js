function areSimilar(a, b) {
  
  tempcounter=0;
  for(i in a){
    
     if((a[i]!=b[i])){
       ++tempcounter;
      
    }
    if(tempcounter>2){return false}
  }
  var start,end;
  count=0;
  for(i in a){
     if(count==1&&(a[i]!=b[i])){
       count++;
      end=i;
    }
    if(count==0&&(a[i]!=b[i])){
      
      count++;
      start=i;
      
    }
   
    console.log(start,end)
    if(start&&end){
      if( (a[start]==b[end] )&&(a[end]==b[start])){
                                    return true
                                    }
      else{return false}
     
    }
  }
  return true
}
