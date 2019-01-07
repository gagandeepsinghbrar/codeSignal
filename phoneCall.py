def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    else:
        minutes1=s/min1
        rem_balance=s-(minutes1*min1)
        
        
        if(rem_balance>=min2_10):
            if(rem_balance>min2_10):
                minutes2=minutes1/min2_10
                rem_balance=rem_balance-(minutes2*min2_10)
                if(rem_balance>=min11):
                    if(rem_balance>min11):
                        minutes3=
            else:
                return minutes1+(rem_balance/min2_10)
            
        else:
            return minutes1
