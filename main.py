import matplotlib.pyplot as plt

#from visualizationinsteps import *
from scoreFunction import *
from greedyRandom import *
from randomAlgorithm import *
from visualization import *
from CGR import *
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
chosenNation, index = pick(options, title)

runTitle, runOptions = 'Please choose number of runs: ', [1, 100, 1000, 10000, 100000, 1000000]
chosenRuns, runIndex = pick(runOptions, runTitle)

schemeTitle, schemeOptions = 'Please choose cost scheme: ', [1, 2, 3, 4, 5]
chosenScheme, schemeIndex = pick(schemeOptions, schemeTitle)

algoTitle, algoOptions = 'Please algorithm: ', ["Random", "greedyRandom", "clusterGreedyRandom"]
chosenAlgoString, algoIndex = pick(algoOptions, algoTitle)

# Pick library is fussy about using functions as pick options so this is how i solve it
if chosenAlgoString == "Random":
    chosenAlgo = randomAlgorithm
elif chosenAlgoString == "greedyRandom":
    chosenAlgo = greedyRandom
elif chosenAlgoString == "clusterGreedyRandom":
    chosenAlgo = clusterGreedyRandom



print "-------------------------------------------------------------"
print "Nation:", chosenNation, "with costscheme", chosenScheme, "and", chosenAlgoString, "algorithm"
print "-------------------------------------------------------------"

def Show(algorithm, scheme, nationtxt):
    """
    Make colored map and show score of algorithm
    """
    nation = algorithm(nationtxt)
    colorNation(nation, nationtxt[:-4])
    return str(algorithm)[10:-19] + ", score: " + str(scoreFunction(nation, chosenScheme))

def Plot(scores):
    """
    Plot the distribution scores in a nice chart
    """
    x = []
    y = []
    
    for i in scores:
        x.append(i)
        y.append(scores[i])

    g, (ax1) = plt.subplots(1)
    ax1.bar(x, y, color = "black")

    ax1.set_title("Distribution of the " + chosenAlgoString + " algorithm", fontsize = 34)
    ax1.set_ylim(0,100000)
    ax1.set_xlabel("Score", fontsize = 26)
    ax1.set_ylabel("Frequency", fontsize = 24)
    ax1.tick_params(labelsize = 18)

    plt.bar(x, y, color = "black")
    #~ plt.savefig("million.png", bbox_inches="tight", dpi = 600)
    plt.show() 

def Distribution(algorithm, runs, nationtxt, updateFreq, plot):
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
    if nationtxt == "Ukraine.txt":
        scoreRange = range(500, 950)
    elif nationtxt == "China.txt":
        scoreRange = range(600, 1300)
    elif nationtxt == "USA.txt":
        scoreRange = range(1000 ,1750)
    elif nationtxt == "Russia.txt":
        scoreRange = range(1650, 2550)

    # score range has to be between these two numbers
    for i in scoreRange:
        scores.update({i : 0})
    
    print "Running " + str(algorithm)[0:-18] + "> " + str(runs) + " times...\n"
    
    stepCount = 0
    minScore = 9999999999999

    for i in range(runs):
        nation = algorithm(nationtxt)
        
        score = scoreFunction(nation, chosenScheme)
        scores[score] += 1
        
        # keep track of best scores and nation
        if score < minScore:
            minScore = score
            bestNation = nation
        
        stepCount += 1
        if updateFreq > 9:
            if not stepCount % updateFreq:
                print "Now at", stepCount
    
    print "Calculating most probable score..."
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
    
    if plot == "y":
        Plot(scores)

    colorNation(bestNation, nationtxt[:-4])

    return "\nPossible scores: " + str(scoreCount) + "\nMost frequent: (score: " + str(maxFreqScore) + ", frequency: " + str(maxFreq) + "), " + "\nLowest score: "+ "(score: "+str(minScore)+", frequency: " + str(minScoreFreq)+")\n"

print Distribution(chosenAlgo, chosenRuns, chosenNation, chosenRuns/10, "y")
