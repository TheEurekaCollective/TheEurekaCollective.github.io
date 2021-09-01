# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Human Thaumatology"

keywords = "​​​​​​arcane arts, magus cabals, alchemists, mages, thaumatologists, thaumaturgy, Ancient Thaumatology, Verses, Division historians, black powder, Modern Thaumatology, conceptual particles, Lifted Veil Event, Thaumaturgical Revolution, Johannes Siddhar, United States’ Bureau of Paraphysics, Esoteric Energies and Their Properies, mana, Solana Igarashi, Theory of Conceptual Particle Interactions, USSR’s State Research Center of Koltsovo, infons, psions, Terran Accords, Theory of Thaumatology, Paraphysics Division, Human Domain, magic, conceptual particles, esoteric energies, life extension, mana production rate, mana pool, neural networking, cognition improvement, brain-computer interfaces, group casting, emitter, wands, somatic threading, spell composition"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "LOCATION", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["History", "Human Domain", "Thaumatology", "Human", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Human Thaumatology Icon.svg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ['paraphysics-lore#thaumatology', 'humanspells-lore']

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

article = """===HUMAN THAUMATOLOGY
Ever since humankind's inception, the arcane arts have shifted and twisted the tides of history. From the magus cabals and alchemists of yore to the construct mages and thaumatologists of the modern day, {thaumaturgy} has played a pivotal role in humanity’s development as a species.
==ANCIENT THAUMATOLOGY
Ancient Thaumatology refers to the method of archaic and inefficient {spellcasting} utilized by mages of old. This was due to a combination of lack of understanding and technological assistants. During this time, cabals of mages and alchemists, usually elderly, would gather and chant a series of words officially now called Verses. These were psychological tools that helped multiple casters envision the same, or close to the same phenomena. By combining their mana and psions, they would will this envisioned phenomena into reality. Usually, this phenomenon is now considered to be of the tame variety, perhaps the lighting of a candle or the subtle increase of fog in an area. However, this art was inconsistent and rudimentary, with mana and psions being regarded as inefficient from a modern standpoint. While Ancient Thaumatology was devastating on battlefields of swords and shields, Division historians surmise that the increase of wars fought with black powder brought this period to an end.
==MODERN THAUMATOLOGY
The time at which the age of Ancient Thaumatology ended and Modern Thaumatology began is a highly debated topic amongst scholars. However, there are some standings that have more support than most. Many say that the discovery of conceptual particles marked the beginning of Modern Thaumatology. Others say it was the Lifted Veil Event, where thaumaturgical information was disseminated to the public for the first time in the mid-twentieth century. Some go even further, purporting that the beginning of the Thaumaturgical Revolution was the catalyst for Modern Thaumatology.
==DISCOVERY OF CONCEPTUAL PARTICLES
While the discovery of conceptual particles was a convergent event amongst many paraphysical institutes, two scientists are credited with formulating the complete theory of paraphysics. The first was Johannes Siddhar of the United States’ Bureau of Paraphysics, who devised a paper titled “Esoteric Energies and Their Properties” that detailed the energy now known as mana. The second was Solana Igarashi’s “Theory of Conceptual Particle Interactions,” written in the USSR’s State Research Center of Koltsovo, which discussed the existence of infons and psions. They had the two pieces of the puzzle, but due to their organizations being hostile and separate, further developments were unable to be pursued. However, after the Terran Accords were signed and their respective organizations were merged, the two scientists were finally able to collaborate, construct, and complete the Theory of Thaumatology, establishing the foundation for Modern Thaumatology.
==LIFTED VEIL EVENT
The Lifted Veil Event spelled the end for most of the Paraphysics Division’s secrecy. The knowledge of the arcane arts and Modern Thaumatology were disseminated throughout the Human Domain. It was a landmark day for humanity, with thaumatology, in other words, magic, being regarded as real by mainstream scientists and physicists. Historians scrambled to rewrite their thesis while conspiracy theorists went crazy from the idea that some of their ideas were actually true. Prevailing questions humankind had about its own history were finally answered, and the science of thaumatology became a respected study in many schools.
==THAUMATURGICAL REVOLUTION
While the discovery of conceptual particles and esoteric energies were incredibly impactful for human society and understanding of history, the phenomena on their own had little to no application at the time. However, a series of keystone technological developments allowed humanity to finally harness these new forces to their full potential.
=Life Extension
As the age of a person increases, so does their mana production rate. Due to this, many thaumaturgists of the ancient world were quite old, having spent the majority of their lives honing this art. However, the invention of life extension technology allowed any person, provided they live long enough, to eventually gain the mana pool necessary to pull off spells.
=Neural Networking and Cognition Improvement
The invention of brain-computer interfaces and neural computers afforded modified humans a much higher degree of cognition and psion output compared to their unmodified counterparts. It also allowed humans to meld their minds with each other, allowing for more effective group casting. This was instrumental in placing thaumaturgy in the hands of the average citizen.
=Emitter Development
The development of spellcasting devices allowed for more effective spell composition and delivery. The creation of technologies such as wands and somatic threading enabled anyone to wield thaumaturgy with efficiency as well as integrating thaumaturgy in already existing technologies."""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "humanthaumatology-lore.html"

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
