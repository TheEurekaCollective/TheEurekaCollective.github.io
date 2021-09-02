# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Spell Rifles"

keywords = "spell rifles, combat mages, wands, hermetically sealed, psionic pylon, computation module, fire control system, bespoke weave, neural seed, Psionic Interference, somatic cable, internal matrices, burnout, computation module, spell capacitor, AI, thread receiver, mental commands, mana-catalyzed, antimatter, microreactor, neural interface, Paraphysics Division, 6D Vacuum Printing, Hardlight Construction"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "CREATOR", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Items", "Paraphysics Division", "Weapon", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Spell Rifles Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['combatmages-lore', 'magus-lore']

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

article = """===SPELL RIFLES
Spell rifles are the primary form of armament used by {combat mages}. They are military-grade wands dedicated to aiding a {mage} in focusing their spells and delivering them over long distances towards targets. They allow a mage to convert what would have initially been a random spray of information into a condensed beam. These weapons are recoilless, silent, and are hermetically sealed to prevent tampering.
=Components
While the manufacture and structure of spell rifles vary, they are most often composed of a psionic pylon, computation module, fire control system, power supply, and frame.
_Psionic Pylon
The psionic pylon is the primary functioning component of the spell rifle.  It is a bespoke weave of neurons grown using the mage’s personal neural seed. These neurons are woven in such a special matrix so as to afford the mage higher degrees of accuracy when casting their psions. Using the principle of Psionic Interference, psions are transferred directly from a somatic cable to the psionic pylon. These focus the psions and turn what would be a wild torrent of spells into a precise beam of information. Accuracy of a spell rifle is highly dependent on the length of the pylon and the complexity of the internal matrices. Rapid, repeated use of a pylon may wear out the neural integrity or cause overheating, an effect known as burnout. This may necessitate the periodic replacement of a pylon.
_Computation Module
The computation module both stores low-power spells and with a spell capacitor, it can interpret and compose spells that come from somatic threads. It can also store an AI so as to further assist the mage in terms of aiming and firing. The stored AI has a degree of authority over the use of the spell rifles. As a result, it can control portions of both the fire control and optical systems.
_Fire Control System
The fire control system is what links all the other systems of a spell rifle together. It is composed of the trigger, toggle buttons, and thread receiver. A mage is able to insert its hand-based somatic threads through the thread receiver built into the handle and as a result can operate the weapon using only mental commands.
_Power Supply
While the type varies, the most common is a mana-catalyzed antimatter microreactor. This is used to power the systems without needing to connect directly to the mage.
_Frame
The frame of a spell rifle is a shell that the parts of a spell rifle are placed into for ease of manipulation. High resolution sensor packages are often integrated into the frame so as to assist with aiming and data collection. This information is delivered to the mage via direct neural interface.
=Internal Explosive
When used by an unauthorized individual, the weapon will explode and destroy itself.
=Production
The individual components are produced by the Paraphysics Division utilizing a mixture of 6D Vacuum Printing and Hardlight Construction."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "spellrifles-lore.html"

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
