function evenDigitsOnly(n) {
  return String(n).split('').filter(x=> x%2==0).length==String(n).length
}
