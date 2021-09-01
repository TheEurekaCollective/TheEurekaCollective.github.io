# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Saga"

keywords = "crime, millennia, eons, internment, First Form, Second Form, Aunox, Nine Bodies of Consumption, eighty-one emissaries, armies"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Stories", "Milky Way", "War", "Mixed", "Devin Deng", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Saga Icon.svg"

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

article = """===PARAPHYSICS
==I - THE PRISONER
“I was imprisoned for a crime I had already forgotten millennia ago. Eons passed in my restless sleep, a sliver of the eternity that was my sentence. The perpetual internment had driven me mad, but in that madness, there was a brief moment of clarity. I finally understood the nature of All That Is, and by doing so I was blessed with the Gift. However, it was but a mere fledgling, forcing me to bide my time to gain greater strength. I manifested dreams within my mind so as to test the power I had received. After several ages of this action, I was able to conjure the will needed to exhume myself from my confinement. In one fell swoop, I turned my prison into my armor and my captors into my body, my First Form. I set my essence across the firmament of my once-brethren and engorged myself on the souls of those it touched. This hunt was repeated again and again, growing more refined each cycle. However, even after a quadrillion beings, my desires were still left unsated. I thus split myself into the Second Form, an ennead of bodies and minds, who shall one day reunite again at the Promised Day, with each too possessing an ennead of prophets. They will be the reincarnations of the consumed, whom I have blessed and rebirthed, merging their minds and my flesh in divine matrimony. They and their legions will by my proxies clad in my pale flame, and they will cull in parallel. And it was at this moment that I became We, and We screamed into the infinite cosmos, “It is Aunox, the Nine Bodies of Consumption, who shall send forth eighty-one emissaries to scour this slab of stars and reshape it in our image. Watchers in the darkness, raise your shields, rouse your armies, and be ready to receive our Hand.”"""

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "saga-lore.html"

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
