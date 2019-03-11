def newRoadSystem(roadRegister): 
        # easier access to the length
        n=len(roadRegister)
        
        # loop over the main list
        for node in range(len(roadRegister)):
        
        
                # refer to the nth list in the matrix
                lst = roadRegister[node]
                # count number of connections from that node
                total = sum(lst)
                        
                other = []
                
                for i in range(n):
                        # store the connected nodes in other
                        other.append(roadRegister[i][node])
                # the sum of the nodes coming back should be the same
                if sum(other)!=total:
                        # if it was not we can stop since it is not correct
                        return False
        # if we reach here it's all good.
        return True