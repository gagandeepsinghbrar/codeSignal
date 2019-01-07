def boxBlur(image):
    return [[sum(sum(x[i:i+3]) for x in image[j:j+3])/9 
                                   for i in range(len(image[0])-2)] 
                                   for j in range(len(image)-2)]

