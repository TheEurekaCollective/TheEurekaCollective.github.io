# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Ygirin"

keywords = "Ygirin (Star Children), cosmic strings, early Commonwealth period, Xweili, plasma probe, psionic emissions, Bureau of Astrobiology, Galactic Codex, sophont, hunting, plasma fishers, Fields of Aster, gravitic nets, Fusion Matrix, electromagnetically shielded, Khepri, Ptah, Hathor, Aten, Talaphrian Order, groundmaster, War of the Disk, General Ohu, Second Legion, Lord-Merchant Olande, Olande’s Scepter, Commonwealth Public Athenaeum"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Factions", "Milky Way", "Species", "Ygirin", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Ygirin Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['galacticcommonwealth-lore', 'talaphrianorder-lore', 'karanaan-lore']

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

article = """===YGIRIN
Ygirin, otherwise known as Star Children, is an umbrella term used to refer to organisms that are born due to the pressures and energies that exist within stars. These forces amalgamate and entangle collections of cosmic strings, creating a Ygirin. As they grow and mature by accumulating more “energy-mass”, they move towards the surface of their host stars. This process can take thousands of years. However, they eventually die due to them reaching the surface and being ejected from their host stars.
==HISTORY
The first documented case of a Ygirin was sometime during the early {Commonwealth} period. A group of Xweili scientists were exploring the inner workings of a star utilizing a plasma probe when one of the probe’s scanners detected a series of psionic emissions originating from within the star. Electromagnetic imaging showed a miniscule amorphous blob of higher density compared to the surrounding area. This news was brought to the attention of the Bureau of Astrobiology, who then officially catalogued the species in the Galactic Codex.
==BIOLOGY
=Composition
Ygirin lack the specialized structures that most other species have. Their bodies are entirely homogeneous, with all their functions distributed throughout their bodies.
=Growth and Development
Ygirin consume plasma and nuclear matter to grow themselves. Given enough material, they can grow indefinitely. Over time, a Ygirin gains a stronger grasp over electromagnetism as well as increases in intelligence.
==SOCIETY
Since it is very rare for more than a few Ygirin to exist within a star at a single time, most Ygirin are naturally antisocial. However, some of the sophont Ygirin have been able to form relationships with others.
==RARITY
Ygirin are extremely rare due to the very specialized conditions that involve their emergence. As a result, only a few thousand Ygirin have been detected within the Milky Way.
==YGIRIN HUNTING
Ygirin hunting is an extremely profitable practice as wealthy individuals and laboratories are willing to pay exorbitant amounts of credits to acquire a specimen. Hunters of Ygirin are known as plasma fishers. The Fields of Aster, a region of the galaxy heavily populated with stars, is a hotspot for Ygirin hunters.
==YIGIRIN EXTRACTION
To collect a Ygirin, a gravitic net is deployed into its host star. This net then pulls the Ygirin into a Fusion Matrix. This matrix is essentially a collection area for plasma to keep the Ygirin alive. It is also electromagnetically shielded to prevent the Ygirin from interacting with the outside world.
==SOPHONTHOOD
While the majority are non-sophont in terms of intelligence, there have been four notable instances of a sophont Ygirin occurring naturally. They are known as Khepri, Ptah, Hathor, and Aten. To interact with the world, they utilize a modular fusion matrix, which adapts to any form the Ygirin desires.
==NOTABLE INDIVIDUALS
Groundsmaster Aten of the {Talaphrian Order} is one of the oldest groundmasters within the Order. It has been part of the order since the pre-war era, meaning that it was a veteran of the War of the Disk. Aten’s most prolific achievement was destroying General Ohu of the Second Legion.
==KNOWN OWNERS
Lord-Merchant Olande: The long life of the leader of the {Karanaan} has allowed it to collect multiple Ygirin. The most prominent in its collection is the one that resides within the capstone of Olande’s Scepter. It is an infinitely mirrored gem, creating a “star within star” visual effect. 
The Commonwealth Public Athenaeum is known to have a Ygirin exhibit."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "ygirin-lore.html"

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
