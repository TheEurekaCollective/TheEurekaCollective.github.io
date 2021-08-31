// all the data in each page, make sure it's surrounded by backticks instead of quotes
// so that it can contain multiple lines, ex `this is a quote`
const pagedata = [`MATERNA
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`, `AETERNUM
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation ullamco laboris nulla pariatur. Duis nulla pariatur. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation fugiat quis nostrud exercitation ullamco nulla pariatur.`,
`FASTER THAN LIGHT
Within {Project Anima}, there have been many methods in which faster-than-light (FTL) is accomplished and utilized. This article is a compendium of all faster than light capable phenomena and applications. It can be noted that many of these systems could be used in tandem for different results.
WARP
Warp is the compression and expansion of space-time using a warp drive. With advanced gravitics and quantum manipulation, a bubble is generated in which the area in front of the vessel is compressed while the area behind the vessel is expanded to compensate. Warp speeds are affected by the size, shape, and efficiency of the warp field.
Warp Shielding
When a warp bubble is projected, spacetime in the area becomes skewed and becomes difficult for sensors to understand. This allows ships that host a warp drive to use the bubble as a form of shielding.
Warp Weaponry
Warp drives are extremely expensive. However, in rare instances, an explosive device can be fitted with a warp drive.
VOID
The Void is a higher-dimensional space that is composed purely of mana. One location in the Void can coincide with multiple locations in the Material Plane. This property allows for travel within the Void to be much faster than travel in the Material Plane, a practice known as voidjumping. The Void is theoretically infinite and is hostile to all forms of matter. As a result, travel into the Void requires using a reality stabilization field and a spatial auger. Spatial augers allow ships to tear through space-time and enter Void space while a reality stabilization field protects ships from the Void. Should a reality stabilization field fail, its contents would disappear completely. Travelers of the Void must also be wary of large gravitic influences that stem from the Material Plane, as gravity possesses the ability to penetrate space-time. Should a vessel intercept a large gravitational field, it might be pulled off its designated course. To address this, advanced computers calculate a voidjump solution before entering the Void.
Void Submersibles
Void Submersibles are ships designed to operate for long periods in the Void without reentering the Material Plane.
Void Carriers
Void Carriers are a type of spaceship that exhibits a very large reality stabilization field. This allows for ships without a void drive to hitch on for a ride within the reality stabilization field. This requires significant degrees of coordination as the ships have to move in unison and at the same speeds so as to not accidentally leave the field and enter the Void.
Void Tracking
Just as gravity from the Material Plane penetrates spacetime into the Void, gravitic signatures could be detected within the Void from the Material Plane.
Constructs
With the proper technology, constructs such as the Nexus and the Void Wyrms could be established within the Void.
Void Wormholes
While wormholes function within the Void, their calibration systems are skewed and thus have the possibility of inducing a paradox. Since a single location within the Void can represent multiple locations within the Material Plane, a wormhole passage can be split between multiple locations, and thus destroy whatever travels through.
Void Tactics
It is common for spaceships to rapidly enter and exit Void space to evade the enemy during ship-to-ship combat.
WORMHOLE
A bridge between two spaces in spacetime is known as a wormhole. Wormholes are one of the fastest methods of FTL but also the costliest due to the nature of wormhole energy consumption. While the size of a wormhole is expanded in a scalar fashion, the required energy input rises exponentially. It also takes a much larger amount of infrastructure compared to most other forms of FTL travel. Wormhole travel effectiveness drops over large distances due to an accumulation of Yunian Uncertainty. To address this issue, wormhole relay stations are utilized.
Wormhole System
A system of wormholes gates were established by the Pathfinders Legion for the Galactic Commonwealth. Nearly all major systems have access to one or more wormhole gates. These wormhole gates are relatively small and are open for short bursts at specific times. It is common to see fleets of spaceships arrayed in front of offline wormholes awaiting their opening. It is also common for ships to link their navigation systems with one another to maintain the best balance between speed and cohesion.
Wormhole Cooling
One of the main pitfalls for any spacefaring object is the amount of heat that needs to be released or decreased. One of the methods devised to help alleviate this issue was to use a wormhole as a cooling system. High-energy matter would be dumped through the wormhole into an off-site cooling facility. This method has also been used in the reverse, allowing for ships with wormholes to be supplied indefinitely. The stellar engines used by the Traders of the Wandering Sun utilize this technology extensively.
Quantum Wormholes
Small wormholes are generated and allow for superluminal communications, which can include photons and radiowaves.
ANIMA
Anima-based FTL can be divided into two categories. These are designated binary systems and singularity systems. A binary system requires the use of two hosts while a singularity system only needs one.
Binary Systems
Transpositioning
The Bygone Races had mastered the art of transpositioning, a method of FTL where an object is uploaded to the conceptual plane and placed via an anima in a different location. However, this requires a host to already be at the target location.
Ansible
Ansibles are utilized by organizations such as the Scribes Consortium to allow for FTL communications using an anima as a medium.
Singularity Systems: Singularity systems use anima to produce the FTL systems described above. Essentially, they empower a host to be able to enter the Void, generate wormholes, or warp space. `,
`Akanthe International Park, Akanthe, void ecology, migration, seeding, life, G-Type Star, Nujim system, Commonwealth Galactic Research Initiative, Theomachy, Galactic Assembly, autotrophs, gravitic well, bucket whales, telescopic eyes, raptors, methane rockets, derma, artificial atmospheres, mutation rates, organizations, Optil Kawau Hotels & Resorts, Akanthe Research Institute, Akanthe Park Service`,
`Human Domain, antimatter, currency, containment units (wells), Sol system, New Heliopolis, solar colonies, Dyson Project, Laser Energy Transport Grid, drones, laser energy, particle accelerators, hermetically sealed container, fuel source, mages, starships, mana-catalyzed antimatter reactors, paraphysical techniques, antimatter credit, weaponry, counterfeit`]
// heading that shows up, title of the lore page or name of the image
const pagetitle = ["MATERNA", "AETERNUM", "FASTER THAN LIGHT", "AKANTHE INTERNATIONAL PARK", "ANTIMATTER"];
// link to the specific page
// note that if the html file is 'artspecific.html' the link is 'artspecific'
const pagelink = ["lorespecific", "artspecific", "fasterthanlight-lore", 'akantheinternationalpark-lore', 'antimatter-lore'];
// 'lore' if it's lore, else 'art' if it's art
const type = ["lore", "art", "lore", "lore", 'lore'];
// index it shows up in lore.js or art.js, remember that it's 0-indexed
const indices = [1, 0, 3, 4, 0];
// ignore this stuff
var loreindices;
var artindices;

for (var i = 0; i < pagedata.length; i++) {
	pagedata[i] = pagedata[i].toLowerCase();
}

//shortens document.getElementById
function element(id) { return document.getElementById(id); }

function initresults() {
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	var search = urlParams.get("search");
	loreindices = [];
	artindices = [];
	if (search.length==0) {
		return;
	}
	var tosort = [];
	for (var i = 0; i < pagedata.length; i++) {
		tosort.push([score(i, search), i]);
	}
	tosort.sort(function(a, b) {return a[0]-b[0];});
	tosort.reverse();
	for (var i = 0; i < tosort.length; i++) {
		if (tosort[i][0]>0) {
			var x = tosort[i][1];
			if (type[x] == "lore") {
				loreindices.push(indices[x]);
			} else {
				artindices.push(indices[x]);
			}
		}
	}
}

function rflip(x) {
	var rmenu = document.querySelectorAll('a.rmenup');
	for (var i = 0; i < 2; i++) {
		if (i==x) rmenu[i].className='rmenup rmenuc';
		else rmenu[i].className='rmenup';
	}
	var displays = [['0', '-100%'], ['100%', '0']];
	element('resultlore').style.left=displays[0][x];
	element('resultgallery').style.left=displays[1][x];
	if (x==0) element('resultcontainer').style.height=element('resultlore').style.height;
	else element('resultcontainer').style.height=element('resultgallery').style.height;
}



function strcnt(a, b) {
	var r = a.indexOf(b);
	var c = 0;
	while (r != -1) {
		c++;
		r = a.indexOf(b, r + 1);
	}
	return c;
}

function score(p, s) {
	s = s.split(' ');
	var ans = 0;
	for (var i = 0; i < s.length; i++) {
		if (s[i].length==0) continue;
		ans += strcnt(pagetitle[p].toLowerCase(), s[i])*s[i].length*s[i].length*10;
		ans += strcnt(pagedata[p], s[i])*s[i].length*s[i].length;
	}
	return ans;
}

//gets each inputs data starting from second input
function getResults() {
	//gets value of input
	let search = document.querySelectorAll('input.menu')[0].value.toLowerCase();
	var tosort = [];
	allSearchData = ""; //clears data for each word typed

	element("search-results").style.display = "none";
	element("search-results").innerHTML = "";

	if (search.length==0) return;
	for (var i = 0; i < pagedata.length; i++) {
		tosort.push([score(i, search), i]);
	}
	tosort.sort(function(a, b) {return a[0]-b[0];});
	tosort.reverse();
	for (var i = 0; i < tosort.length && i < 10; i++) {
		if (tosort[i][0]>0) {
			var x = pagetitle[tosort[i][1]];
			if (x.length>17) x = x.slice(0, 17) + "...";
			element("search-results").innerHTML +=
				"<div class='search-item'><a class='search-item' href='"+pagelink[tosort[i][1]]+"'>" + x + "</a></div>";
		}
	}
	if (tosort[0][0]==0) {
		element("search-results").innerHTML = "<div class='search-item no-results'><a class='search-item no-results'>No Results</a></div>"
	}
	element("search-results").style.display = "block";
}
//gets results after each input
document.querySelectorAll('input.menu')[0].oninput = function() {
	getResults();
};
document.querySelectorAll('input.menu')[0].onblur = function() {
	window.addEventListener("click", function() {
		setTimeout(() => {element("search-results").style.display = "none";}, 10);
	}, {once : true});
};
document.querySelectorAll('input.menu')[0].onfocus = function() {
	getResults();
};
