# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Kalatari Origin"

keywords = "​​​​​​Kalathron, waves of plasma, stone skies, volcanic vents, flora, fauna, Skago, sophont, Prinor, steel magic, iron flesh, Fallen Star, stone sky, underground lake, Grand Matron Talavale, Dragonslayer, liquid light, metal husk, golden lightning, halo of hardlight, voids of space, cosmos, heroes of the past, Kalatar, Firstborn, Revelator Scyanthus, Mouth of the Fallen Star, legions of living iron, blessings, Kalatari, Children of the Fallen Star"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Stories", "Kalatari Domain", "Origin", "Kalatari", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Kalatari Origin Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['kalatari-lore#prinor', 'kalatari-lore']

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

article = """===KALATARI ORIGIN
==CHAPTER 1 - FIRSTBORN
The world of Kalathron revolved around a cruel sun. Great waves of plasma would sweep across the planet, cursing those it came in contact with. However, life found a way to survive, not on the surface, but within deep caverns. From above, stone skies shielded life from the scorching rays, allowing only what was necessary to pass through. From below, volcanic vents would feed the various flora and fauna, allowing life to eventually advance to that of a sophont species, a reptilian race known as the Skago. They were a collection of primitive tribes, distributed throughout the myriad continents of the planet. One of these tribes called themselves the {Prinor}. They were hunters, slayers of great beasts. They adorned their bodies with the remnants of such beasts, so that their strength may be known to all. It was them who would first grasp the art of steel magic and bestow upon themselves iron flesh.
Tales speak of the Fallen Star breaking through the stone sky, its body coming to rest at an underground lake near a Prinor settlement. The greatest of this tribe was Grand Matron Talavale, the Dragonslayer. Talavale, curious as to what had fallen from the Lands above, led her people into the murky depths of the lake. Through the deep water, she was able to see liquid light pouring from a metal husk, permeating throughout the lake. Talavale reached out her hand, for she had never seen such a beautiful sight before. When she did, she was enveloped with golden lightning. It began changing her, with a halo of hardlight manifesting itself above her head. Through a great trial of pain, her body was made anew. Steel scales replaced ivory plates, her bones gained strength rivaling that of iron. Images from a thousand lives flooded her mind. She saw stars grow dim and die. She touched the voids of space and felt what came at the edge of the cosmos. When the process was over, she finally understood; the body before her was not of this age, or even of this world. It was old, much older than even the heroes of the past. She gave the husk before her a name: Kalatar, the Fallen Star. It would serve as the god of her people, the Firstborn. But most of all, Talavale was no more; she was now Revelator Scyanthus, Mouth of the Fallen Star. Legions of living iron marched across the continents, spreading the blessings of Kalatar for the next 1,000 years. When this was done, the Skago people were no longer. They were known by a new name: the {Kalatari}, Children of the Fallen Star. """

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "kalatariorigin-lore.html"

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
