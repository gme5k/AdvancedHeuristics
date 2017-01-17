from BeautifulSoup import BeautifulSoup
import json
import os

def colorNationInSteps(nationname):
	'''
	Arguments: Only nationname (without.txt)

	Reads all JSON formatted .txt files in JSON/[nationname] folder and makes colored map for each one

	put this part in Algorithm function where transmitters nr's are assigned to write JSON files
	----------
	import json
	counter = 0

	[in loop]
		counter += 1
		jsonPath = "JSON/" +  nationtxt[:-4] + "/Step" + counter + ".txt"

	    json.dump(nation, open(jsonPath,'w'))

	'''
	# Path for blank svg
	openName = "SVG/" + nationname + ".svg"	
	jsonFolder = "JSON/" + nationname

	# Open svg & load into Beautiful Soup
	svg = open(openName, 'r').read()
	soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

	colors = ["#f9f9f9", "#dbf3fd", "#95dbfa", "#4fc3f7", "#3f9cc5", "#1f4e62", "#000000"]
	path_style = "fill-opacity: 1; stroke:white; stroke-opacity: 1;stroke-width:0.5; fill:"

	counter = 1

	# Read json file every step and use this to color nation
	for jsonFile in os.listdir(jsonFolder):

		readPath = "JSON/" + str(nationname) + "/Step" + str(counter) + ".txt"
		writeName = "SVG/" + str(nationname) + "/Step" + str(counter) + str(nationname) + "color.svg"
		counter += 1
		
		nation = json.load(open(readPath))

		# Make new file object for writing
		new_map = open(writeName, 'w') 

		# Find all paths in svg file
		paths = soup.findAll('path')	
	
		for p in paths:
			if p['id'] in nation:
				color = nation[p['id']][1]
				p['style'] = path_style + colors[color - 1]

		# Write to svg file
		new_map.write(soup.prettify())
		new_map.close()