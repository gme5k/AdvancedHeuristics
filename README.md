									Team
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     ______   | || |     ______   | || |   ______     | |
| |   .' ___  |  | || |   .' ___  |  | || |   .' ___  |  | || |  |_   __ \   | |
| |  / .'   \_|  | || |  / .'   \_|  | || |  / .'   \_|  | || |    | |__) |  | |
| |  | |         | || |  | |         | || |  | |         | || |    |  ___/   | |
| |  \ `.___.'\  | || |  \ `.___.'\  | || |  \ `.___.'\  | || |   _| |_      | |
| |   `._____.'  | || |   `._____.'  | || |   `._____.'  | || |  |_____|     | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 

									README
------------------------------------Radio Russia---------------------------------

								Jules Blom		11363150
								Charlotte Tanis	10304533
								Timothy Mans	10430431

---------------------------------------------------------------------------------

De main.py en branchNBoundv8.py zijn de bestanden die je moet runnen.
Dan volgt een keuzemenu waarin je kan kiezen welk land, welk kostenschema het uitgevoerd
moet worden in geval van main.py ook het aantal runs en welk algoritme. 

Bij main.py wordt automatisch een ingekleurde SVG van het de beste oplossing gemaakt
in de map SVG met de naam 'landcolored.svg' waarin 'land' de naam is van je gekozen land.

Bij branchNBoundv8.py worden alle beste oplossingen weergegeven. Voor Ukraine zijn deze
apart van elkaar in JSON/UkraineBNB gezet. Met ujsonVisualization.py worden in de map
SVG/UkraineBNB alle gekleurde landen geplaatst. Deze staat alleen ingesteld op Ukraine
en hiervoor moet in visualizationinsteps "/Step" aangepast worden in "/Sol"!!!

De bestanden nationLoader.py, scoreFunction.py, jsonDeepCopy.py, visualization.py,
visualizationinsteps.py zijn hulpbestanden. 

De bestanden randomAlgorithm.py, greedyRandom.py en CGR.py [ClusterGreedyRandom]
zijn de bestanden van algoritmes die aangeroepen kunnen worden in main.py.