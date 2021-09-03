# This will be displayed as the title of the tab, ex "Aeternum"
# will display the title "Aeternum - Project Anima" on the tab
tabtitle = "Cool Title"

keywords = ""

# This is the title of the art piece that shows up on the page,
# it's probably the same as the page title but make sure it's all caps
arttitle = "COOL TITLE"

# This is where the image is stored, make sure the address is
# in relation to where the html file will be located (it'll
# probably look something like resources/artthing.jpg)
imagelocation = "resources/artthing.jpg"

# This is the description of the art piece that'll show up
# as the block of text on the right, make it as long as you
# want there'll be a scroll thingy there too
description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation ullamco laboris nulla pariatur. Duis nulla pariatur. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation fugiat quis nostrud exercitation ullamco nulla pariatur."

# this is the link to the corresponding lore page, don't
# include the .html extension because when it's uploaded
# the link will work without that extention (so instead
# of thingy-lore.html just write thingy-lore)
lorepage = "thingy-lore"

# this is the location of the artist's profile picture,
# also make sure it's addressed properly (probably
# something like resources/memberprofiles/face.png)
artistprofilepicture = "resources/memberprofiles/face.png"

# this is the artist's name
artistname = "Devin Deng"

# this is the artist's role (probably just 'Artist'
# but if you wanna change it up it's there to change)
artistrole = "Artist"

# this is the file you want to save the html code in
# (this time you have to include the .html extension)
filename = "thingy-art.html"

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
