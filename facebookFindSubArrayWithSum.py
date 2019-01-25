def findSub(lst,total):

    hMap={}
    sum=0
    for itemNo in range(len(lst)):

        sum=sum+lst[itemNo]

        hMap[sum]=itemNo

        if sum-total in hMap:

            return lst[hMap[sum-total]+1:itemNo+1]


result=findSub([3,4,6,8,56,4,3,3,654,43,65],68)
print(result)