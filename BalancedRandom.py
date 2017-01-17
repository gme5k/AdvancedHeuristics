from random import choice
from random import shuffle
from collections import Counter
from nationLoader import *
from visualization import *
from pick import pick

title, options = 'Please choose a nation: ', ["Ukraine.txt", "China.txt", "USA.txt", "Russia.txt"]
chosenNation, nationIndex = pick(options, title)

chosenNationPath = "TXT/" + chosenNation 

def balancedRandom(nationtxt):
    """
    Adapted Random algorithm that attempts to get an even number of transmittertypes per nationLoader
    Checks which transmitter is most common and removes this from options for following province
    Does not always succede 
    """
    transmitters = []

    while True:
        nation = nationLoader(nationtxt)

        try:
            province_names = []

            for province in nation:
                province_names.append(province)

            # Randomly shuffle list of province names
            shuffle(province_names)
         
            for province in province_names:

                transmitterOptions = range(1,5)

                # If province has no neighbours then assign random transmitter
                if not nation[province][0]:
                    nation[province][1] = choice(transmitterOptions)
                # If no transmitter is set yet choose random but not the same as the most common transmitter yet
                elif nation[province][1] == 0:
                    common = Counter(transmitters).most_common(1)

                    try:
                        most_common = common[0][0]
                        if most_common in transmitterOptions:
                            transmitterOptions.remove(most_common)
                    except:
                        # No most commont element exists yet so
                        pass

                    # Remove transmitters of neighbors from options
                    for neighbor in nation[province][0]:
                        if nation[neighbor][1] in transmitterOptions:
                            transmitterOptions.remove(nation[neighbor][1])

                    # Select random transmitter from options and assign it
                    transmitter = choice(transmitterOptions)

                    nation[province][1] = transmitter
                    transmitters.append(transmitter)
                    # print transmitters
            break
            
        except:
            # Empty the transmitters list
            print "trying"
            transmitters = []
            pass

    length = len(nation)

    # Check what desired balanced distribution would be with 4 transmittertypes
    if length % 4 == 0:
        print chosenNation[:-4], "has even number of provinces, so desired is all transmittertypes occuring", length/4, "times"       
    else:
        remainder = length % 4
        print chosenNation[:-4], "has uneven number of provinces. Remainder is", remainder
        print "Desired: 3 transm types occuring", (length - remainder) / 4, "and one type occuring", (length - remainder) / 4 + remainder,"times"

    for i in range(1,5):
        print i, "occurs", transmitters.count(i), "times"

    common = Counter(transmitters).most_common()[0][0] 
    print "So most common transmitter is", common

    colorNation(nation, chosenNation[:-4])

    return nation

balancedRandom(chosenNationPath)