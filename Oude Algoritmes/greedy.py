from random import *
from numpy import *
from nationLoader import *

def greedy(nationtxt):
    nation = nationLoader(nationtxt)
    neighborCount = {}
    for province in nation:
        neighborCount.update({province:len(nation.get(province)[0])})
        
    neighborCountSorted = sorted(neighborCount, key=neighborCount.__getitem__)
    

    for province in neighborCountSorted:
        transmitterOptions = [1, 2, 3, 4, 5, 6, 7]
        
        if nation[province][1] == 0:
            print 'yes'
            # remove neighbor transmitters from options
            for neighbor in nation[province][0]:
                if nation[neighbor][1] in transmitterOptions:
                    transmitterOptions.remove(nation[neighbor][1])

            # select best transmitter from options and assign it
            transmitter = transmitterOptions[0]
            nation[province][1] = transmitter
    
            
    #~ print "--------------------------------"
    return nation
