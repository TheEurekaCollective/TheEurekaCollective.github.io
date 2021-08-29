var log = `
==08/28/21
=General
{
Replaced logo in header
Fixed searchbar links
Created guide for adding new pages
}
=Universe
{
Finished developer log 
Fixed margins
}
==08/27/21
=General
{
Fixed header links
}
=Results
{
Edited lore and art javascript to make results page easier
Created results page javascript to generate results
Implemented submenu selection
Added no results found message
Added results heading
}
==08/26/21
=General
{
Hitting enter on search bar redirects to empty results page
}
=Universe
{
Added update timer
}
=About Us
{
Allowed arbitrarily many team members
}
==08/25/21
=Universe
{
Added developer log
}
==08/23/21
=General
{
Replaced social media links
}
=Lore
{
Changed how links are set
}
==08/20/21
=General
{
Added python and text files to generate future lore pages
Allowed searching with one letter only
}
==08/19/21
=General
{
Tweaked onblur timing to wait for next click
Added python and text files to generate future art pages
Resized most images
}
=Homepage
{
Altered new release ratios
Made it easier to edit contents of homepage
}
=Art (Specific)
{
Added and resized fullscreen icon
Resized image margins
Tested profile pictures
}
==08/18/21
=General
{
Added logos to footer
Resized header text
Added search engine
Added No Results message to search bar
Fixed onblur issue with search bar
}
=Homepage
{
Added and resized learn more button
Resized title text
Fixed lore icons clipping
Altered scroll parameters
Fixed choppy text transforms
Centered art carousel
}
=Art
{
Moved gallery labels to image center
Links cover entire image
Art labels go completely visible on hover
Fixed margins
}
=Art (Specific)
{
Dot moves when scrolling through text
}
=About Us
{
Resized Meet the Team profiles
}
=Privacy Policy
{
Added privacy policy
}
=Sitemap
{
Added sitemap
}
==08/17/21
=General
{
Created footer, added to each page
Set up google analytics
}
=Homepage
{
Tweaked new releases section
Edited scrollbar mechanics
Resized various elements
}
=Lore
{
Minor tweaks to submenus and filtering
Implemented clicking again to unfilter
}
=Art
{
Removed gallery title
}
==08/16/21
=Art (Specific)
{
Finished html outline
}
=Universe
{
Created overview, origin, and sandbox
}
=About Us
{
Created About and Meet the Team sections
Uploaded profile pictures
}
==08/15/21
=Art
{
Created art gallery
Played with fade-in effects
}
=Art (Specific)
{
Created art specific page
Added most features (missing bottom of right side)
}
==08/14/21
=Lore (Specific)
{
Aesthetic tweaks
Wrote javascript to generate html text
}
==08/13/21
=Homepage
{
Created fade-in effect on page load
Aesthetic tweaks
}
=Lore
{
Created lore feed
Created submenu selection
}
=Lore (Specific)
{
Set up lore page template
}
==08/12/21
=Homepage
{
Minor fixes
Proportions remain constant across variable screen sizes
}
==08/11/21
=Homepage
{
Boxes expand on hover in lore section
Art carousel names show up on hover
Created sponsor section
}
==08/09/21
=Homepage
{
Replaced temporary png's with svg's
Borders light up on hover in lore section
Started work on art carousel
}
==08/08/21
=Homepage
{
Created synopsis section
Created featured section
Created lore section
}
==08/06/21
=General
{
Implemented header
}
=Homepage
{
Added scrollbar
Created title screen
}
`

function initdevlog() {
	var div = document.querySelectorAll('div.devlog')[0];
	var html = "";
	var lines = log.split('\n');
	for (var i = 0; i < lines.length; i++) {
		if (lines[i].length==0) continue;
		else if (lines[i]=='{') html += '<ul>\n';
		else if (lines[i]=='}') html += '</ul>\n';
		else if (lines[i].length>=2 && lines[i].substring(0,2)=='==') {
			html += "<p class='devlogday'>"+lines[i].substring(2)+"</p>\n";
		} else if (lines[i].substring(0,1)=='=') {
			html += "<p class='devlogcategory'>"+lines[i].substring(1)+"</p>\n";
		} else html += '\t<li>'+lines[i]+'</li>\n';
	}
	console.log(html);
	div.innerHTML = html;
}

var now;
var until;
var timer;

function universescroll() {
	var div = document.querySelectorAll('div.devlog')[0];
	var totalheight = div.scrollHeight;
	var showheight = div.clientHeight;
	// var showheight = 35 * window.innerWidth / 100.0;
	if (totalheight <= showheight) return;
	var percent = div.scrollTop / (totalheight - showheight);
	document.getElementById('udot').style.top = (100.0 * percent) + '%';
}

var timeObject = {
    days: 0, hours: 0, minutes: 0, seconds: 0, total: 0
};

var elements = {
    days: undefined, hours: undefined, minutes: undefined, seconds: undefined
};

Number.prototype.pad = function (count) {
    var retval = String(this);
    while (retval.length < (count || 2)) { retval = "0" + retval; }
    return retval;
}

//shortens document.getElementById
function element(id) { return document.getElementById(id); }

function init() {
	initdevlog();
	until = new Date("2021-09-01T00:00:00");
	document.getElementById("soon").style.display = "none";
	document.getElementById("timer").style.display = "block";
	update();
	timer = setInterval(function () { update(); }, 1000);
}

function update() {

    now = new Date();
    timeObject.total = now - until;

    if (timeObject.total < 0) {
		document.getElementById("soon").style.display = "none";
		document.getElementById("timer").style.display = "block";
        timeObject.total = Math.abs(timeObject.total / 1000);

        timeObject.days = Math.floor(timeObject.total / 86400);
        timeObject.total -= timeObject.days * 86400;

        timeObject.hours = Math.floor(timeObject.total / 3600);
        timeObject.total -= timeObject.hours * 3600;

        timeObject.minutes = Math.floor(timeObject.total / 60);
        timeObject.total -= timeObject.minutes * 60;

        timeObject.seconds = Math.floor(timeObject.total);


        element('days').innerHTML = "<p class='updatenumber'>" + timeObject.days + "</p><p class='updatetype'>Day" + (timeObject.days === 1 ? '' : 's') + "</p>";
        element('hours').innerHTML = "<p class='updatenumber'>" + timeObject.hours.pad(2) + "</p><p class='updatetype'>Hour" + (timeObject.hours === 1 ? '' : 's') + "</p>";
        element('minutes').innerHTML = "<p class='updatenumber'>" + timeObject.minutes.pad(2) + "</p><p class='updatetype'>Minute" + (timeObject.minutes === 1 ? '' : 's') + "</p>";
        element('seconds').innerHTML = "<p class='updatenumber'>" + timeObject.seconds.pad(2) + "</p><p class='updatetype'>Second" + (timeObject.seconds === 1 ? '' : 's') + "</p>";

    } else {
        if (timer !== undefined) {
            clearInterval(timer);
        }

		document.getElementById("soon").style.display = "block";
		document.getElementById("timer").style.display = "none";
    }
}

window.onload = function () {
    init();
}
