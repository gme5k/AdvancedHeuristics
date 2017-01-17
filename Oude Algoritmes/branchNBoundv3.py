from nationLoader import *
from scoreFunction import *
from jsonDeepCopy import *

Nation = nationLoader("TXT/Nederland.txt")

#Netherlands = nationLoader("Nederland.txt")
#USA = nationLoader("USA.txt")
#Germany = nationLoader("Germany.txt")
#Iraq = nationLoader("Iraq.txt")

stack = []
upperBoundCost = 1200
cheapest = []
province = ''
counter = 0

# Push begin situation to stack
stack.append(Nation)

# While stack is not empty
while not len(stack) == 0:

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
        if counter % 1000000 == 0:
            print counter
        child[province][1] = i

        """
        transmitterCount = 0
        for key in child:
            if child[key][1] != 0:
                transmitterCount += 1
        """

        costs = scoreFunction(child, 1)[0]

        # Check if costs are above upperbound
        if costs > upperBoundCost:# or costs > 24 * transmitterCount:
            continue

        # Check if neighbour has same transmitter
        conflict = False
        for neighbor in child[province][0]:
            if child[neighbor][1] == i:
                conflict = True
                break

        if conflict == True:
            continue

        # Check if it is a solution (all provinces have transmitters)
        solution = True
        for key in child:
            if child[key][1] == 0:
                solution = False
                break

        # If not a solution, add child to stack
        if solution == False:
            add = json_deep_copy(child)
            stack.append(add)
            continue

        # If solution, update upperbound and cheapest solution
        if costs < upperBoundCost:
                cheapest = []

        cheapest.append(json_deep_copy(child))
        upperBoundCost = scoreFunction(cheapest[0], 1)[0]
        print upperBoundCost
        print cheapest

print cheapest
print len(cheapest)
print upperBoundCost
print counter
