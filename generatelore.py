# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Human Spells"

keywords = "​​​​​​spells, thaumaturgy, psions, mana , emitters, Ancient Thaumaturgy, formulas, chants, Modern Thaumaturgy, neural extension, cognition improvement, ritual, neural interface, psion generation, spell collection, Spell Compendium, Fusion Point, Atmospheric Repulsion, Material Compression, hyperelements, Ionize, Hardlight, lightspeed weapons, Psionic Interference, static spells, scalar spells, casting"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Subjects", "Human Domain", "Thaumatology", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Human Spells Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['paraphysics-lore#thaumatology', 'humanthaumatology-lore#ancient-thaumatology', 'humanthaumatology-lore#modern-thaumatology']

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

article = """===HUMAN SPELLS
Spells are the foundation of {thaumaturgy}, serving as which thaumaturgical phenomena are generated. They are energy-information packages composed of psions and mana, cast from devices known as emitters.
==HISTORY
During the age of {Ancient Thaumatology}, methods of spell composition and casting often took the form of various written formulas and verbal chants. Thaumaturgists of this time believed that the formulas and chants themselves caused the phenomena to occur, leading to inconsistent or inefficient casting. In reality, the formulas and chants guide the caster’s thoughts to produce the thaumaturgical phenomenon. This was later realized during the age of {Modern Thaumatology} and improved upon using various technologies such as neural extension and cognition improvement.
==RITUAL
A ritual is a process in which spells are composed and cast. This specific outlined process details a technologically assisted ritual, the most common method in the year 2570.
=Acquisition
A thaumaturgist mentally designates a system in a specific location. This system is where the psions are going to impact the infons.
=Calculation
An AI scans the system and makes an approximation as to the number of particles present in it. Calculations are then made to determine the present physical properties of each particle and what they will be after the spell has affected them. Once the property solutions are calculated, the AI will send them to the neural interface of the thaumaturgist.
=Translation
The neural interface accepts and translates the property solution into information that the thaumaturgist's brain will understand.
=Psion Generation
The translated property solutions are interpreted by the brain and translated into psions.
=Spell Collection
Mana and psions are pooled into an information and energy package, officially becoming a spell.
=Spell Delivery
The spell is either sent unassisted or with an emitter towards the desired target. Due to the lightspeed nature of psions and mana, as well as them exclusively interacting with conceptual particles, a spell-making impact with its target seems to be a spontaneous phenomenon to the average onlooker. For example, a thaumaturgist making use of a fire spell might launch the spell from their wand, but instead of leaving a visible flaming trail, it simply appears at the target at the speed of light.
==SPELL COMPENDIUM
=Fusion Point
Fusion Point is a spell that compresses atomic nuclei in a specific area into a much smaller area, forcing fusion reactions to occur. This spell is used widely in both combat as well as energy production.
=Atmospheric Repulsion
Atmospheric Repulsion is a spell that actively pushes air away from the emitter. This is especially useful in both increasing the aerodynamicness of atmospheric craft and acting as a form of propulsion.
=Material Compression
Material Compression is a spell that increases the density of particles within a target system. This can be used to increase the sharpness of a blade, reinforce physical armor, or even synthesize hyperelements.
=Ionize
Ionize is a spell that converts particles in a system into a plasma, which could be turned into a weapon or as a form of energy shielding.
=Hardlight
Hardlight is a spell that forces photons in a given system to slow down to a crawl, which forces them to gain mass. This creates a form of solid light, which is incredibly useful in fields such as quantum computing, superconductor development, and lightspeed weapons development.
=Psionic Interference
Psionic Interference is a spell that utilizes a caster’s own psions to interfere with another caster’s psions. This could be used in surveillance to detect when spells are being cast as well as used to interfere with spells in a specific area, creating a form of area denial.
==SCALING
Most casting methods can be divided into two categories: static and scalar. While static spells are able to bypass the computation phase of casting, they aren’t adaptive as they produce almost the same phenomenon every time they are casted. However, they can be chained and combined to produce varied effects in a small amount of time. Meanwhile, scalar spells utilize the computation phase to create a spell uniquely suited to a certain situation, meaning lower rates of casting but higher degrees of potency."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "humanspells-lore.html"

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
