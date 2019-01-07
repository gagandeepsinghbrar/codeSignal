def electionsWinners(votes, k):
    if k==0:
        
        decision=votes.count(max(votes))
        if decision==1:
            return 1
        if decision==True:
            return 0
        
    max_num=max(votes)
    return len(list(filter(lambda x:x>max_num,list(map(lambda x:x+k,votes)))))
    
    