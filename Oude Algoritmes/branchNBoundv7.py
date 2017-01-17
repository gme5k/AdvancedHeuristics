from nationLoader import *
from scoreFunctionv2 import *
from jsonDeepCopy import *

provinces = []
numTransmitters = 4
index = 0

def branchNBound(nationtxt, bound):
    nation = nationLoader(nationtxt)

    for key in nation:
        provinces.append(key)

    upperbound = bound

    global index

    solution = []
    counter = 0

    while True:
        counter += 1
        if counter % 100000000 == 0:
            print counter

        if index == -1:
            break

        if nation[provinces[index]][1] == numTransmitters:
            updateTransmitter(nation, True)
            continue
        else:
            updateTransmitter(nation, False)

        # Costs
        costs = scoreFunctionv2(nation, 1)
        if (costs + (len(provinces) - (index + 1)) * 20) > upperbound:
            updateTransmitter(nation, True)
            continue


        # Neighbor
        conflict = False
        for neighbor in nation[provinces[index]][0]:
            if nation[neighbor][1] == nation[provinces[index]][1]:
                conflict = True
                break

        if conflict:
            continue

        # Solution
        if index == len(provinces) - 1:
            print "SOLUTION:"
            if costs < upperbound:
                solution = []
            solution.append(json_deep_copy(nation))
            upperbound = costs
            print upperbound
            print nation
            updateTransmitter(nation, True)
            continue

        index += 1

    print solution
    print upperbound
    print len(solution)
    print counter


def updateTransmitter(nation, previous):
    global index
    if previous == True:
        nation[provinces[index]][1] = 0
        index -= 1
    else:
        nation[provinces[index]][1] += 1

branchNBound("TXT/USA.txt", 1126)
