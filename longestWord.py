def longestWord(t):
    s = re.split('[^a-zA-Z]',t)
    return max(s,key=len)