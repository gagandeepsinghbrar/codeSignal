function sortByHeight(a) {
    var inx=[]
  for(i in a){
    if(a[i]==-1){
        inx.push(Number(i))
    }
  }
  var restof= a.filter(x=> x!=-1).sort((a,b)=> a-b)
 for(i in inx){
     restof.splice(inx[i],0,-1)
 }
return restof
}