# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Silent Elder"

keywords = "Outlands, sleeping creators, tombs, prisons, Galactic Commonwealth, extragalactic threats, Department of Defense, voidjumping, Assembly, Talaphrian Order, Talaphria, hardlight, antineutronium orbs, Theomachy, voidslashes, Elder Races"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "TYPE", "CLASS", "LOCATION", "AUTHOR", "LAST UPDATE"]
infoentries = ["History", "First Contact", "Incident", "Outlands", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Silent Elder Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['galacticcommonwealth-lore', 'talaphrianorder-lore']

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

article = """===SILENT ELDER
In the gaps between galaxies, in a cold realm known as the Outlands, there resides engines that were constructed to bear their sleeping creators to the time when the stars have grown dim and the universe has grown cold. Their function is variable, with as many being tombs as prisons. Opening such pandoran vessels may awaken a benevolent god or a sleeping devil. One of these objects was discovered by the {Galactic Commonwealth} during a routine patrol for extragalactic threats. It was a smooth sphere of onyx coloration with at least three hundred kilometers in diameter. Upon approaching the object, black figures arose straight from the surface of the sphere as if it were a liquid and lunged at the party, cutting off all further transmissions. Whatever this object was, it was hostile, and it possessed the capability to destroy an entire flotilla of Commonwealth scout ships. A larger fleet was dispatched by the Department of Defense to contain the area and further monitor the object. However, all attempts were again met with hostility, forcing the fleet to voidjump away from the area. The Assembly decided that their ships were not equipped to deal with such a  threat, leading them to turn to the {Talaphrian Order} for aid.
Five Knights Talaphria were contracted to investigate, and if possible, exterminate the entity. Upon arrival, thousands upon thousands of onyx warriors were launched from the sphere, firing at the knights with various weapons of hardlight. These attempts failed, and the warriors retreated into the structure. The knights didn’t dare engage with the object, eyeing it warily during the calm. This calm was cut short, however, when an orifice of pale light opened on the sphere. From it emerged a figure approximately ten meters tall and clad in black spheres. It regarded the knights for a brief moment, before summoning an array of antineutronium orbs, a form of weapon not seen since the Theomachy. In nanoseconds, the projectiles were fired at the knights at speeds nearing the speed of light. The knights were only able to react quickly enough to dampen the blow with rudimentary shields, resulting in the damage weakening them severely. With their remaining strength, they attacked the entity before it could recover its weaponry, trying to tear it asunder with rapid voidslashes. The entity suffered extreme damage, and seemed to sense that its loss was inevitable. It destroyed its home in a great conflagration which killed itself in the process. When the knights recovered, the body and the sphere were gone, supposedly annihilated from the blast. An observer ship recorded this entire ordeal, documenting it as one of the first cases where an Elder was awoken from its tomb. From then on, all structures of this construction were quarantined and made inaccessible to the public."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "silentelder-lore.html"

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
