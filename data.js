// all the data in each page, make sure it's surrounded by backticks instead of quotes
// so that it can contain multiple lines, ex `this is a quote`
const pagedata = [`MATERNA
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`,
`AETERNUM
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation ullamco laboris nulla pariatur. Duis nulla pariatur. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation fugiat quis nostrud exercitation ullamco nulla pariatur.`,
`FASTER THAN LIGHT
Within Project Anima, there have been many methods in which faster-than-light (FTL) is accomplished and utilized. This article is a compendium of all faster than light capable phenomena and applications. It can be noted that many of these systems could be used in tandem for different results.`,
`Akanthe International Park, Akanthe, void ecology, migration, seeding, life, G-Type Star, Nujim system, Commonwealth Galactic Research Initiative, Theomachy, Galactic Assembly, autotrophs, gravitic well, bucket whales, telescopic eyes, raptors, methane rockets, derma, artificial atmospheres, mutation rates, organizations, Optil Kawau Hotels & Resorts, Akanthe Research Institute, Akanthe Park Service`,
`Human Domain, antimatter, currency, containment units (wells), Sol system, New Heliopolis, solar colonies, Dyson Project, Laser Energy Transport Grid, drones, laser energy, particle accelerators, hermetically sealed container, fuel source, mages, starships, mana-catalyzed antimatter reactors, paraphysical techniques, antimatter credit, weaponry, counterfeit`,
`​​​​Argentimaria Attack, BCI-based psychotechnical terrorist attack, lunar city, Argentimaria, seventh of November, anti-BCI group, Ad Antea, Neurogenesis, BCI firm, neurovirus attack, backdoor, guardian AI, data traffic, malignant information, trojan virus, nervous system, motor control, live capture footage, rogue craft, atmospheric dome, analyst AI, Terran Union, Foxhound, anti-terrorism division, Terran military, trial and punishment, Eris, Sol System, thaumaturgists, orbital facilities, chronoprison, Union government, Human Domain`,
`Caspia Interactive (CI), video games, Human Domain, Dreamscape, virtual reality, Noosphere engine, Vulkan Games, Caspia (artificial island), Caspian Sea, troposcraper, enigmatic council, Rasui Mimoza, Satellites, Superluminal Information Relays, Tolkienesque fantasy, discopunk, brain-computer interface (BCI), Heimdall application, NPC, neural imprint, Temporal Manipulation, Sleep Play, Great Server Merge of 2499, the Union, Oneironauts, simulation-type worlds, memory blockers, Morpheus, Terra`,
`combat mage, chassis, biomechanical , Paraphysics Division, Research and Technology Sector, Bases, Central Cognition Cores (CCC), General Utility Combat Chassis (GUCC), Soft Systems, Hard Systems, Nanolaminate Plating, Superstructure, Artificial Muscles, liquid-metal matrix, Somatic Threads, mana, psions, Modular Armature System (MAS), Nanite Nodes, nanites, nanopod // nanite pod, Movement Systems, Digitigrade Legs, Power Limbs, Jointed Limbs, Non-Jointed Limbs, Manipular Limbs, artificial cilia, Flight Packages, Njordian Flight Unit, repulsor-type thrusters, Utility Slots, Utility Modules, Central Cognition Core (CCC), mage, Anchor, Computation Module, Sensor and Communications Suite (SCS), mage-to-ship communications,sensory capabilities, magnetoreception, thermography, object bypass vision (OBV) , electroreception, psioreception, drones, mothership, Mana-Catalyzed Micro Antimatter Reactor (MCMAR), wand, hydrogen-antihydrogen reactions, fine manipulation, Auxiliary Life Support (ALS)`,
`warfare, paraphysics, ultimate soldier, combat mage, mages, Human Domain, Project Nephilim, Experimental Weapons Department, mech suits, Hard Body Infantry units, House Faber, deep archives, Paraphysics Division, Mage Program, Department of War, Mana Production Potential (MPP), Magus Sector, Drone Combat, Aerial strike drones, breaching drones, chained-wand drones, Armament, Spell Rifles, spells, Sidearm, laser pistol, reactor energy, somatic, Melee, Redundant Oscillating Photoblade, vibrating blade, plasma emitter, plasma cutting, sharpening sheath, Sub-Wand, wand, paraphysical machinery, Hand-to-Hand, thaumaturgical, artificial, muscles, mothership, drone complement, orbital strike, Electronics and Sensors, Viruses, Defense, onion model of defense, flight packages, sensor scramblers, electronic warfare systems, decoy drones, dummy drones, shield drones, kinetic weaponry, plasma weaponry, active camouflage systems,Null Psionic Fields,Psionic Fields,psionic interference system,psionic deadlock,Energy Shielding, Nanolaminate Plating, Reinforcement Spells, chassis, Nanite Protocols, nanites, CCC, redundant life support system, mobility package, Reconnaissance, sensor packages, Communications, mentally communication, cognition stack, mage-to-drone communication, Logistics, mule drones, ordnance packages, Gear, biomechanical, Research and Technology Sector, space superiority, faster-than-light weaponry, drone and android warfare, paraphysical elements, breaching pods, personnel launch tubes, Swarm Mages, Stealth Mages, sensor duping technology, Juggernaut Mages, Scout Mages, Seeker Mages, repulsors, arachnid-type Njordian flight pack, Sniping Mages, Zero-G Mages`,
`the Outside, It Who Sleeps (the Dreamer), Existences, Material Plane, Conceptual Plane, Void, universe, dimensions, micro-universes, the Abyss, metaphysics, souls, anima, conjecture, apotheons, mana, mass shadows, faster-than-light (FTL), voidjumping`,
`souls, liturgy, Ego, Ixus, Theomachy, Zaehaldyn (the Mortal Instrument), Eyon, Aunox, True Form, metaphysics, Apotheon, Perfect Shapes, Abyss, Voidslash, Slab of Time, Sisyphean Scribe, Vagabond Artificers`]
// heading that shows up, title of the lore page or name of the image
const pagetitle = ["MATERNA", "AETERNUM", "FASTER THAN LIGHT", "AKANTHE INTERNATIONAL PARK", "ANTIMATTER", "ARGENTIMARIA ATTACK", "CASPIA INTERACTIVE", "CHASSIS", "COMBAT MAGES", "COSMOLOGY", "EGO"];
// link to the specific page
// note that if the html file is 'artspecific.html' the link is 'artspecific'
const pagelink = ["lorespecific", "artspecific", "fasterthanlight-lore", 'akantheinternationalpark-lore', 'antimatter-lore', 'argentimariaattack-lore', 'caspiainteractive-lore', 'chassis-lore', 'combatmages-lore', 'cosmology-lore', 'ego-lore'];
// 'lore' if it's lore, else 'art' if it's art
const type = ["lore", "art", "lore", "lore", 'lore', 'lore', 'lore', 'lore', 'lore', 'lore', 'lore'];
// index it shows up in lore.js or art.js, remember that it's 0-indexed
const indices = [1, 0, 3, 4, 0, 5, 6, 7, 8, 9, 10];
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
