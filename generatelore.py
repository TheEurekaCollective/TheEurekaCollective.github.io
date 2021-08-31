# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Antimatter"

keywords = "​​​​Human Domain, antimatter, currency, containment units (wells), Sol system, New Heliopolis, solar colonies, Dyson Project, Laser Energy Transport Grid, drones, laser energy, particle accelerators, hermetically sealed container, fuel source, mages, starships, mana-catalyzed antimatter reactors, paraphysical techniques, antimatter credit, weaponry, counterfeit"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "CREATOR", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Items", "Human Domain", "Energy", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Antimatter Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ["milkywaygalaxy-lore", "galacticcommonwealth-lore"]

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

article = """===ANTIMATTER
Within the Human Domain, antimatter is the primary form of energy production and storage. From cities to starships, antimatter powers almost every aspect of life. It is even used as a currency and is stored in special containment units colloquially dubbed "wells."
==PRODUCTION
=Step 1 - Collecting Energy
The production of antimatter within the Sol system begins at various stations of New Heliopolis, a series of interconnected solar colonies that have an orbit close to that of Mercury’s. It serves both as the staging ground for the Dyson Project and the central base of operations for the Laser Energy Transport Grid.
_Dyson Project
The Dyson Project is a long-running initiative to partially cover Sol with an array of mirrors, which will funnel the collected light into tight beams and send them to antimatter production facilities around the system. To do this, material is lifted directly from the surface of the star using strong magnetic fields. Then, manufacturing drones convert this raw material into ultra-thin reflective panels, which become the robotic mirrors that collect and send light throughout the system.
_Laser Energy Transport Grid
The Laser Energy Transport Grid (LETG) is a series of facilities that collect and distribute laser energy throughout the system. Hundreds of these facilities are scattered throughout the Sol System to account for celestial bodies blocking the path of the lasers. The path of these lasers end in various factories dedicated to producing various goods, including that of antimatter.
=Step 2 - Synthesis
At various orbital antimatter plants around the solar system, particle accelerators generate antimatter. This antimatter is then shipped off to various locations or fed to their destination via direct pipeline.
=Step 3 - Storage
A hermetically sealed container known as a well is used to store antimatter safely. It generates a strong internal magnetic field to suspend the antimatter within the center of a vacuum, preventing the substance from making contact with the matter composing the container. The magnetic field can also be manipulated so that the antimatter moves along a designated path. Antimatter pipelines are based on this principle.
==APPLICATIONS
=Energy
Antimatter is used as a portable fuel source for most constructs, including mages and starships which utilize mana-catalyzed antimatter reactors to produce usable energy. These reactors can be miniaturized down to the size of a marble with the aid of paraphysical techniques.
=Antimatter Credit
Long before the 26th century, currency became regarded as simply an analogue for time and energy, so when the technology became available, it made sense to turn energy itself into currency. Antimatter as a currency is referred to as the antimatter credit. This comes in two forms: the physical antimatter credit and the virtual antimatter credit. While the physical antimatter credit is a physical amount of antimatter, the virtual antimatter credit refers to the amount of energy a person can use.
=Weaponry
Projectiles and missiles, such as antimatter warheads, are highly present within the Human Domain’s arsenal.
==SECURITY
Producing antimatter always yields less energy than is invested. This alone greatly deters counterfeiting, but even if counterfeiters attempt antimatter production, the energy signatures generated would easily be picked up by scanners."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "antimatter-lore.html"

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
