# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Karanaan"

keywords = "​​​​​​Karanaan, Traders of the Wandering Sun, Lord-Merchant Olande, Galactic Commonwealth, galactic governments, galactic politics, Bygone Races, Theomachy, stellar engine, Ascendance, Head Chairman of Zvrenda Holdings, Fellowship of Voidwalkers, Nexus, Ikujo Family, pontifices, Society of Silver Scales, Aukhukr Logistics, waystations, wormhole gates, Ergotan International, advanced technologies, Vlahir Communications, wormhole communications, galactic interweb, Taekoti Mining and Manufacturing (TMM), starlifters, automated mining platforms, forge worlds, megastructures, Tykupiel (the Resplendent Aster)"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Factions", "Karanaan", "Guild", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Karanaan Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['galacticcommonwealth-lore', 'milkywaygalaxy-lore#bygone-races', 'nexus-lore']

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

article = """===KARANAAN
The Karanaan, otherwise known as the Traders of the Wandering Sun, are a collective of organizations dedicated to building wealth both in and out of the galaxy. Led by Lord-Merchant Olande, the Karanaan hold sway over the large majority of logistics and financial institutions within the galaxy. While they are highly associated with the {Galactic Commonwealth} and other galactic governments, they are not part of any, allowing them to maintain their sovereignty amidst galactic politics.
==HISTORY
To fill the vacuum in infrastructure left behind by the {Bygone Races} after the Theomachy, the Karanaan was founded. Seven guilds of wandering nomads, each with their own stellar engine, merged under a single banner. Each guild of the Karanaan held equal authority in the collective, with each relying on the others to maintain their own operations at their full capacity. However, the Ascendance of the Head Chairman of Zvrenda Holdings, Olande, disrupted the status quo. Given this new power, Olande reformed the Karanaan to the one that exists during the modern-day.
==ORGANIZATION
The Karanaan are a septet of organizations bound together by Lord-Merchant Olande, Head Chairman of Zvrenda Holdings. Acting in unison, they could be considered one of the most powerful organizations within the Milky Way, with either themselves or their proxies being present in almost every galactic affair.
=Zvrenda Holdings
Zvrenda Holdings is the primary shareholder for all the organizations within the Karanaan, allowing it to posit itself as the collective leader. Led by Lord-Merchant Olande, it is the glue that binds all the different organizations together into a single force. While many initially despised Olande’s takeover of the Karanaan, Olande’s masterful leadership and strength took the collective to new heights and profits, rapidly regaining the support of the guilds.
=Fellowship of Voidwalkers
The Fellowship of Voidwalkers controls almost all commerce that occurs within the {Nexus}, save for other major organizations such as the Ikujo Family. They are charged with forging pacts with pontifices as well as charting new pathways within the Nexus. 
=Society of Silver Scales
The Society of Silver Scales is the primary bank for the Galactic Commonwealth and many smaller governments, charged with keeping track of currency as well as maintaining exchange rates between various currencies.
=Aukhukr Logistics
Aukhukr Logistics is one of the largest corporations within the Karanaan, possessing the most expansive merchant fleets known in the galaxy. This is due to their many services and charges, including transportation of goods and people, monitoring and maintaining the various waystations and wormhole gates, as well as charting new transportation routes for the galactic community.
=Ergotan International
Ergotan International is a private military corporation that not only protects the Karanaan’s interests but also serves as Olande’s private army. They have their own weapons research divisions, allowing them to stay equipped with the most advanced technologies to bring into battle.
=Vlahir Communications
Vlahir Communications monitors and maintains the wormhole communications technology that composes twenty-three percent of the galactic interweb.
=Taekoti Mining and Manufacturing
Taekoti Mining and Manufacturing (TMM) acquires the resources and produces the various goods needed to keep the Karanaan operational. They own expansive fleets of starlifters, automated mining platforms, and even forge worlds, megastructures dedicated to the single act of production for the Karanaan.
==LOCATIONS
The hubs of the Karanaan are stellar engines, machines held to a godlike status within the collective. They number seven, with each of the guilds controlling one. To enable the travel of these gargantuan constructs, each guild must dedicate their engine power to the traveling star in question. The foremost of these engines is Tykupiel, the Resplendent Aster. It is nearly 200 million kilometers in diameter, serving as Olande’s flagship and the home of Zvrenda Holdings."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "karanaan-lore.html"

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
