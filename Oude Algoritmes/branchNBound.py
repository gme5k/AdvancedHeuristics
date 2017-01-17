from nationLoader import *
#from scoreFunction import *
import copy

def branchNBound(nationtxt):

    nation = nationLoader(nationtxt)

    stack = []
    upperBoundCost = 600
    cheapest = []
    province = ''
    counter = 0


    # Push begin situation to stack
    stack.append(nation)

    # While stack is not empty
    while not len(stack) == 0:

    # for i in range(3):
        parent = stack.pop()

        # Find province without transmitter
        for key in parent:
            if parent[key][1] == 0:
                province = key
                break

        child = parent
        # Assign transmitter
        for i in range (4, 0, -1):
            counter = counter + 1
            if counter % 1000 == 0:
                print counter / float(3**25)
            child[province][1] = i

            """
            print "stack was:"
            for k in range(len(stack)):
                print stack[k]
            """
            transmitterCount = 0
            for key in child:
                if child[key][1] != 0:
                    transmitterCount += 1

            costs = scoreFunction(child, 1)[0]


            if costs >= upperBoundCost:# or costs > 24 * transmitterCount:
                # print "high costs"
                continue

            conflict = False
            for neighbor in child[province][0]:
                if child[neighbor][1] == i:
                    conflict = True
                    #print "conflict"
                    break

            if conflict == True:
                continue

            solution = True
            for key in child:
                if child[key][1] == 0:
                    solution = False
                    break

            if solution == False:
                add = copy.deepcopy(child)
                #print "add to stack"
                #print add

                stack.append(add)
                """
                print "stack is now:"
                for k in range(len(stack)):
                    print stack[k]
                """
            else:
                # print "solution"

                cheapest = copy.deepcopy(child)
                upperBoundCost = scoreFunction(cheapest, 1)[0]
                print upperBoundCost
                print cheapest



            #print len(stack)

    print cheapest
    print upperBoundCost
    print counter
    return cheapest


