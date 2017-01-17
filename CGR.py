from random import *
import json
from nationLoader import *

def clusterGreedyRandom(nationtxt):
    """
    Make cluster around province with most neighbors like ABABAB

    Then fill in rest of nation with greedyRandom

    Uncomment all ### to visualize in steps
    """
    ### stepcounter = 0

    while True:
        # Cluster Algorithm part
        provinceNames = []
        nation = nationLoader("TXT/" + nationtxt)
        
        for province in nation:
            provinceNames.append(province)
        
        neighborCount = {}

        for province in nation:
            neighborCount.update({province:len(nation.get(province)[0])})
            
        # Sort
        neighborCountSorted = sorted(neighborCount, key = neighborCount.__getitem__,reverse = True)
        
      
        for province in neighborCountSorted:
            conflict = False
            
            if nation.get(province)[1] == 0:
                
                # If neighbor has a transmitter, don't assign transmitters to group
                for neighbor in nation.get(province)[0]:
                    
                    if nation.get(neighbor)[1] != 0:
                        conflict = True
                        break
                    
                    # If neighbour of neighbour has transmitter, don't...
                    for neighbor2 in nation.get(neighbor)[0]:
                        
                        if nation.get(neighbor2)[1] != 0:
                            conflict = True
                            break
                        
                # Else assign transmitters to group as ABABAB...
                if conflict == False:
                    
                    
                    if len(nation[province][0]) > 1:
                        c = 0
                        
                        # even case
                        if len(nation[province][0]) % 2 == 0:
                            nation[province][1] = 3
                            
                            for neighbor in nation[province][0]:
                                x = c % 2 + 1
                                nation[neighbor][1] = x
                                c += 1
                        
                        #uneven case
                        else:
                            nation[province][1] = 3
                            maximum = 0
                            
                            for neighbor in nation[province][0]:
                                
                                if len(nation[neighbor][0]) > maximum:
                                    maximum = len(nation[neighbor][0])
                                    mostNeighborProvince = neighbor
                                    
                            nation[mostNeighborProvince][1] = 4
                            
                            for neighbor in nation[province][0]:
                                
                                if nation[neighbor][1] == 0:
                                    x = c % 2 + 1
                                    nation[neighbor][1] = x
                                    c += 1
                                    
                    # 1 neighbor                
                    elif len(nation[province][0]) > 0:
                       
                    
                    # 0 neighbor
                        nation[province][1] = 2
                        nation[province][0][0] = 1 
                    elif len(nation[province][0]) == 0:
                        nation[province][1] = 1

        # GreedyRandom part
        try:    
            # Randomly shuffle list of province names
            shuffle(provinceNames)
         
            for province in provinceNames:
                transmitterOptions = [1, 2, 3, 4, 5, 6, 7]

                # If province has no neighbours then assign transm 1
                if not nation[province][0]:
                    nation[province][1] = 1
                elif nation[province][1] == 0:
                    # Remove neighbor transmitters from options
                    for neighbor in nation[province][0]:
                        if nation[neighbor][1] in transmitterOptions:
                            transmitterOptions.remove(nation[neighbor][1])

                    # Select first transmitter from options and assign it
                    transmitter = transmitterOptions[0]
                    nation[province][1] = transmitter

                    ### stepcounter = stepcounter + 1
                    ### jsonPath = "JSON/" + nationtxt[:-4] + "/Step" + str(stepcounter) + ".txt"
                    ### json.dump(nation, open(jsonPath,'w'))
            break
            
        except IndexError:
            print nation
            pass

    return nation
