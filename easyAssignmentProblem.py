def easyAssignmentProblem(skills):
    
    # special case where employee TWO does both jobs equally
    if skills[1][0]==skills[1][1]:
        # worry about how employee ONE would do
        if skills[0][0]>skills[0][1]:
            
            first = 1
            second = 2
        else:
            first =2 
            second =1
    else:
         # special case where both employees do first job equally 
        if skills[0][0]==skills[1][0]:
            # let's check if who does the second job better
            if skills[0][1]> skills[1][1]:
                
                first = 2
                second = 1
            else:
                first =1 
                second = 2
            
        else:
            
            # no special case 
            # Store the better performer for first job
            first = 1 if skills[0][0]> skills[1][0] else 2
            # Similarly store the better performer for first job
            second = 2 if first ==1  else 1
        
    return [first,second]
    
    


