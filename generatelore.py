# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Koios Institute"

keywords = "​​​​​​Koios Institute, Terran Union, astrogeology, biology, Horizon League, celestial maps, United Celestial Cartographers, Terran Accords, generation ships, faster-than-light research, Human Heritage Preservation Society, Human Heritage Reserve (Artifact City), Acropolis, Pyramids, Terracotta Army, superluminal drives, Foundation of Biology, Habitats, arcologies, animal translators, Human Domain, Octavius, Terran Environmental Assembly (TEA), Terran Environmental Restoration Projects"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Factions", "Human Domain", "Science", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Koios Institute Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['milkywaygalaxy-lore']

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

article = """===KOIOS INSTITUTE
The Koios Institute is a collection of loosely related organizations within the Terran Union. They are responsible for the exploration and investigation of various phenomena within the universe, including astrogeology and biology.
==ORGANIZATIONS
=Horizon League
The Horizon League is dedicated to exploring the vast expanses of space. They maintain humanity’s celestial maps and establish new stations as they go. Their predecessor was the United Celestial Cartographers, but this changed after the Terran Accords due to the assimilation of other organizations. They have been the source of many exploration efforts such as the creation of generation ships and faster-than-light research.
=Human Heritage Preservation Society
The Human Heritage Preservation Society is charged with collecting and preserving human artifacts from throughout human history.
_Human Heritage Reserve
The Acropolis of Athens no longer serves as the base of the Parthenon, Cairo no longer rests under the shadow of the Pyramids, and the Terracotta Army no longer stands in Qin Shi Huangdi's mausoleum. Those, and other cultural artifacts of the human species, have been transported to the Human Heritage Reserve of the Human Heritage Preservation Society. The reserve, also known as Artifact City, is composed of several interconnected cylinders of varying sizes. Each reserve has an artificial sun and a unique biosphere. Entire cities have been transported to this reserve in order to protect them from degradation and natural disasters. This facility is public and free to access, encouraging millions to visit the facility every day. These reserves are also equipped with superluminal drives, so that the artifacts may escape in the event of an emergency.
=Foundation of Biology
The Foundation of Biology investigates all forms of life, both terrestrial and extraterrestrial. They have brought back extinct species, translated animal languages, and researched the alien life of the {Milky Way}.
_Habitats
The Habitats are a series of arcologies created as habitats for extinct species that have been revived through genetic manipulation processes. These arcologies consist of vast artificial environments that best suit their dependent species. Some of the species that have been brought back and inhabit these environments include the Irish elk, wooly mammoth, and dire wolf. Some of the aforementioned species have also been allowed back into their original habitats on Terra, such as the woolly mammoths that currently live in the Arctic tundra.
_Animal Translators
While the uplifting of non-sophont species is still considered highly controversial, animal translators are in fact very popular. These translators are essentially brain-computer interfaces that utilize AI to learn and understand the thoughts of animals. In fact, one of the most famous celebrities within the Human Domain is Octavius, a veined octopus.
=Terran Environmental Assembly
The Terran Environmental Assembly (TEA) monitors and protects the various ecologies present on Terra. This branch was established during the Terran Environmental Restoration Projects, a series of initiatives that utilized natural, technological, and social means to improve the state of the environment on Terra. Some of the initiatives include the restoration of the polar ice caps, the construction of carbon sequestration plants in cities, and the subsidization of underground vertical farms. These and many more projects have helped humankind live in harmony with nature. Now, solar farms cover the various deserts of the world, cities of white are clad in flora and fauna, and the dodos once again tread the island of Mauritius."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "koiosinstitute-lore.html"

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
