from nationLoader import *

def clusterAlgorithm(nationtxt):
    openName = "TXT/" + nationtxt
    nation = nationLoader(openName)
    neighborCount = {}
    
    for province in nation:
        neighborCount.update({province:len(nation.get(province)[0])})
        
    neighborCountSorted = sorted(neighborCount, key=neighborCount.__getitem__,reverse = True)
    
  
    for province in neighborCountSorted:
        conflict = False
        
        if nation.get(province)[1] == 0:
            
            # if neighbor has a transmitter, don't assign transmitters to group
            for neighbor in nation.get(province)[0]:
                
                if nation.get(neighbor)[1] != 0:
                    conflict = True
                    #~ print 'level 1 conflict'
                    break
                #~ print 'through 1st level check'
                
                # if neighbour of neighbour has transmitter, don't...
                for neighbor2 in nation.get(neighbor)[0]:
                    
                    if nation.get(neighbor2)[1] != 0:
                        conflict = True
                        #~ print 'level 2 conflict'
                        break
                    #~ print 'through 2nd level check'
                    
            # else assign transmitters to group
            if conflict == False:
                #~ print province
                
                if len(nation.get(province)[0]) > 1:
                    c = 0
                    
                    if len(nation.get(province)[0]) % 2 == 0:
                        nation[province][1] = 3
                        
                        for neighbor in nation.get(province)[0]:
                            x = c % 2 + 1
                            nation[neighbor][1] = x
                            #~ print x
                            c += 1
                            
                    else:
                        nation[province][1] = 3
                        maximum = 0
                        
                        for neighbor in nation.get(province)[0]:
                            
                            if len(nation.get(neighbor)[0]) > maximum:
                                maximum = len(nation.get(neighbor)[0])
                                mostNeighborProvince = neighbor
                                
                        nation[mostNeighborProvince][1] = 4
                        
                        for neighbor in nation.get(province)[0]:
                            
                            if nation.get(neighbor)[1] == 0:
                                x = c % 2 + 1
                                nation[neighbor][1] = x
                                #~ print x
                                c += 1
                                
                elif len(nation[province][0]) > 0:
                       
                    
                        nation[province][1] = 2
                        nation[province][0][0] = 1 
                        
                elif len(nation[province][0]) == 0:
                    nation[province][1] = 1
    return nation
