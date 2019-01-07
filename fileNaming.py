def fileNaming(names):
    results=[]
    for name in names:
        if name not in results:
            results.append(name)
        else:
            
            results.append(generateNext(name,results))
            print("results became "+str(results))
            
    return results

def generateNext(passedName,result):
    # if passedName=="a":
    #     print("-------------------------")
    #     print("result is "+str(result))
    #     print("passedName is "+str(passedName))
    #     print("-------------------------")
    count=0
    convertedName=""
    for item in result:
        
        if passedName==item:
            
            count=count+1
            
        # check if dd has only one bracket after it : dd is nm
        else:
            
            convertedName="".join(map(lambda y: '\)' if y==')' else y,list(map(lambda x: '\(' if x=='(' else x,list(passedName)))))
            checker=re.compile('^{}\(\d\)$'.format(convertedName))
            
            
            if checker.match(item):
                
                count=count+1
                
    #---------------- Figure out what to return back --------------
    #
    #
    #
    #
    #
    #
    #
    #
    for j in range(1,len(result)+1):
        if passedName+'('+str(j)+')' not in result:
            return passedName+'('+str(j)+')'
    return passedName+'('+str(count)+')'
            