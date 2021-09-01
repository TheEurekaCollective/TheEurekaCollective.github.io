# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Operation Helios"

keywords = "​​​​​​Helios Class, Appalachia Rejectionist Enclaves, USNA, Seekers, Intendant Eureka, Stealth Station Tarnhelm, HALO-Assisted Drop Pods, subsonic flight, Scramblers, Huginn reconnaissance drones, aerial hypnotics drone, amnestic application, Cataphract Dropships, Hard-Body Combat Androids, Scrappers, Programmers, non-combat drones, Stasis Containment Unit, Hermetic Biovault, Gotfir, House Faber"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Stories", "Human Domain", "Mission Log", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Operation Helios Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['combatmage-lore']

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

article = """===OPERATION HELIOS
Mission Log Start
Terran Time: 22:30
Terran Date: 24-11-2570
Subject: Candidate Extraction
Codename: Operation Helios
00:00: Helios Class Candidate detected and confirmed in the Appalachia Rejectionist Enclaves of the USNA.
02:00: 7 {Seekers} and the local drone contingent coordinated by Intendant Eureka were deployed from Stealth Station Tarnhelm.
04:00: Seekers made landfall through the use of HALO-Assisted Drop Pods twelve kilometers from the target destination. On subsonic flight, they approached the target destination.
4:30:  Seekers reached the Rejectionist Compound. Sensor Scramblers were activated and Huginn reconnaissance drones were able to obtain a lock on the Host and Candidate. 4 Seekers were deployed to establish a perimeter while 3 Seekers were sent to retrieve the Targets.
05:10: Entire compound successfully put to sleep via aerial hypnotics drone.
05:14: Host and Candidate were apprehended. In-situ Host-to-Container surgery and amnestic application initiated.
06:57: Detection Sector Z breached. 23 Cataphract Dropships and 7300 drones of unknown origin descended upon the compound. Seekers and friendly drones were able to destroy 21 dropships and 7043 drones before they made landfall. The two dropships that remained were able to deploy 170 Hard-Body Combat Androids.
08:17: 2 dropships, 170 HBCAs and 257 unfriendly drones successfully eliminated. Total casualties were 562 friendly drones, 8 civilians, and 0 Seekers.
10:42: Candidate successfully extracted and Seekers exited the compound. Scrappers and Programmers deployed. Non-combat drones recalled to local retention facility. Non-combat drones memory wiped.
21:00: Seekers and Candidate returned to Tarnhelm via Imran Stealth Dropship. Seekers placed to sleep. Candidate transferred to Stasis Containment Unit. Unit placed in Hermetic Biovault 3.
65:26: Scrappers’ and Programmers’ tasks completed. Returned to a local retention facility. Memories wiped.
Mission Log Finish
Administrator: Intendant Kanté
Addendum: Upon further inspection, the Cataphract Dropships, drones, and HBCAs seemed to originate from Gotfir, a proxy of House Faber. """

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "operationhelios-lore.html"

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
