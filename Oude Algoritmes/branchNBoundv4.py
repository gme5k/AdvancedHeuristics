from nationLoader import *
from scoreFunction import *
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
    end = False

    while not end:
        if index == -1:
            end = True
            continue

        if assignTransmitter(nation) == "previous":
            index -= 1
            continue

        # Costs
        costs = scoreFunction(nation, 1)[0]
        if (costs + (len(provinces) - (index + 1)) * 20) > upperbound:
            nation[provinces[index]][1] = 0
            index -= 1
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
            nation[provinces[index]][1] = 0
            index -= 1
            print upperbound
            print nation
            continue

        index += 1

    print solution
    print upperbound
    print len(solution)


def assignTransmitter(nation):
    if nation[provinces[index]][1] == numTransmitters:
        nation[provinces[index]][1] = 0
        return "previous"
    else:
        nation[provinces[index]][1] += 1
        return "next"


branchNBound("TXT/Nederland.txt", 600)







