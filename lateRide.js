function lateRide(n) {
    var mn=String(n%60).split('').map(a=> Number(a)).reduce((a,b)=>a+b)
    var hr=String(Math.trunc(n/60)).split('').map(a=> Number(a)).reduce((a,b)=>a+b)
    return mn+hr
    /* all rights reserved */
}
