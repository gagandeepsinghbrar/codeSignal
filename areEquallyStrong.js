function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
  var you= yourLeft>yourRight ? yourLeft : yourRight
    var friend= friendsLeft>friendsRight ? friendsLeft : friendsRight
   return (yourLeft+yourRight)==(friendsLeft+friendsRight) && (you==friend)
   
}
