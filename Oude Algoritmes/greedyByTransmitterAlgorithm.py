from random import *
from nationLoader import *

def greedyByTransmitterAlgorithm(nationtxt):
    nation = nationLoader(nationtxt)
    neighborCount = {}
    for province in nation:
        neighborCount.update({province:len(nation.get(province)[0])})
        
    neighborCountSorted = sorted(neighborCount, key=neighborCount.__getitem__)
    
    transmitterList = [1, 2, 3, 4, 5, 6, 7]
    
    #for each transmitter type
    for transmitter in transmitterList:
        #~ print 'passing ', transmitter
        
        for province in neighborCountSorted:
            conflict = False
            
            if nation.get(province)[1] == 0:
                
                # if neighbor has the same transmitter, don't assign current transmitter to province
                for neighbor in nation.get(province)[0]:
                    if nation.get(neighbor)[1] == transmitter:
                        conflict = True
                        #~ print 'conflict'
                        break
                
                # else assign current transmitter to province
                if conflict == False:
                    nation[province][1] = transmitter
    return nation
