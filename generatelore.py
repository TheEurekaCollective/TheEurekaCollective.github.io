# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Materna"

keywords = "​​​​​​Materna, biotechnology, cloning, prenatal modification, artificial births, Faber Technologies, Variable-Organic Apparatuses, BioTubes, corporation, landside, spaceside, artificial birthing clinics, genes, genetic template, embryo, artificial uterus, polymers, tailored life support system, monitoring sensors, Class-3, human cloning, banned, organs, pets, redundant heart, extra kidney, artificially created organs, hyperlungs, endocrine manipulators, crimson retrievers, great chihuahuas, state-of-the-art, printers, duplicating cells, Gene Hosting, Gamete Hosting, Genetic Banks, genetic lineages, Medicine, Medical BioTubes, culture cells, injured cells, nutrient mix, specially-made viruses, pill, kill code, Gene Tagging, biological products, Materna Genetic Tag, isolated section, artificial genetic code, Materna Corporation, child, mother, grandmother, one-time fees, subscriptions, ecosystem, organic growth capacity, 25 kilograms, 50 kilograms, 100 kilograms, cellular matter, Class 1 subscription, Class 2 subscription, Class 3 subscription, Class 4 subscription, Class 5 subscription, Organization Class subscription, Expedited Medical Program, Priority Medical Pickup, Priority Biotube Replacemnet, Priority Organ Replacement, Yearly Organ Upgrades, unlimited kilograms, growth rates"

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
infoimagesource = "resources/Materna Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['madamemartins-lore']

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

article = """===MATERNA
Materna is one of the largest companies in the biotechnology sector and focuses on providing services such as cloning, prenatal modification, and artificial births. They are a subsidiary of Faber Technologies and have existed since the mid-21st century. They utilize the trademark Variable-Organic Printing Apparatuses, otherwise known as BioTubes, to grow and modify organics.
==OPERATIONS
Materna is an extremely large corporation and has stakes in almost every portion of the human technologies sector. Materna facilities could be found in almost every landside or spaceside city.
=Artificial Births
The primary focus of Materna’s operations is the artificial birthing clinics. These are facilities where babies are grown and modified. To begin the fully automated process, genetic samples are extracted from the parents and are mixed to create a genetic template. Desired genes are added and undesired genes are removed. The genetic template is then codified for storage. An embryo is generated based on the genetic template and placed within an artificial uterus. This artificial uterus is made of advanced polymers and has both a tailored life support system and monitoring sensors to ensure that the baby grows up healthy and any complications during the growing process are addressed quickly. The growing period usually takes nine months, but people with a Class 3 or greater subscription can have it decreased up to merely two months.
=Cloning
While human cloning is officially banned, organs and pets can be cloned. Organs are not only made to replace existing organs, but also act as an additive. It is not uncommon to see a person with a redundant heart or extra kidney. Artificially created organs, such as hyperlungs and endocrine manipulators, are popular. Pets can also be created with specific traits in mind, some being completely unnatural. Crimson retrievers and great chihuahuas are some of the pets that have been made possible.
=BioTube
Materna’s state-of-the-art BioTubes are containers that are suitable for the culturing and duplicating of cells. They are essentially printers for organics.
=Gene and Gamete Hosting
Many families have their entire genetic lineages hosted within the Genetic Banks of Materna.
=Genetic Modifications
People can pay to have specific snippets of their genetic code removed or added to.
=Medicine
Medical BioTubes not only have the capacity to culture cells but also heal injured cells. Injured individuals are placed into a deep sleep and are submerged in a nutrient mix. Specially-made viruses are then injected into the system to perform operations on the individual. After the treatment, an individual takes a pill that sends a kill code to the viruses, which are promptly decomposed and excreted.
=Gene Tagging
Almost all biological products of Materna possess the Materna Genetic Tag. This isolated section of artificial genetic code marks the product as originating from the Materna corporation.
==BUSINESS MODEL
Most people have their entire families placed in the hands of Materna. In fact, a child, her mother, and her grandmother might have all been grown in the same BioTube. There are two ways that people can pay for Materna’s services: one-time fees and subscriptions. However, one-time fees are unusual as usage of Materna and their ecosystem is quite common. There are six classes of subscription services, each offering a different set of benefits and services. Organizations such as {Madame Martins} can also take advantage of organic growth capacity.
=Class 1
For a Class 1 Subscription, one person can get cells, gametes, and gene hosting. This is the first, and only free, tier of Materna subscriptions.
=Class 2
For a Class 2 subscription, one person can get 25 kilograms of cellular matter made a year.
=Class 3
For a Class 3 subscription, one person can get 50 kilograms of cellular matter made a year.
=Class 4
For a Class 4 subscription, one person can get 100 kilograms of cellular matter made a year and a spot in the Expedited Medical Program.
=Class 5
For a Class 5 subscription, one person can get Priority Medical Pickup, Priority Medical Biotube Reservation, Priority Organ Replacement, Yearly Organ Upgrades, and unlimited kilograms of cellular matter made a year.
=Organization Class
This is the most expensive, but offers lower rates for employees of the organizations as well as incredibly cheap cellular matter growth rates."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "materna-lore.html"

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
