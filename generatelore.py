# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Tendril"

keywords = "Tendril, sophont gigafauna, terraforming engines, tribal species, Quazon, commensalistic relationship, genetically engineered species, biological supercomputers, ice giants, grazers, excavators, energy generation, Pod Riders, gigaorganisms"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Factions", "Mixed", "Species", "Tendril", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Tendril Icon.svg"

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

article = """===TENDRIL
The Tendril are a species of sophont gigafauna that are theorized to be terraforming engines created by an unknown race. They possess the capability to modify their own genome and generate subspecies as needed. A tribal species known as the Quazon have formed a commensalistic relationship with certain Tendril, using them for survival and transport in exchange for being the Tendril’s proxies in galactic affairs.
==EVOLUTION & BIOLOGY
=Creation Theory
Some scientists theorize that the Tendril species is a genetically engineered species meant to terraform planets for some higher race. However, no plausible species within the galaxy have claimed to be responsible as its creator. Other scientists purport that they are in actuality a form of space whale that decided to settle down onto planets instead of traveling throughout the galaxy nomadically.
=Physiology
Tendril are biological supercomputers that possess the capability to voluntarily modify their genome with incredible accuracy. This has allowed them to adapt to a variety of environments as well as develop subspecies to aid them in carrying out their primary function: terraforming. As a result, it is hard to precisely fit the Tendril into a single series of physical descriptions, as each of them exists in different environments with different genetic codes.
=Life Cycle
The life of a tendril begins as a pod, one of hundreds to tens of thousands created by its mother. The pod is then launched into space on a calculated trajectory to a new planet or asteroid. These celestial bodies are chosen based on hospitality ratings collected by sensors that the mother grew. Tendril seem to have the highest preference for ice giants due to their hard outer shells but abundant water supplies. After making impact on the planet’s surface, the pod will open up and immediately begin the process of penetrating the ice surface and acquiring energy. Based on the type of star that hosts it, it will create plants uniquely suited for that type of star. It will then create a variety of subspecies such as grazers and excavators to find physical material for growth. After penetrating the surface, it will make a journey to the planet's core, where it will repeat the process of creating holes in the ice for energy generation, creating subspecies to help it grow and maintain itself, and terraforming the planet. After reaching maturity, a process that takes several hundred, if not thousands of years, they will then create pods to start the process over again.
==PSYCHOLOGY
While the Tendril are sophont, their gargantuan sizes make communication between their different parts take large amounts of time, meaning their thoughts are incredibly slow compared to most other sophont species. They possess no form of society as they spend most of their lives in isolation, creating behaviors that would be considered extremely antisocial compared to most other sophont species. However, some have bonded with the Quazon tribes they host, with some regarding them as pets and others seeing them as individuals on equal footing with themselves.
==QUAZON
The Quazon, otherwise known as the Pod Riders, are a race of sophont quadrupeds that worship the Tendril as gods. They are called pod riders due to their method of propagating from planet to planet by hitching a ride on pods. Quazon have a commensalistic relationship with the Tendril, with them harvesting resources such as foods and building materials from the gigaorganism. Particularly benevolent Tendril will heed the prayers of its resident Quazon, forming subspecies that act as beasts of burden or guardians. The long period of interaction between the Quazon and the Tendril have led the Quazon to develop very similar genetic makeups to the Tendril, with some components even being interchangeable."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "tendril-lore.html"

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
