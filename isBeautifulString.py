def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    print(r)
    print(r[::-1])
    print(sorted(r))
    return r[::-1] == sorted(r)