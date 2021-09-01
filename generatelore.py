# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Madame Martins"

keywords = "​​​​​​postnatal genetic modification, cellular sculpting, fleshcraft, Madame Martins, luxury, reworks, modifications, biotubes, Materna, 20D printers, Creidhne, bespoke robots, nanorobots, chemical therapy, morphs, gargantua type, habitation cylinders, iron-clad golems, dragons, Homo felisians, Argus, mermaids, Ancalagon the Black, Silmarillion (Lord of the Rings), Orpheus Irad, House Irad, aeries, Uriel (the Light of God), Safara Gotfir, House Gotfir, fullerene reinforced bone"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Factions", "Human Domain", "Corporation", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Madame Martins Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['materna-lore']

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

article = """===MADAME MARTINS
The invention of postnatal genetic modification and cellular sculpting bestowed upon humans the ability to modify their bodies as they see fit. This newfound ability was initially used for medical procedures but developed into a form of artistic expression by body artists. This denomination of fashion became known as fleshcraft. Madame Martins, a member of the 9 Muses Group, was established to cater to luxury fleshcraft clients. They accomplish everything from simple facial reworks to full body modification that would make a patient unrecognizable as a human.
==ORGANIZATION
Like any corporation, Madame Martins possesses a Board of Directors, Presidents, Vice-Presidents, Treasurers, Secretaries, and the like. However, the two notable groups are the engineers and the biologists. While the engineers focus on mechanical modifications, the biologists are tasked with making genetic and cellular modifications.
==OPERATIONS
Madame Martins takes pride in their work to redefine what it means to be a human. There is no modification that they cannot accomplish, as their only limitation is their imagination. Engineers and biologists utilize special biotubes built by {Materna} or 6D printers from  Creidhne to construct the specimens their client demands. Bespoke robots then utilize a variety of technologies, including nanorobots and chemical therapy, to either graft specimens onto their clients or modify their clients directly. This process and set of modifications are referred to as a morph.
==LOCATIONS
Extreme body modifications, such as those of the gargantua type, are strictly prohibited from public spaces within most human cities due to them posing a public danger. To address this, Madame Martins constructed specialized habitation cylinders to act as both habitats and social spaces for their clients. These cylinders host a wide range of environments, from deserts to oceans. However, they all converge at a central cylinder where most of the clients inhabit. Here, iron-clad golems tromp on the streets while dragons fly between their aeries. Homo felisians can mingle with a child of Argus while mermaids swim in great glass aquariums. It is a true statement of accommodating architecture, as specialized infrastructure for nearly all major types of modifications are available.
==NOTABLE MORPHS
=Ancalagon the Black
Ancalagon the Black was a dragon from the ancient Silmarillion, a companion book to the Lord of the Rings saga. Within the lore, it could crush mountains and blacken the sky with its wings. Orpheus Irad of House Irad was inspired by this fictional figure, and chose it to be his morph. He constructed a specialized habitation cylinder that would serve as his aerie and constructed an entire division of sculptors to create the morph. Redundant hearts, graphene skin, and lighter-than-air gas sacs were just some of the myriad modifications made to Orpheus’s body. The morph took several months to complete due to the sheer volume of organic and mechanical matter that needed to be printed.
=Uriel, the Light of God
Uriel, the Light of God, was a seraphic morph commissioned by Safara Gotfir of House Gotfir. It is an angel clad entirely in red-orange flame standing at thirteen meters in height. Embedded in the morph’s chest was a greatsword of the same infernal nature. This was accomplished by implanting various glands along the body that produced a gas. This gas would be contained in a small field that, when ignited, produced a smokeless flame. A series of bodily reinforcements such as fullerene reinforced bone were also necessary to aid in helping Safara grow to and maintain the commissioned size."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "madamemartins-lore.html"

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
