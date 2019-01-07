function differentSymbolsNaive(s) {
   return new Set(s.replace(/&\w+\b|;/g, '')).size
   
}
