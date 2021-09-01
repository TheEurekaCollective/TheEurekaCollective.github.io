# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "International Space Elevator"

keywords = "​​​​​​Carbon Spire, International Space Elevator (ISE), megastructure, civilization, Apex Station, Terran Union, landside tethering, nanothreads, habitation units, nanolaminates, mana-based active reinforcement systems, living pods, nonliving pods, amenities, skybus, vacuum tram, Old Age"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Locations", "Human Domain", "Megastructure", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/International Space Elevator Icon.svg"

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

article = """===INTERNATIONAL SPACE ELEVATOR
The first Carbon Spire, otherwise known as the International Space Elevator (ISE), is humankind's first megastructure. It is one of the centerpieces of human civilization, ferrying people and goods non-stop between its base platforms and Apex Station.
==HISTORY
By the middle of the 21st century, the Terran Union realized it needed a more efficient way to take ships into orbit. After much debate, the Union approved the construction of the International Space Elevator (ISE) in 2054. In 2059, the first few hundred platforms were built to facilitate landside tethering. By 2062, the first automated nanothread factory was launched into geostationary orbit over the designated base site. The nanothread factory then began lowering its products down to the platforms, where they were connected. This process was repeated thousands of times, with each subsequent tether having a much faster connection process. In 2066, the first test climb was initiated, and turned out to be a success. At this stage, habitation units started being added onto the orbital nanothread factory, turning it into Apex Station. By 2070, the ISE became fully operational, routinely transporting passengers and resources to and from Apex Station. Both the station and tether are continually being expanded at record rates to facilitate the ever increasing flow of goods.
==DESIGN & CONSTRUCTION
=Base
The ISE’s base is composed of hundreds of thousands of platforms spread out throughout the coastal waters of Singapore. The location is important in helping to maintain geostationary orbit above Terra’s equator.
=Height
The ISE is approximately 100,000 kilometers long, which is nearly a quarter of the distance from Terra to Luna.
=Materials
Its primary structure utilizes carbon nanothreads, nanolaminates, and mana-based active reinforcement systems. To supply power, superconductor cables are paired with the carbon nanothread tethers.
=Transportation
Every day, hundreds of thousands of tether runners are sent up and down the elevator to transport people and goods to Apex Station. People are placed in habitable transport pods, otherwise known as living pods, which are equipped with amenities such as in-transit meals and life support safety measures. Meanwhile, nonliving pods are simply vacuum sealed containers storing either raw materials or manufactured commodities. Since both of these pods utilize the same universal locking lugs, tether runners don’t need to differentiate between the two for transport. On average, it takes one or two days to fully climb a tether and reach Apex Station from the base.
=Emergency Measures
In the event that a tether is destroyed, parachutes placed at regular intervals will activate in unison with small explosive charges. The parachutes aid in slowing down the descent of the broken tether as well as breaking the tether into several pieces so it will burn itself up in the atmosphere more easily.
=Apex Station
Apex Station was built around the original nanothread factory that began the ISE. Since its inception, several more factories have been built to facilitate higher rates of nanothread production. The station also keeps tens of thousands of kilometers of extra nanothread in reserve for the event of a tether disconnect. Nanothread production and storage aside, the primary purpose of Apex Station for the people and goods that travel through it is to serve as a jumping-off point to harbors of Luna. As a result, there are many amenities available to travelers awaiting their lunar transport, including restaurants, hotels, observatories, and nature decks.
==OPERATIONS
To begin the transportation operation, people and goods are brought by a skybus or vacuum tram to one of the collection and sorting facilities. These facilities are similar to Old Age airports, where prospective travelers and goods are grouped into their respective pods. Then, a tram takes these groups to their respective tether platform, where a tether runner and open pod awaits them. The travelers enter the pod, diagnostics are made, and the journey up begins. After the travelers have scaled the tether and are deposited into Apex Station, the tether runners and empty pods go back down to restart their transport cycle."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "internationalspaceelevator-lore.html"

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
