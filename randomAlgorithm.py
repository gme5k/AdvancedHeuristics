from random import choice
from random import shuffle
from nationLoader import *

def randomAlgorithm(nationtxt):

    while True:
        try:
            provinceNames = []
            openName = "TXT/" + nationtxt
            nation = nationLoader(openName)

            for province in nation:
                provinceNames.append(province)

            shuffle(provinceNames)
         
            for province in provinceNames:
                transmitterOptions = [1, 2, 3, 4, 5, 6, 7]

                
                

                # Set transmitter if it is not set yet
                if nation[province][1] == 0:
                    # If province has no neighbours then assign random transmitter
                    if len(nation[province][0]) == 0:
                        nation[province][1] = choice(transmitterOptions)
                    # Remove neighbor transmitters from options
                    else:
                        for neighbor in nation[province][0]:
                            if nation[neighbor][1] in transmitterOptions:
                                transmitterOptions.remove(nation[neighbor][1])
                    
                        # Select random transmitter from options
                        nation[province][1] = choice(transmitterOptions)
    
            break
            
        except:
            pass
        
    return nation
