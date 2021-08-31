# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Caspia Interactive"

keywords = "​​​​Caspia Interactive (CI), video games, Human Domain, Dreamscape, virtual reality, Noosphere engine, Vulkan Games, Caspia (artificial island), Caspian Sea, troposcraper, enigmatic council, Rasui Mimoza, Satellites, Superluminal Information Relays, Tolkienesque fantasy, discopunk, brain-computer interface (BCI), Heimdall application, NPC, neural imprint, Temporal Manipulation, Sleep Play, Great Server Merge of 2499, the Union, Oneironauts, simulation-type worlds, memory blockers, Morpheus, Terra"

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
infoimagesource = "resources/Caspia Interactive Icon.svg"

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

article = """===CASPIA INTERACTIVE
Caspia Interactive is the main proprietor of video games within the Human Domain. Their most popular product is the Dreamscape, a virtual reality game built on the revolutionary Noosphere engine.
==HISTORY
Vulkan Games was established in 2060 A.D. as a small indie games company in New Zealand. In 2065, they were able to create the Noosphere Engine, based on the first commercial brain-computer interfaces (BCIs) that came out a few years earlier. They then created the Dreamscape, which was released to the public in 2069. The game blew up nearly immediately, with in-game population numbers growing exponentially. In 2074, the island of Caspia was built in the Caspian Sea. The company was rebranded as Caspia Interactive, with the beginning of the city being built in 2077. Over time, layers and sections of the city were built, eventually culminating in the completion of the troposcraper in 2111.
==ORGANIZATION
The creators of the Dreamscape and the Noosphere network reside as the original and only owners of Caspia Interactive. It is a council of six people. The only member of this enigmatic council that the public is aware of is Rasui Mimoza, the head of the Public Relations department.
==BASE OF OPERATIONS
Caspia Interactive (CI) built an artificial island known as Caspia in the middle of the Caspian Sea. This gargantuan platform is host to a city populated by CI employees, their families, support employees that run the various businesses of the island, and visitors. In the center of Caspia stands a troposcraper that serves as CI’s main base. This troposcraper is primarily filled with servers and system equipment, but specific parts of the building are sectioned off for visitors. It is also said that the founders of CI reside at the top of the troposcraper, but this is uncertain.
==SATELLITES
CI operates swarms of satellites around planets to convey signals quickly and efficiently. They also utilize a significant chunk of the bandwidth of the Superluminal Information Relays.
==BUSINESS MODEL
Dreamscape is subscription-based. However, it is incredibly cheap and most of the money collected is used to run the Dreamscape itself. However, the sheer amount of players has made CI one of the largest companies within the Human Domain.
==DREAMSCAPE
The Dreamscape is a virtual reality game that utilizes the revolutionary Noosphere Engine to host a nearly infinite amount of worlds and universes to explore and enjoy. It is a realm of infinite possibilities as it is not bound by conventional laws of physics. Tolkienesque fantasy worlds to discopunk nightclubs are just some of the locations available to explore. The phenomena of the game can be set to perfectly emulate the real world, with sensations such as pain being indistinguishable from that in real life.
=Noosphere Engine
The Noosphere Engine is a state-of-the-art game engine that has a peculiar way of generating content for the game. Information from history, as well as the memories and experiences of players, are collected and compiled using AI. This allows the system to essentially be self-propagating, with more content generated as more players log in and play.
=System Requirements
Once a person gets their BCI tuned, they can download the Heimdall application. This allows them to enter the Dreamscape. One can access the Dreamscape with most BCIs, however, the speed of the BCI limits what timescales the player can play with.
=NPCs
The Dreamscape is not only populated with players, but also with trillions of nearly lifelike NPCs, from bartenders to dragons. Some of these NPCs are also based on real people who have died and wanted their neural imprint to be placed within the game.
=Temporal Manipulation
Time operates differently within the Dreamscape as compared to the real world. The normal time rate within the game is twice that of real life, but players can customize their worlds’ time speeds.
=Sleep Play
It is necessary for the players to be sleeping (forced or naturally) whilst playing this game due to their BCIs intercepting their bodily signals and translating that into interactions within the Dreamscape.
=Population
As of 2570, nearly 72 percent of humanity regularly uses the Dreamscape.
=Servers
The servers of Dreamscape used to be independent of each other, with each server correlating with a different planet or system. However, the advent of Superluminal Information Relays allowed for the Great Server Merge of 2499, allowing players from all over the Union to play with one another.
=Oneironauts
Oneironauts are a culture of players that create simulation-type worlds within the Dreamscape. They then use memory blockers and enter their constructed worlds. They live out their lives within the Dreamscape, completely oblivious to the fact that they are within a video game. Oneironauts play on speeds several times that of the normal server speed, allowing them to experience lifetimes in their constructed worlds in a matter of a few years. The most famous oneironaut is Morpheus, who constructed a real life analogue to 17th century Terra and conquered the entirety of it.
"""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "caspiainteractive-lore.html"

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
