from random import *
import json
from nationLoader import *
from jsonDeepCopy import *
from randScoreFunction import *
from scoreFunction import *



f = open('writefile', 'w')
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
            
         
            for province in provinceNames:
                transmitterOptions = [1, 2, 3, 4]

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

                    ### stepcounter = stepcounter + 1
                    ### jsonPath = "JSON/" + nationtxt[:-4] + "/Step" + str(stepcounter) + ".txt"
                    ### json.dump(nation, open(jsonPath,'w'))
            break
            
        except:
            pass

    return nation
    
def Repeater(algorithm, runs, nationtxt):
    """
    Show distribution plot of algorithm

    Arguments
    ----------
    algorithm:  algorithm you want used
    runs:       number of trials chosen
    nationtxt:  name of nation text file
    updateFreq: Gives update after updateFreq number of runs
    plot:       'y' or 'n' for yes or no to plot. Standard is 'y'
    """

    scores = {}

    # Make sure appropriate range is used for scores

    scoreRange = range(0, 10000)

    # score range has to be between these two numbers
    for i in scoreRange:
        scores.update({i : 0})
    
    #~ print "Running " + str(algorithm)[0:-18] + "> " + str(runs) + " times...\n"
    
    
    minScore = 10**40
    
   
    scheme = kostenschema()
    for i in range(runs):
        nation = algorithm(nationtxt)
        
        score = randScoreFunction(nation, scheme)
        scores[score] += 1
        
        # keep track of best scores and nation
        if score < minScore:
            minScore = score
            bestNation = nation

    maxFreq = 0
   
    scoreCount = 0

    for score in scores:
        if scores[score] > maxFreq:
            maxFreq = scores[score]
            maxFreqScore = score
        if score == minScore:
            minScoreFreq = scores[score]
        if scores[score] >= 1:
            scoreCount += 1 
    
    
    usedTrans = []
    fivePlus = 0
    fivePlusNoDuplicate = 0

    one = 0
    two = 0 
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0

    for province in bestNation: 
        
        if bestNation[province][1] == 1:
            one += 1
        if bestNation[province][1] == 2:
            two += 1
        if bestNation[province][1] == 3:
            three += 1
        if bestNation[province][1] == 4:
            four += 1
        if bestNation[province][1] == 5:
            five += 1
        if bestNation[province][1] == 6:
            six += 1
        if bestNation[province][1] == 7:
            seven += 1
            
    
    if five > 0 or six > 0 or seven > 0:
        fivePlus += 1
        if scheme[3] != scheme[4]:
            fivePlusNoDuplicate += 1
    
    usedTrans.append([one, two, three, four, five, six, seven])     
        
        
    return minScore, minScoreFreq, scheme, fivePlus, fivePlusNoDuplicate, usedTrans, scoreCount





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
            #~ print "\nSOLUTION:"
            if costs < upperbound:
                solution = []
            solution.append(json_deep_copy(nation))
            upperbound = costs
            #~ print "Score:", upperbound
            #~ print nation
            updateTransmitter(nation, True)
            continue

        index += 1
        
    usedTrans = []
    fivePlus = 0
    fivePlusNoDuplicate = 0
    
    for nation in solution:
        
        one = 0
        two = 0 
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0

        for province in nation: 
            
            if nation[province][1] == 1:
                one += 1
            if nation[province][1] == 2:
                two += 1
            if nation[province][1] == 3:
                three += 1
            if nation[province][1] == 4:
                four += 1
            if nation[province][1] == 5:
                five += 1
            if nation[province][1] == 6:
                six += 1
            if nation[province][1] == 7:
                seven += 1
                
        
        if five > 0 or six > 0 or seven > 0:
            fivePlus += 1
            if transmitterCosts[3] != transmitterCosts[4]:
                fivePlusNoDuplicate += 1
        
        usedTrans.append([one, two, three, four, five, six, seven])     
              
    return fivePlus, fivePlusNoDuplicate, usedTrans, upperbound, len(solution), counter
    #~ f.write("\n Used Transmitters: "+ str(one)+" "+ str(two)+" "+ str(three)+" "+ str(four)+" "+ str(five)+" "+ str(six)+" "+ str(seven)+"\n Cost: "+str(upperbound)+"\n Number of solutions: "+str(len(solution))+"\n Iterations: "+str(counter)+"\n"+"\n"+"\n"+"\n")
    
    #~ print "transmitter frequecies:", one, two, three, four, five, six, seven
    #~ print "Solutions:", solution
    #~ print "Cost:", upperbound
    #~ print "Number of solutions:", len(solution)
    #~ print "Iterations:", counter
  
 
def kostenschema():
    kostenschemalen = 7
    schema = []
    
    for i in range(kostenschemalen):
        x = random.randint(1,50)
        
        schema.append(x)
        
        
    
    schema.sort()
    
    return schema

def updateTransmitter(nation, previous):
    """
    Assign transmitter and update costs
    """
    global index
    global costs

    # Subtract costs of current transmitter from costs
    if nation[provinces[index]][1] != 0:
        costs -= transmitterCosts[nation[provinces[index]][1] - 1]

    # If previous, set transmitter f current province to 0 and set index to previous province
    if previous:
        nation[provinces[index]][1] = 0
        index -= 1
    # Else, assign next transmitter to province and update costs
    else:
        nation[provinces[index]][1] += 1
        costs += transmitterCosts[nation[provinces[index]][1] - 1]
        
        
        
        
h = 1
maxIterations = 0
fivePlusCount = 0
fivePlusNoDuplicateCount = 0
fivePlusCountG = 0
fivePlusNoDuplicateCountG = 0
hardestScheme = 0
hardestSchemeG = 0
curMinScoreFreq = 10000

for i in range(20):
    
    print h
    provinces = []
    index = 0
    costs = 0
    numTransmitters = 7
    
    bound, minScoreFreq, scheme, fivePlusG, fivePlusNoDuplicateG, usedTransG, scoreCount = Repeater(greedyRandom, 10000, "Germany.txt")
    transmitterCosts = scheme
    fivePlus, fivePlusNoDuplicate, usedTransmitters, lowCost, nSolutions, iterations = branchNBound("TXT/Germany.txt", bound)
    
    fivePlusCount += fivePlus
    fivePlusNoDuplicateCount += fivePlusNoDuplicate
    
    fivePlusCountG += fivePlusG
    fivePlusNoDuplicateCountG += fivePlusNoDuplicateG
    
    if iterations > maxIterations:
        maxIterations = iterations
        hardestScheme = scheme
        f.write("\n branch")
        print "branch"
        f.write("\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n")
        print "\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n"
    
    if fivePlus > 0:
        f.write("\n fivePlus")
        print "fivePlus"
        f.write("\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n")
        print "\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n"
    
    if minScoreFreq < curMinScoreFreq:
        curMinScoreFreq = minScoreFreq
        hardestSchemeG = scheme
        print "greedy"
        f.write("\n greedy")
        f.write("\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n")
        print "\n Scheme: "+str(scheme)+"\n\n greedyLowestCost: "+str(bound)+"\n minScoreFreq: "+str(minScoreFreq)+"\n scoreCount: "+str(scoreCount)+"\n greedyUsedTrans"+str(usedTransG)+"\n greedyFivePlus: "+str(fivePlusG)+"\n greedyFivePlusNoDuplicate: "+str(fivePlusNoDuplicateG)+"\n\n branchLowestCost: "+str(lowCost)+"\n branchIterations: "+str(iterations)+"\n branchNSolutions: "+str(nSolutions)+"\n branchTransUsed: "+str(usedTransmitters)+"\n fivePlus: "+str(fivePlus)+"\n fivePlusNoDuplicate: "+str(fivePlusNoDuplicate)+"\n\n\n"
    
    h += 1
    
f.write("\n Hardest Branch")   
print "Hardest Branch"
f.write("\n maxIterations: "+str(maxIterations)+"\n fivePlusCount: "+str(fivePlusCount)+"\n fivePlusNoDuplicateCount: "+str(fivePlusNoDuplicateCount)+"\n hardestScheme: "+str(hardestScheme)+"\n\n")
print "\n maxIterations: "+str(maxIterations)+"\n fivePlusCount: "+str(fivePlusCount)+"\n fivePlusNoDuplicateCount: "+str(fivePlusNoDuplicateCount)+"\n hardestScheme: "+str(hardestScheme)+"\n\n"

f.write("\n Hardest Greedy")   
print "Hardest Greedy"
f.write("\n curMinScoreFreq: "+str(curMinScoreFreq)+"\n fivePlusCountG: "+str(fivePlusCountG)+"\n fivePlusNoDuplicateCountG: "+str(fivePlusNoDuplicateCountG)+"\n hardestScheme: "+str(hardestSchemeG))
print "\n curMinScoreFreq: "+str(curMinScoreFreq)+"\n fivePlusCountG: "+str(fivePlusCountG)+"\n fivePlusNoDuplicateCountG: "+str(fivePlusNoDuplicateCountG)+"\n hardestScheme: "+str(hardestSchemeG)

f.close()
