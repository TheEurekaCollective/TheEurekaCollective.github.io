# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Akanthe International Park"

keywords = "​​​​Akanthe International Park, Akanthe, void ecology, migration, seeding, life, G-Type Star, Nujim system, Commonwealth Galactic Research Initiative, Theomachy, Galactic Assembly, autotrophs, gravitic well, bucket whales, telescopic eyes, raptors, methane rockets, derma, artificial atmospheres, mutation rates, organizations, Optil Kawau Hotels & Resorts, Akanthe Research Institute, Akanthe Park Service"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Locations", "Galactic Commonwealth", "Natural Park", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Akanthe International Park Icon.svg"

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

article = """===AKANTHE INTERNATIONAL PARK
Akanthe International Park is a series of scientific missions and resorts located within Akanthe and its ring system. This area is designated a Park due to it being one of the few occurrences of void ecology within the {Milky Way Galaxy}.
==ORIGIN
Due to the young nature of the system itself, {Commonwealth} scientists theorized that life did not arise within the system but instead came from an external source through migration or seeding. The flora and fauna that have arisen are incredibly complex and varied, which implies that life has been present in the system for at least a few million years.
==SOLAR SYSTEM
Akanthe International Park rests in the ring system of Akanthe, a planet that orbits around a G-Type Star.
==AKANTHE
Akanthe is a gaseous planet orbited by a ring system with a diameter of approximately 90 million kilometers.
==DISCOVERY
While recovered pre-war data modules have indicated previous knowledge of the Nujim system and its contents, the area was rediscovered by the Commonwealth Galactic Research Initiative after the Theomachy. It was designated as a nature reserve twelve years later by the Galactic Assembly.
==ECOLOGY
=Autotrophs
While some animals possess their own form of autotrophy, primary autotrophs are prevalent throughout the ring system. They are primarily found on asteroids with a suitable gravitic well, or just floating in the form of large planes in the vacuum. Although some autotrophs are capable of photosynthesizing, other portions of the electromagnetic spectrum are utilized as well. Some have even been documented to use photovoltaic cells, which can directly convert light to electricity. Autotrophs of all colors—from purple, pink, and beige for photosynthetic cells to yellow and brown for photovoltaic cells—can be found here.
=Bucket Whales
One of the most notable herbivore species within this ecosystem is the bucket whale, a migratory animal that can span several kilometers in size. They possess incredibly wide mouths that funnel into a small body, which then funnel into an even smaller excretory system. These mouths are used to wrap around drifting autotrophs. A long tongue-like structure then extends from the body and the plant matter is consumed using a combination of chemical and mechanical digestion. After digestion, gas is stored in a rear sac until it needs to be excreted for propulsion. Bucket whales possess four telescopic eyes on stalks that can peek over their large mouth to determine their heading as well as to watch for predators. These eyes can retract into the body in the event of an attack for protection.
=Raptors
One of the primary carnivores that reside within the ring system are the raptors, tentacled predators that orbit asteroids. They possess compound eyes that can spot various herbivores that venture near the surface of their asteroids. Raptors utilize a form of methane rocket to propel themselves toward their prey. They use their hooked tentacles to latch onto their prey which then they promptly consume using a toothed maw. During long periods without food, they may enter a state of orbital hibernation. In this case, their tentacles will wrap around their entire bodies save for their compound eyes. When their eyes detect significant movement, the raptors will immediately reemerge from hibernation to hunt their prey.
=Derma
There exists a fungal organism named derma that envelops celestial bodies, such as asteroids, within the ring system. It is a thin membrane that stretches across the surface of celestial bodies, which allows the fungus to decompose various detritus that fall into the gravity well of the asteroids. This can include the bodies of old raptors as well as the uneaten bits of flesh of the bucket whales.
=Environment
The size of the ring system allowed for a large variety of environments where life flourished. Some of these include artificial atmospheres created by coral-like organisms, ice chunks with sizable amounts of internal water, and the barren surface of asteroids.
=Increased Mutation Rate
Due to the lack of protective magnetic fields or atmosphere within the ring system, the organisms that dwell within are constantly bombarded with powerful radiation, leading to high mutation rates.
==ORGANIZATIONS
Several organizations have been established within the park, including Optil Kawau Hotels & Resorts, the Akanthe Research Institute, and the Akanthe Park Service. """

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "akantheinternationalpark-lore.html"

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
