const arrayMaxConsecutiveSum = (a, k) => {
    let s = 0;

    for (let i = 0; i < k; i ++) {
        s += a[i];           
    }
    
    let max = s;
    
    for (let i = k; i < a.length; i++) {
        s -= a[i-k] - a[i];
        if (s > max) {
            max = s;
        } 
    }
    
    return max;
}
