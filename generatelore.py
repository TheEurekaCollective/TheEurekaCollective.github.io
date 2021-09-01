# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Slime Mold"

keywords = "slime molds, protists, neural network simulations, civil engineering, Human Domain, alien behaviors, physarum polycephalum (blob), fuligo septica (dog’s vomit), hemitrichia serpula (pretzel slime), genetic splicing, genetic modification, eclipse slime mold, bioluminescence, mobile terrariums, slime mold art, colonies, generations, collections"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Characters", "Human Domain", "Pet", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Slime Mold Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = []

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

article = """===SLIME MOLD
Slime mold is an umbrella term used to describe various single-celled protists that can coalesce to form complex structures. While originally used in tasks such as neural network simulations and civil engineering, they are now commonly seen as pets within the Human Domain due to their low maintenance and peculiar, seemingly alien, behaviors.
==SPECIES
There are many species of slime molds that are kept as pets. Some of these include physarum polycephalum (blob), fuligo septica (dog’s vomit), and hemitrichia serpula (pretzel slime). They are usually chosen by owners due to their shape and color, as the behaviors of slime molds do not vary much from species to species. Genetic splicing and modification have also allowed some very interesting species to come to life, such as the eclipse slime mold, possessing a pure black color that exhibits a form of bioluminescence.
==MAINTENANCE
Keeping and maintaining a slime mold varies from species to species, but the process is usually quite simple. Slime molds do not require much in terms of interaction and need only to be fed. Slime molds kept in more natural terrariums are regularly supplied with fresh detritus and decaying organic matter. However, those kept in less natural environments are provided alternatives such as oat flakes and valerian root.
==EQUIPMENT
Mobile terrariums are robotic bodies that utilize various sensors and tactile stimuli to allow a slime mold to somewhat rudimentarily pilot walking vessels. The slime mold also acts as the robot’s central processing unit -- stored in a glass terrarium for viewing pleasure. The glass has multiple settings to allow in variable amounts of light, as slime molds generally have an aversion to it. The interiors of the terrarium are also highly modular, with not only the environmental conditionals able to be changed but also the physical layout. Clever slime mold owners have been known to make living sculptures and tapestries by growing slime molds in different patterns and setups. Many owners also grow different species in the same setting, adding another layer of complexity to making slime mold art.
==ACQUISITION
While it is possible to buy a newly grown slime mold, most people tend to prefer splitting one of their family’s existing colonies. It is not uncommon to see colonies of slime molds hundreds of years old, passed down from generation to generation. People often keep multiple colonies of slime molds as a collection."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "slimemold-lore.html"

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
