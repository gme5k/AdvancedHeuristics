from nationLoader import *

def greedyByNeighbor(nationtxt):
    '''
    Starts with province with most neighbors
    '''
    nation = nationLoader(nationtxt)
    neighborCount = {}
    for province in nation:
        neighborCount.update({province:len(nation.get(province)[0])})
        
    neighborCountSorted = sorted(neighborCount, key=neighborCount.__getitem__,reverse=True)
    
    for province in neighborCountSorted:
        transmitterOptions = [1, 2, 3, 4, 5, 6, 7]

        if nation[province][1] == 0:
            # remove neighbor transmitters from options
            for neighbor in nation[province][0]:
                if nation[neighbor][1] in transmitterOptions:
                    transmitterOptions.remove(nation[neighbor][1])
                    # print 'removed: ', nation.get(neighbor)[1]
            
            bestOption = transmitterOptions.index(min(transmitterOptions))
            bestTransmitter = transmitterOptions[bestOption]
            nation[province][1] = bestTransmitter
            
            # print 'province: ', province
            # print 'neighbors: ', nation.get(province)[0]
            # print "options are: ", transmitterOptions
            # print "choice: ", bestTransmitter
            # print "\n"
    return nation
