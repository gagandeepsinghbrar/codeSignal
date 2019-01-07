def messageFromBinaryCode(code):
    decoded=""
    for i in range(0,len(code),8):
        decoded+=chr(int(code[i:i+8],2))
    return decoded

