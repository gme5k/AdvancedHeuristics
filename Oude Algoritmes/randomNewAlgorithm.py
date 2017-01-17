import random
from nationLoader import *
from visualization import *

Russia = nationLoader("TXT/Russia.txt")

def randomNewAlgorithm(nation):
    '''
    NOG NIET AF
    Start with 'truly' random province 
    '''
    options = [1, 2, 3, 4, 5, 6, 7]

    # Select random province from nation
    firstRandom = random.choice(nation.keys())
    firstNeighbors = nation[firstRandom][0]

    rand = random.choice(options)
    #low = min(options)
    nation[firstRandom][1] = rand

    print "Random province is", firstRandom, "and its neighbors are", firstNeighbors
    print "Its transmitter nr is", nation[firstRandom][1]
    print "-------------------"

    # Iterate over neighbors and assign valid transmitters
    def assignNeighborTransmitters(province):
        
        neighbors = nation[province][0]
        # Remove own transm from options
        try:
            options.remove(nation[province][1])
        except ValueError:
            print "Probably already removed"

        for neighbor in neighbors:
            LocalOptions = options[:]

            print "transmitterOptions:", options
            #neighborTransmitter = nation[neighbor][1]
            print "Neighbor is", neighbor, "and", neighbor, "'s neighbors are", nation[neighbor][0]
            # Find common neighbors
            commonNeighbors = set(neighbors) & set(nation[neighbor][0])
            print "Common neighbors are ", commonNeighbors

            # Remove transmitters of adjacent neighbors from options
            for commonNeighbor in commonNeighbors:
                print commonNeighbor, "transmitter:", nation[commonNeighbor][1]
                if nation[commonNeighbor][1] in options and nation[commonNeighbor][1] != 0:
                    try:
                        LocalOptions.remove(nation[commonNeighbor][1])
                    except ValueError:
                        print "Probably already removed"

            print "tranmitterOptionsLocal:", LocalOptions
                
            rand = random.choice(LocalOptions)
            #lowest = min(LocalOptions)

            # Assign random from transmitterOptions
            if nation[neighbor][1] == 0:
                nation[neighbor][1] = rand
                print neighbor, "; transmitter assigned:", nation[neighbor][1], "\n"

    #checkNeigborsOfNeighbor(firstRandom)
    assignNeighborTransmitters(firstRandom)
    print "Continue with: ", random.choice(firstNeighbors)

    return nation

randomNewAlgorithm(Russia)
colorNation(Russia, "Russia")