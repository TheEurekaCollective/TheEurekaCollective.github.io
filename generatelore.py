# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Nexus"

keywords = "Nexus, transportation, Void, Theomachy, highway systems, mass shadows, Material Plane, gravitically dead, pontifices, sectors, vacuum corridors, Nexus Gate, Galactic Commonwealth, Fellowship of Voidwalkers, Karanaan , Damdayu (the Freewalker), Ikujo, Zaramin, black market, Free City of Jakka, Lost Civilization of Indalu., voidborne vessels"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Locations", "Mixed", "Gigastructure", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Nexus Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['cosmology-lore#void', 'cosmology-lore#material-plane', 'galacticcommonwealth-lore', 'karanaan-lore']

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

article = """===NEXUS
The Nexus is a complex series of transportation systems residing within the {Void}. While it is unknown as to who constructed it, it is theorized to be from before the Theomachy. This system is special from the jump and Void highway systems in the sense that it can pass through mass shadows originating from the {Material Plane}. It is essentially gravitically dead from both the inside and the “outside.”
==DENIZENS
The primary denizens of the Nexus are a group of intelligences known as pontifices (singular
pontifex). Pontifices each have their own section of the Nexus that they possess full control over. Each pontifex acts independently of each other, possessing their own wills and personalities. They can be hostile, friendly, or neutral, with said dispositions seemingly chosen at random. To traverse a specific section of the Nexus, a traveler has to be approved by the sector’s pontifex. Currently, thousands of these sectors and pontifices exist, with some beyond the edge of the galaxy.
=Pontifex Hostilities
Pontifices possess a form of free will and so some of them exhibit hostilities towards one another, as their primary precept is that of expansion. This leads to battles between pontifices, with the victor overtaking the sector of the vanquished.
=Dead Pontifices
A pontifex is very rarely killed by a non-pontifex. In those instances, their sector would either be left derelict or consumed by a neighboring pontifex.
=Defense
Intruders are dealt with by pontifices swiftly through methods such as closing itself off, collapsing tunnel sections, or even opening itself up to the Void. What might be a planet-sized tunnel one second may be a pinhole the next. However, these actions are highly energy intensive and most pontifices usually resort to using defense constructs known as sentinels. Akin to pontifices,  sentinels are also highly varied. Some are swarms of nanomachines while others are melee-oriented golems. Attempts to remove portions of the tunnels are also met with deadly force.
==ENVIRONMENT
The Nexus, in its base form, is simply a series of small vacuum corridors. Travelers with the proper permissions can request that a tunnel be dilated or contracted, or that a specific section be terraformed. As a result, certain pontifices have allowed various ecosystems and constructs to flourish.
==TRAVEL
To enter the Nexus, one must use a designated Nexus Gate. They are rings of variable size spread throughout the galaxy. There used to be many spread throughout the galaxy, but the Theomachy had destroyed many, leading to a massive reconstruction project after the war. However, since opening a Nexus Gate requires the permission of a friendly pontifex, various factions maintain control over their own gates. There exists at least one Nexus Gate within each major city of the {Galactic Commonwealth}.
==GROUPS
Many factions have arisen over time to take advantage of the Nexus and the pontifices.
=Fellowship of Voidwalkers
The Fellowship of Voidwalkers is a subset of {Karanaan} dedicated to exploring and mapping the multitude of pathways of the Nexus. They designate greenlit sectors and maintain some dead sectors. Due to the geography and politics of the Nexus constantly changing, the task of the Fellowship of Voidwalkers is considered to be very important. Within this faction also resides a cult, worshipping a prophesied figure they call “Damdayu, the Freewalker”. This entity would be universally regarded as friendly by all pontifices, allowing it to travel unabated throughout the Nexus.
=Ikujo
The Ikujo are an expansive and powerful crime family that have forged a pact with a pontifex known as Zaramin. They specialize in all sorts of black market activity, but their main forte within the Nexus is the smuggling of goods considered illegal by the Galactic Commonwealth.
==EXPLORATION
Due to the risk posed by a potentially hostile pontifex, new sectors are explored via remote drones deployed by the Fellowship of Voidwalkers.
==NOTABLE LOCATIONS
Various permanent locations have been established or found within the Nexus, including the Free City of Jakka and the Lost Civilization of Indalu.
==INCIDENTS
On very rare occasions, a voidborne vessel will crash into one of the tunnels that compose the Nexus. If it is big and fast enough, it may destroy parts of the underlying structure."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "nexus-lore.html"

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
