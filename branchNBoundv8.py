from nationLoader import *
from jsonDeepCopy import *
from pick import pick

"""
Cost schemes for reference
--------------------------------------
Scheme 1: [20, 22, 28, 32, 37, 39, 41]
Scheme 2: [28, 30, 32, 33, 36, 37, 38]
Scheme 3: [12, 26, 27, 30, 37, 39, 41]
Scheme 4: [19, 20, 21, 23, 36, 37, 38]
Scheme 5: [16, 17, 31, 33, 36, 56, 57]

"""

# Pick multimenu for easy selection of options
title, options = 'Please choose a nation: ', ["Ukraine.txt", "China.txt", "USA.txt", "Russia.txt"]
chosenNation, nationIndex = pick(options, title)

chosenNationPath = "TXT/" + chosenNation

schemeTitle, schemeOptions = 'Please choose cost scheme: ', [1, 2, 3, 4, 5]
scheme, schemeIndex = pick(schemeOptions, schemeTitle)

transmTitle, transmOptions = 'Please choose how many transmitter can be used (less is always faster!): ', [4, 5, 6, 7]
numTransmitters, transmIndex = pick(transmOptions, transmTitle)

print "------------------------------------------"
print "Nation:", chosenNation, "with costscheme", scheme
print "------------------------------------------"

provinces = []
index = 0
costs = 0

if chosenNation == "Ukraine.txt":
    if scheme == 1:
        bound = 586
    if scheme == 2:
        bound = 748
    if scheme == 3:
        bound = 524
    if scheme == 4:
        bound = 502
    if scheme == 5:
        bound = 531
if chosenNation == "China.txt":
    if scheme == 1:
        bound = 768
    if scheme == 2:
        bound = 983
    if scheme == 3:
        bound = 667
    if scheme == 4:
        bound = 661
    if scheme == 5:
        bound = 692
if chosenNation == "USA.txt":
    if scheme == 1:
        bound = 1120
    if scheme == 2:
        bound = 1437
    if scheme == 3:
        bound = 1020
    if scheme == 4:
        bound = 962
    if scheme == 5:
        bound = 1013
if chosenNation == "Russsia.txt":
    if scheme == 1:
        bound = 1954
    if scheme == 2:
        bound = 2487
    if scheme == 3:
        bound = 1746
    if scheme == 4:
        bound = 1670
    if scheme == 5:
        bound = 1763

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

def branchNBound(nationtxt, bound):
    """
    Depth first, check upper bound and neighbors
    """
    nation = nationLoader(nationtxt)

    for key in nation:
        provinces.append(key)

    upperbound = bound

    global index

    solution = []
    counter = 0

    while index >= 0:
        counter += 1
        if counter % 100000000 == 0:
            print counter
            print "Now at:", nation

        if index == -1:
            break

        # Assign transmitter
        if nation[provinces[index]][1] == numTransmitters:
            updateTransmitter(nation, True)
            continue
        else:
            updateTransmitter(nation, False)

        # Check if costs are above upper bound
        if (costs + (len(provinces) - (index + 1)) * transmitterCosts[0]) > upperbound:
            updateTransmitter(nation, True)
            continue

        # Check if a neighbor has the same transmitter
        conflict = False
        for neighbor in nation[provinces[index]][0]:
            if nation[neighbor][1] == nation[provinces[index]][1]:
                conflict = True
                break

        if conflict:
            continue

        # Check if a solution is found
        if index == len(provinces) - 1:
            print "\nSOLUTION:"
            if costs < upperbound:
                solution = []
            solution.append(json_deep_copy(nation))
            upperbound = costs
            print "Score:", upperbound
            print nation
            updateTransmitter(nation, True)
            continue

        index += 1

    print "Solutions:", solution
    print "Cost:", upperbound
    print "Number of solutions:", len(solution)
    print "Iterations:", counter


def updateTransmitter(nation, previous):
    """
    Assign transmitter and update costs
    """
    global index
    global costs

    # Subtract costs of current transmitter from costs
    if nation[provinces[index]][1] != 0:
        costs -= transmitterCosts[nation[provinces[index]][1] - 1]

    # If previous, set transmitter of current province to 0 and set index to previous province
    if previous:
        nation[provinces[index]][1] = 0
        index -= 1
    # Else, assign next transmitter to province and update costs
    else:
        nation[provinces[index]][1] += 1
        costs += transmitterCosts[nation[provinces[index]][1] - 1]

branchNBound(chosenNationPath, bound)