def scoreFunction(nation, scheme):
    """
    Returnshow much a nation costs in total

    Give nation and number of cost scheme as arguments

    Use like: Score(nation, 1)

    """
    if nation == 1:
        return 1

    totalCost = 0

    # Different cost schemes
    if scheme == 1:
        transmitterCosts = [20, 22, 28, 32, 37, 39, 41]
    elif scheme == 2:
        transmitterCosts = [28, 30, 32, 33, 36, 37, 38]
    elif scheme == 3:
        transmitterCosts = [12, 26, 27, 30, 37, 39, 41]
    elif scheme == 4:
        transmitterCosts = [19, 20, 21, 23, 36, 37, 38]
    elif scheme == 5:
        transmitterCosts = [16, 17, 31, 33, 36, 56, 57]
    
    for province in nation:
        # Ignore unnassigned transmitters ie zeroes
        if nation[province][1] != 0:
            totalCost += transmitterCosts[nation[province][1] - 1]

    return totalCost