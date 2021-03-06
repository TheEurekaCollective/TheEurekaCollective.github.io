# coding=utf-8

# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Rebirth"

keywords = "Theomachy, Aunox, soulfire, Saga, War in Heaven, War of Dreams, War of the Gods, War of the Broken Sky, War of the Split Disk, the Greatest War, prophets, ennead, Nagel, the Pale Hunger"

# This is the title of the art piece that shows up on the page,
# it's probably the same as the page title but make sure it's all caps
arttitle = "REBIRTH"

# This is where the image is stored, make sure the address is
# in relation to where the html file will be located (it'll
# probably look something like resources/artthing.jpg)
imagelocation = "resources/Rebirth.jpg"

# This is the description of the art piece that'll show up
# as the block of text on the right, make it as long as you
# want there'll be a scroll thingy there too
description = "“Come, my children. Climb out from my furnace-womb and be granted with new life. Clad yourselves in the flesh I made for you, and in return, bring my Dream into fruition.” - Nagel, the Pale Hunger"

# this is the link to the corresponding lore page, don't
# include the .html extension because when it's uploaded
# the link will work without that extention (so instead
# of thingy-lore.html just write thingy-lore)
lorepage = "saga-lore"

# this is the location of the artist's profile picture,
# also make sure it's addressed properly (probably
# something like resources/memberprofiles/face.png)
artistprofilepicture = "resources/memberprofiles/Xiaoshen Ma With Flame.jpg"

# this is the artist's name
artistname = "Xiaoshen Ma"

# this is the artist's role (probably just 'Artist'
# but if you wanna change it up it's there to change)
artistrole = "Artist"

# this is the file you want to save the html code in
# (this time you have to include the .html extension)
filename = "rebirth-art.html"

# ignore this stuff
s = open('arttemplate.txt', 'r').read()
s = s.replace("(PAGETITLE)", tabtitle)
s = s.replace("(KEYWORDS)", keywords)
s = s.replace("(IMAGELOCATION)", imagelocation)
s = s.replace("(ARTHEADING)", arttitle)
s = s.replace("(ARTDESCRIPTION)", description)
s = s.replace("(READMORE)", lorepage)
s = s.replace("(ARTISTPFP)", artistprofilepicture)
s = s.replace("(ARTISTNAME)", artistname)
s = s.replace("(ARTISTROLE)", artistrole)
f = open(filename, 'w')
f.write(s)
f.close()
