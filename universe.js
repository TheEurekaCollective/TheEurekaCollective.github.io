var log = `
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
=Homepage
{
Implemented header
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
