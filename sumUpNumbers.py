def sumUpNumbers(inputString):
    if not any(list(map(lambda x: x.isnumeric(),list(inputString)))):
        return 0
    else:
        try:
            x=str(inputString)
            return int(inputString)
        except:
            pass
        return sum(list(map(lambda y: int(y),list(filter(lambda x:x.isnumeric(),re.split('[^0-9]',inputString))))))
        
    

