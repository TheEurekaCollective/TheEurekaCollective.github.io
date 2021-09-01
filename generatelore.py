# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Metaphysics"

keywords = "Metaphysics, Conceptual Plane, Material Plane, dimensions, sister universe, ontologically, quark, souls, anima, conceptual web, sentient creature, constituents, Galactic Commonwealth, Apotheons, entity"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Subjects", "Conceptual Plane", "Science", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Metaphysics Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['galacticcommonwealth-lore']

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

article = """===METAPHYSICS
Metaphysics is a term used to describe the phenomena that occurs within the Conceptual Plane. Metaphysics and the Conceptual Plane operate on completely different laws compared to the Material Plane, meaning it is beyond true comprehension. It is not composed of dimensions nor does it follow a linear form of time. As a result, this plane is highly theoretical and can only be explored through experimentation and conjecture, not firsthand exploration.
==CONCEPTUAL PLANE
The Conceptual Plane is a sister universe where metaphysical concepts reside. Everything that can be categorized ontologically exists in this universe, from the idea of a cup to a quark. As the Material Plane’s sister universe, it is inherently tied to the activities of the Material Plane. This is also the plane where souls and anima reside.
==ANIMA
Souls are containers for memories and experiences. It is only natural that over time multiple souls would host similar memories and experiences. When this occurs, a conceptual web begins to be generated. When exceeding a certain threshold, this web becomes a sentient creature, known as an anima. The souls that compose this conceptual web are then designated as constituents. For an anima to grow, it either must have its constituents increase information related to it or attain more constituents. The larger and more complex this group of constituents is, the more powerful an anima becomes. There is a near infinite amount of anima residing in the Conceptual Plane due to the sheer number of differing concepts available in existence.
=Classification
There are a multitude of methods for classifying anima. In the {Galactic Commonwealth}, the primary methods are by primary concept(s), constituent count, and origin.
_Apotheons
Apotheons are a special subtype of anima due to their point of origin not being that of the Conceptual Plane, but the Material Plane. This occurs when the point of worship stems from not just a concept, but an entity and its soul. When people begin to worship such entities, their soul begins to take on some of the properties of an anima."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "metaphysics-lore.html"

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
