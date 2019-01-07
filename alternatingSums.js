function alternatingSums(a) {
    if(a.length!=1){
    odd=a.filter((a,inx)=> inx%2==0).reduce((x,y)=>x+y)
    console.log(odd)
    even=a.filter((a,inx)=> inx%2==1).reduce((x,y)=>x+y)
    console.log(even)
    }
    else{
        odd=a[0]
        even=0
    }
   return [odd,even]
   }