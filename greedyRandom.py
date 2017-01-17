from random import *
import json
from nationLoader import *

def greedyRandom(nationtxt):
    '''
    Shuffle list of provinces and loop over this list and assign transmitters

    Uncomment all ### to visualize in steps
    '''
    ### stepcounter = 0

    while True:
        #Buiten try loop 
        provinceNames = []
        nation = nationLoader("TXT/" + nationtxt)
        
        for province in nation:
            provinceNames.append(province)

        try:            
            # Randomly shuffle list of province names
            shuffle(provinceNames)
            aCount = 0
            bCount = 0
            cCount = 0
            dCount = 0
            eCount = 0
            fCount = 0
            gCount = 0
            
         
            for province in provinceNames:
                transmitterOptions = [1, 2, 3, 4, 5, 6, 7]

                # If province has no neighbours then assign transm 1
                if not nation[province][0]:
                    nation[province][1] = 1
                elif nation[province][1] == 0:
                    # remove neighbor transmitters from options
                    for neighbor in nation[province][0]:
                        if nation[neighbor][1] in transmitterOptions:
                            transmitterOptions.remove(nation[neighbor][1])

                    # select first transmitter from options and assign it
                    transmitter = transmitterOptions[0]
                    nation[province][1] = transmitter
                    if transmitter == 1:
                        aCount += 1
                    elif transmitter == 2:
                        bCount += 1
                    elif transmitter == 3:
                        cCount += 1
                    elif transmitter == 4:
                        dCount += 1
                    elif transmitter == 5:
                        eCount += 1
                    elif transmitter == 6:
                        fCount += 1
                    elif transmitter == 7:
                        gCount += 1

                    ### stepcounter = stepcounter + 1
                    ### jsonPath = "JSON/" + nationtxt[:-4] + "/Step" + str(stepcounter) + ".txt"
                    ### json.dump(nation, open(jsonPath,'w'))
            break
            
        except:
            pass

    return nation, aCount, bCount, cCount, dCount, eCount, fCount, gCount
