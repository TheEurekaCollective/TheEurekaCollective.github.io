# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Faster Than Light"

# This is the information that will appear in the lil box on
# the right, the order the entries appear in the box is:
# 1 4
# 2 5
# 3 6
infoheadings = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"]
infoentries = ["Subjects", "Mixed", "Superluminal", "Mixed", "Sirawyn", "September 1st, 2021"]

# this is the address of the image that appears in the lil
# box on the right, make sure it's relative to the html file
# (probably something like resources/image.jpg)
infoimagesource = "resources/Faster Than Light Icon.jpg"

# if the article has links, put the addresses for those links
# here. They must be listed in the same order as they appear
# in the article. You can omit the .html extension
articlelinks = ["/"]

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

article = """===FASTER THAN LIGHT
Within {Project Anima}, there have been many methods in which faster-than-light (FTL) is accomplished and utilized. This article is a compendium of all faster than light capable phenomena and applications. It can be noted that many of these systems could be used in tandem for different results.
==WARP
Warp is the compression and expansion of space-time using a warp drive. With advanced gravitics and quantum manipulation, a bubble is generated in which the area in front of the vessel is compressed while the area behind the vessel is expanded to compensate. Warp speeds are affected by the size, shape, and efficiency of the warp field.
=Warp Shielding
When a warp bubble is projected, spacetime in the area becomes skewed and becomes difficult for sensors to understand. This allows ships that host a warp drive to use the bubble as a form of shielding.
=Warp Weaponry
Warp drives are extremely expensive. However, in rare instances, an explosive device can be fitted with a warp drive.
==VOID
The Void is a higher-dimensional space that is composed purely of mana. One location in the Void can coincide with multiple locations in the Material Plane. This property allows for travel within the Void to be much faster than travel in the Material Plane, a practice known as voidjumping. The Void is theoretically infinite and is hostile to all forms of matter. As a result, travel into the Void requires using a reality stabilization field and a spatial auger. Spatial augers allow ships to tear through space-time and enter Void space while a reality stabilization field protects ships from the Void. Should a reality stabilization field fail, its contents would disappear completely. Travelers of the Void must also be wary of large gravitic influences that stem from the Material Plane, as gravity possesses the ability to penetrate space-time. Should a vessel intercept a large gravitational field, it might be pulled off its designated course. To address this, advanced computers calculate a voidjump solution before entering the Void.
=Void Submersibles
Void Submersibles are ships designed to operate for long periods in the Void without reentering the Material Plane.
=Void Carriers
Void Carriers are a type of spaceship that exhibits a very large reality stabilization field. This allows for ships without a void drive to hitch on for a ride within the reality stabilization field. This requires significant degrees of coordination as the ships have to move in unison and at the same speeds so as to not accidentally leave the field and enter the Void.
=Void Tracking
Just as gravity from the Material Plane penetrates spacetime into the Void, gravitic signatures could be detected within the Void from the Material Plane.
=Constructs
With the proper technology, constructs such as the Nexus and the Void Wyrms could be established within the Void.
=Void Wormholes
While wormholes function within the Void, their calibration systems are skewed and thus have the possibility of inducing a paradox. Since a single location within the Void can represent multiple locations within the Material Plane, a wormhole passage can be split between multiple locations, and thus destroy whatever travels through.
=Void Tactics
It is common for spaceships to rapidly enter and exit Void space to evade the enemy during ship-to-ship combat.
==WORMHOLE
A bridge between two spaces in spacetime is known as a wormhole. Wormholes are one of the fastest methods of FTL but also the costliest due to the nature of wormhole energy consumption. While the size of a wormhole is expanded in a scalar fashion, the required energy input rises exponentially. It also takes a much larger amount of infrastructure compared to most other forms of FTL travel. Wormhole travel effectiveness drops over large distances due to an accumulation of Yunian Uncertainty. To address this issue, wormhole relay stations are utilized.
=Wormhole System
A system of wormholes gates were established by the Pathfinders Legion for the Galactic Commonwealth. Nearly all major systems have access to one or more wormhole gates. These wormhole gates are relatively small and are open for short bursts at specific times. It is common to see fleets of spaceships arrayed in front of offline wormholes awaiting their opening. It is also common for ships to link their navigation systems with one another to maintain the best balance between speed and cohesion.
=Wormhole Cooling
One of the main pitfalls for any spacefaring object is the amount of heat that needs to be released or decreased. One of the methods devised to help alleviate this issue was to use a wormhole as a cooling system. High-energy matter would be dumped through the wormhole into an off-site cooling facility. This method has also been used in the reverse, allowing for ships with wormholes to be supplied indefinitely. The stellar engines used by the Traders of the Wandering Sun utilize this technology extensively.
=Quantum Wormholes
Small wormholes are generated and allow for superluminal communications, which can include photons and radiowaves.
==ANIMA
Anima-based FTL can be divided into two categories. These are designated binary systems and singularity systems. A binary system requires the use of two hosts while a singularity system only needs one.
=Binary Systems
=Transpositioning
The Bygone Races had mastered the art of transpositioning, a method of FTL where an object is uploaded to the conceptual plane and placed via an anima in a different location. However, this requires a host to already be at the target location.
=Ansible
Ansibles are utilized by organizations such as the Scribes Consortium to allow for FTL communications using an anima as a medium.
Singularity Systems: Singularity systems use anima to produce the FTL systems described above. Essentially, they empower a host to be able to enter the Void, generate wormholes, or warp space. """

# this is the file the html gets saved in, make sure to include
# the .html extension
filename = "fasterthanlight-lore.html"

# ignore this stuff
article = article.replace('{', "<a class='infolink' href='(LINKGOESHERE)'>")
article = article.replace('}', "</a>")
for link in articlelinks:
	article = article.replace('(LINKGOESHERE)', link, 1)

htmlcode = ""
lines = article.split('\n')
for line in lines:
	if len(line)>=3 and line[:3]=='===':
		htmlcode += "\t\t<h1>" + line[3:] + "</h1>\n\t\t<span class='underline'></span>\n"
	elif len(line)>=2 and line[:2]=='==':
		htmlcode += "\t\t<h2>" + line[2:] + "</h2>\n\t\t<span class='underline'></span>\n"
	elif len(line)>=1 and line[:1]=='=':
		htmlcode += "\t\t<h3>" + line[1:] + "</h3>\n"
	else:
		htmlcode += "\t\t<p class='infoparagraph'>" + line + "</p>\n"

s = open('loretemplate.txt', 'r').read()
s = s.replace('(PAGETITLE)', tabtitle)
s = s.replace('(INFOIMAGE)', infoimagesource)
for i in range(6):
	s = s.replace('(H'+str(i)+')', infoheadings[i])
	s = s.replace('(I'+str(i)+')', infoentries[i])
s = s.replace('(CONTENT)', htmlcode)

f = open(filename, 'w')
f.write(s)
f.close()
