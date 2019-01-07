function isMAC48Address(inputString) {
    var patt = new RegExp(/^([\dA-F]{2}-){5}([\dA-F]{2})$/);
    return patt.test(inputString);
}