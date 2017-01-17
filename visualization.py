from BeautifulSoup import BeautifulSoup

def colorNation(nation, nationname):
	"""
	Arguments: nation dictionary and nationname string of filename in SVG folder

	Assign color to province based on transmitter number
	Requires BeautifulSoup parsing library to parse SVG file and find matching id's for paths of provinces
	"""
	openName = "SVG/" + nationname + ".svg"	
	writeName = "SVG/" + nationname + "color.svg"

	# Open svg & load into Beautiful Soup
	svg = open(openName, 'r').read()
	soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

	# Make new file object for writing
	new_map = open(writeName, 'w') 

	# Find all paths in svg file
	paths = soup.findAll('path')

	colors = ["#f9f9f9", "#dbf3fd", "#95dbfa", "#4fc3f7", "#3f9cc5", "#1f4e62", "#000000"]

	# SVG style tag string
	path_style = "fill-opacity: 1; stroke:white; stroke-opacity: 1;stroke-width:0.5; fill:"
	
	for p in paths:
		if p['id'] in nation:
			color = nation[p['id']][1]
			p['style'] = path_style + colors[color - 1]

	# Write to svg file
	new_map.write(soup.prettify())
	new_map.close()