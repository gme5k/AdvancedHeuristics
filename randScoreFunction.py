import random
import math



def randScoreFunction(nation, scheme):
    """
    Returnshow much a nation costs in total

    Give nation and number of cost scheme as arguments

    Use like: Score(nation, 1)

    """
    if nation == 1:
        return 1

    totalCost = 0
    transmitterCosts = scheme
    # Different cost schemes
    
    
    for province in nation:
        # Ignore unnassigned transmitters i.e. zeroes
        if nation[province][1] != 0:
            totalCost += transmitterCosts[nation[province][1] - 1]

    return totalCost




