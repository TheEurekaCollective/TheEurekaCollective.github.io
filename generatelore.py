# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Cosmology"

keywords = "​​​​the Outside, It Who Sleeps (the Dreamer), Existences, Material Plane, Conceptual Plane, Void, universe, dimensions, micro-universes, the Abyss, metaphysics, souls, anima, conjecture, apotheons, mana, mass shadows, faster-than-light (FTL), voidjumping"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Subjects", "Existence", "Existence", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Cosmology Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['metaphysics-lore', 'fasterthanlight-lore']

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

article = """===COSMOLOGY
Within the Outside, there resides a being. It is known by many names, but its most prominent is It Who Sleeps, otherwise referred to as the Dreamer. It is a being that undergoes the same repeated cycle of slumber and wakefulness. By dreaming, it undergoes a process of creating Existences, and by waking, it undergoes a process of destroying them. Countless Existences have been fashioned and dismantled in this manner. Anima is simply one of these myriad Existences, and it shall not be the last.
==EXISTENCE
Within all of Existence, there exists three planes of reality. The first is the Material Plane, which is the universe as we know it. The second is the Conceptual Plane, the realm of souls. The last is the Void, the land of in-betweens.
=Material Plane
The Material Plane is our physical universe of matter and energy. It is a four-dimensional space composed of three spatial dimensions and one time dimension. This space contains trillions of galaxies and is billions of years old.
_Abyss
Residing in the material plane is a series is interlinked micro-universes collectively referred to as the Abyss. These micro-universes are realms dominated by onturgists.
=Conceptual Plane
The Conceptual Plane is a sister universe to the Material Plane. It is the plane of {metaphysics}, souls, and anima. Everything that could be categorized ontologically exists in this universe, from the idea of a cup to a quark. However, this is all conjecture as no material being has ever entered this Plane. The only information about the Conceptual Plane has come from the anecdotes of various anima and apotheons.
=Void
The Void is a higher-dimensional space that resides in the space between the Material Plane and the Conceptual Plane. As the two planes’ meeting point, it is rich in mana. It is theoretically as expansive as our universe but is hostile to all forms of matter. Should matter enter this space unprotected, it will disappear instantaneously. However, gravity from our universe is able to penetrate space-time and enter the Void, creating areas known as "mass shadows." Due to its nature of being composed of many more spatial dimensions than the Material Plane, one location in the Void can coincide with multiple locations in the Material Plane. This property has led to the rise of a {faster-than-light} method of transport known as voidjumping."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "cosmology-lore.html"

# ignore this stuff
article = article.replace('{', "<a class='infolink' href='(LINKGOESHERE)'>")
article = article.replace('}', "</a>")
for link in articlelinks:
	article = article.replace('(LINKGOESHERE)', link, 1)

htmlcode = ""
lines = article.split('\n')
for line in lines:
	if len(line)>=3 and line[:3]=='===':
		curID = line[3:].lower().replace(' ', '-')
		htmlcode += "\t\t<h1 id='"+curID+"'>" + line[3:] + "</h1>\n\t\t<span class='underline1'></span>\n"
	elif len(line)>=2 and line[:2]=='==':
		curID = line[2:].lower().replace(' ', '-')
		htmlcode += "\t\t<h2 id='"+curID+"'>" + line[2:] + "</h2>\n\t\t<span class='underline2'></span>\n"
	elif len(line)>=1 and line[:1]=='=':
		curID = line[1:].lower().replace(' ', '-')
		htmlcode += "\t\t<h3 id='"+curID+"'>" + line[1:] + "</h3>\n"
	elif len(line)>=1 and line[:1]=='_':
		curID = line[1:].lower().replace(' ', '-')
		htmlcode += "\t\t<h4 id='"+curID+"'>" + line[1:] + "</h4>\n"
	else:
		htmlcode += "\t\t<p class='infoparagraph'>" + line + "</p>\n"

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
