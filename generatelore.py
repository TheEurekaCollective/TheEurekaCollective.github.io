# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "TI23 Mining Barge"

keywords = "TI23 Mining Barge, Terwa Industrial, Ascella Shipyards, system of Sol, mining vehicles, Human Domain, adaptive mining platform, backward compatible, exosystem, drone platform, asteroid, planetesimals, Human Domain, Ascella Orbital Shipyards of Mars, antimatter drives, Size-M raw materials tub, drone launch bays, carrier, charging station, helical mining laser, chassis, fuel tank reserves, cargo containers, sensor suites, drone repair unit, magnetic field generators, collective, Sol System, Kuiper Belt, foreman AI, skeleton crew, engineers, scientists, ionized, electric fields, raw material, dock, factory"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Items", "Human Domain", "Vehicle", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/TI23 Mining Barge Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['antimatter-lore']

# this is the hardest part so read it carefully, look at the
# example for reference, make sure text is surrounded by triple quotes.
#
# 1 - surround links with brackets, and make sure they correspond
#     the links listed directly above exactly, the text in brackets
#     is what the user clicks on and the link above is where it'll
#     redirect
#
# 2 - be conscious of newlines, they're used to separate paragraphs
#     and heading and such but be aware that something like two
#     consecutive newlines will be interpreted as an extra space
#
# 3 - three equal signs at the beginning of a line signifies a
#     large title that you probably only need at the very
#     beginning of the article, make sure the rest is in all caps
#
# 4 - two equal signs at the beginning of a line signifies a
#     section title, make sure the rest of the line is all caps
#
# 5 - one equal sign at the beginning of a line signifies a
#     paragraph title, the rest should be capitalized regularly
#
# 6 - any line that doesn't start with equal signs is interpreted
#     as a regular paragraph

article = """===TI23 MINING BARGE
The TI23 Mining Barge is a resource acquisition vessel developed by Terwa Industrial and produced by Ascella Shipyards within the system of Sol. It is one of the most widely used mining vehicles within the Human Domain due to its modularity and efficient design.
==DEVELOPMENT
The engineers of Terwa Industrial wanted to make an adaptive mining platform that was backward compatible with other currently existing products within the Terwa Industrial ecosystem. They thus devised the TI23 Mining Barge, a modular and efficient drone platform that could mine everything from the smallest asteroid to the largest planetesimals. It was made with the idea that profits aren’t made on the base vehicle, as it is sold at a loss. Instead, money is made from the sale of various parts and services compatible with the TI23 ecosystem.  They then outsourced the production of the platform and its components to Ascella Shipyards, one of the largest shipbuilding corporations within the Human Domain. Primary production of the vehicle takes place in the Ascella Orbital Shipyards of Mars.
==COMPOSITION
The baseline TI23 Mining Barge is composed of two sets of {antimatter} drives, a Size-M raw materials tub, and a single platform of drone launch bays. This platform would act as both a carrier and a charging station. The drones would be equipped with a single set of antimatter drives and a helical mining laser.
==ATTACHMENTS & UPGRADES
Both the barge and the drones it utilizes can be upgraded. However, the drone and barge systems are not cross-compatible with one another.
=Barge
The barge can be upgraded with a reinforced and enlarged chassis to allow more room for additional upgrades. This could include increased fuel tank reserves, larger cargo containers, faster drives, improved sensor suites, larger and more energy-efficient drone platforms, and even a small drone repair unit.
=Drones
Drones can be equipped with various upgrades such as stronger mining lasers, more precise magnetic field generators, and even the ability to link up with other drones in its collective to combine their lasers and mine harder-to-extract materials more effectively.
==OPERATIONS
The most common application of the TI23 Mining Barge is mining the Kuiper belt in Sol System. Fleets of these vessels would be deployed with a foreman AI and a skeleton crew of engineers and scientists that would act in the event of a failure or emergency. After the mining barges are spread out and their charges allocated, drones will be deployed to target specific asteroids or groups of asteroids. Each drone will utilize ablative mining lasers to burn desired material off of the objects. After the materials are ionized by the mining lasers, electric fields pull the material into the drones’ storage tanks. Once their tanks are full, the drones will return to the mining barge and dump their extracted material into the barge’s containers. After filling up the barge’s containers, the drones will return to their dock and recharge for their next mission. The barge itself will then transport the raw material to its assigned dock or factory."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "ti23miningbarge-lore.html"

# ignore this stuff

htmlcode = ""
lines = article.split('\n')
for line in lines:
	curID = line.lower().replace(' ', '-').replace('{', '').replace('}', '').replace('=', '').replace('_', '')
	for c in "{}=_":
		if c in curID:
			curID = curID.replace(c, '')
	if len(line)>=3 and line[:3]=='===':
		htmlcode += "\t\t<h1 id='"+curID+"'>" + line[3:] + "</h1>\n\t\t<span class='underline1'></span>\n"
	elif len(line)>=2 and line[:2]=='==':
		htmlcode += "\t\t<h2 id='"+curID+"'>" + line[2:] + "</h2>\n\t\t<span class='underline2'></span>\n"
	elif len(line)>=1 and line[:1]=='=':
		htmlcode += "\t\t<h3 id='"+curID+"'>" + line[1:] + "</h3>\n"
	elif len(line)>=1 and line[:1]=='_':
		htmlcode += "\t\t<h4 id='"+curID+"'>" + line[1:] + "</h4>\n"
	else:
		htmlcode += "\t\t<p class='infoparagraph'>" + line + "</p>\n"

htmlcode = htmlcode.replace('{', "<a class='infolink' href='(LINKGOESHERE)'>")
htmlcode = htmlcode.replace('}', "</a>")
for link in articlelinks:
	htmlcode = htmlcode.replace('(LINKGOESHERE)', link, 1)

s = open('loretemplate.txt', 'r').read()
s = s.replace('(PAGETITLE)', tabtitle)
s = s.replace('(INFOIMAGE)', infoimagesource)
s = s.replace('(KEYWORDS)', keywords)
for i in range(6):
	s = s.replace('(H'+str(i)+')', infoheadings[i])
	s = s.replace('(I'+str(i)+')', infoentries[i])
s = s.replace('(CONTENT)', htmlcode)

f = open(filename, 'w')
f.write(s)
f.close()
