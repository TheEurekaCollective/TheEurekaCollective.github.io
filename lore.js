// don't edit these
var lorenames = ["Factions", "Characters", "Items", "Subjects", "Locations", "History", "Stories", "All"];
// make sure these match exactly the entries in lorenames right above
var loretype = ['Items', 'Factions', 'Factions',
'Subjects', 'Locations', 'History',
'Factions', 'Items', 'Characters',
'Subjects', 'Factions', 'Factions',
'Subjects', 'History', 'Factions',
'Locations', 'Stories', 'Factions',
'Stories', 'Factions', 'Factions',
'Characters', 'Subjects', 'Locations',
'Locations', 'Stories', 'Factions',
'Locations', 'Characters', 'Factions',
'Factions', 'Subjects', 'Factions',
'Factions', 'History', 'Items',
'Factions'];
// This is the heading that shows up
var loreheadings = ["ANTIMATTER", "MATERNA", "MADAME MARTINS",
"FASTER THAN LIGHT", "AKANTHE INTERNATIONAL PARK", "ARGENTIMARIA ATTACK",
"CASPIA INTERACTIVE", "CHASSIS", "COMBAT MAGES",
"COSMOLOGY", "EGO", "GALACTIC COMMONWEALTH",
"HUMAN SPELLS", "HUMAN THAUMATOLOGY", "IKOLAE",
"INTERNATIONAL SPACE ELEVATOR", "OPERATION HELIOS", "KALATARI",
"KALATARI ORIGIN", "KARANAAN", "KOIOS INSTITUTE",
"MAGUS", "METAPHYSICS", "MILKY WAY GALAXY",
"NEXUS", "SAGA", "SHARHASTIANS",
"SILVER TOWER", "SLIME MOLD", "TALAPHRIAN ORDER",
"MITHRAEHO", "PARAPHYSICS", "PARAPHYSICS DIVISION",
"SCRIBES CONSORTIUM", "SILENT ELDER", "SPELL RIFLES",
"TENDRIL"];
// This is the description that shows up, trim it manually
// (the first description is abt as long as it goes, don't go much longer than that)
var loretxt = ["Within the Human Domain, antimatter is the primary form of energy production and storage. From cities to starships, antimatter powers almost every aspect of life. It is even used as a currency and is stored in special containment units...",
"Materna is one of the largest companies in the biotechnology sector and focuses on providing services such as cloning, prenatal modification, and artificial births. They are a subsidiary of Faber Technologies and have existed since the...",
"The invention of postnatal genetic modification and cellular sculpting bestowed upon humans the ability to modify their bodies as they see fit. This newfound ability was initially used for medical procedures but developed into...",
"Within Project Anima, there have been many methods in which faster-than-light (FTL) is accomplished and utilized. This article is a compendium of all faster than light capable phenomena and applications. It can be noted... ",
"Akanthe International Park is a series of scientific missions and resorts located within Akanthe and its ring system. This area is designated a Park due to it being one of the few occurrences of void ecology within the Milky Way Galaxy...",
"The Argentimaria Attack was a BCI-based psychotechnical terrorist attack that took place in the lunar city of Argentimaria. On the seventh of November, 2133, a fanatical anti-BCI group known as Ad Antea penetrated the servers of...",
"Caspia Interactive is the main proprietor of video games within the Human Domain. Their most popular product is the Dreamscape, a virtual reality game built on the revolutionary Noosphere engine...",
"A combat mage’s chassis is its body and its method of interaction with the environment. The chassis is a biomechanical frame that is composed of the most advanced materials produced by the Paraphysics Division...",
"Thousands of years of warfare and the discovery of paraphysics culminated in humanity’s ultimate soldier: the combat mage. Of all the mages within the Human Domain, nearly 60 percent are classified as combat mages...",
"Within the Outside, there resides a being. It is known by many names, but its most prominent is It Who Sleeps, otherwise referred to as the Dreamer. It is a being that undergoes the same repeated cycle of slumber and wakefulness...",
"Souls can arise from a variety of patterns and phenomena. Whether they be the electrical interactions between neurons or the optical processing fluctuations of an AI, the physical mainframe is the critical factor needed to sustain...",
"The Galactic Commonwealth, otherwise known as the Commonwealth, is a collection of loosely associated nations and species. It is the dominant organization within the Milky Way, composed of hundreds of member states and being on...",
"Spells are the foundation of thaumaturgy, serving as which thaumaturgical phenomena are generated. They are energy-information packages composed of psions and mana, cast from devices known as emitters...",
"Ever since humankind's inception, the arcane arts have shifted and twisted the tides of history. From the magus cabals and alchemists of yore to the construct mages and thaumatologists of the modern day, thaumaturgy has played...",
"The creation of custodian races and constructs to maintain structures and systems was not uncommon amongst the Elder Races. However, one of the few that have survived the War of Dreams and achieved sophonthood are the...",
"The first Carbon Spire, otherwise known as the International Space Elevator (ISE), is humankind's first megastructure. It is one of the centerpieces of human civilization, ferrying people and goods non-stop between its base...",
"Mission Log Start\nTerran Time: 22:30\nTerran Date: 24-11-2570\nSubject: Candidate Extraction\nCodename: Operation Helios...",
"The Kalatari are a race of animium-based life evolved from the sophont reptilian Skago, who in turn evolved from the non-sophont Skaga. Their entire civilization hinges on a caste system controlled by the clans of Revelators...",
"The world of Kalathron revolved around a cruel sun. Great waves of plasma would sweep across the planet, cursing those it came in contact with. However, life found a way to survive, not on the surface, but within deep caverns...",
"The Karanaan, otherwise known as the Traders of the Wandering Sun, are a collective of organizations dedicated to building wealth both in and out of the galaxy. Led by Lord-Merchant Olande, the Karanaan hold sway over the large...",
"The Koios Institute is a collection of loosely related organizations within the Terran Union. They are responsible for the exploration and investigation of various phenomena within the universe, including astrogeology and biology...",
"The mages of the 26th century are no longer the robe-wearing, stave-brandishing wizards of yore. They are produced by the Terran Union’s Paraphysics Division to be engines of war, pilots of starships, and administrators of civilizations...",
"Metaphysics is a term used to describe the phenomena that occurs within the Conceptual Plane. Metaphysics and the Conceptual Plane operate on completely different laws compared to the Material Plane, meaning it is beyond true...",
"The Milky Way Galaxy, otherwise known as the Milky Way, is a 13.6 billion-year-old galaxy that is approximately 105,700 light-years in diameter and has a height of more than a thousand light-years. It contains several hundred billion...",
"The Nexus is a complex series of transportation systems residing within the Void. While it is unknown as to who constructed it, it is theorized to be from before the Theomachy. This system is special from the jump and Void highway...",
"“I was imprisoned for a crime I had already forgotten millennia ago. Eons passed in my restless sleep, a sliver of the eternity that was my sentence. The perpetual internment had driven me mad, but in that madness, there was a...",
"The Sharhastians are an airborne race of hexapods originally hailing from the gas giant Sharhast. They are a hive race headed by sophont queens, who have formed the current unifying government of the Sharhastians, known as the...",
"Near the edge of the Perseus Arm, within the City of Three Peoples, lies a statement of Kalatari faith: an ark-turned-temple. It holds the Wellspring, the Luminous Falls, but most importantly, it holds the Kalatar’s Body...",
"Slime mold is an umbrella term used to describe various single-celled protists that can coalesce to form complex structures. While originally used in tasks such as neural network simulations and civil engineering, they are...",
"The Talaphrian Order of Knights, otherwise known as the Knights Talaphria, are a warrior cabal originating from the planet Vitar. They are led by Eyon and possess incredible reality-bending powers. They are frequently...",
"The Mithraeho are a sophont race of heptapods originating from the nearly tidally locked planet of Dakhara. They are one of the primary Newborn Races of the Galactic Commonwealth with their current government being the...",
"Paraphysics is an umbrella term used to refer to conceptual-material (metaphysical-physical) interactions. It can be divided into three fields: thaumaturgy, theurgy, and onturgy. Each one of these fields utilizes paraphysics...",
"The Paraphysics Division (PD) is a research organization dedicated to studying and utilizing paraphysical forces. While mostly shrouded in mystery to the common person, the technologies and techniques that have been developed...",
"Scribes Consortium is a galaxy-spanning megaconglomerate composed of the majority of anima-based organizations within the Galactic Commonwealth. From host-based data encryption to paraphysical substance production...",
"In the gaps between galaxies, in a cold realm known as the Outlands, there resides engines that were constructed to bear their sleeping creators to the time when the stars have grown dim and the universe has grown...",
"Spell rifles are the primary form of armament used by combat mages. They are military-grade wands dedicated to aiding a mage in focusing their spells and delivering them over long distances towards targets. They allow...",
"The Tendril are a species of sophont gigafauna that are theorized to be terraforming engines created by an unknown race. They possess the capability to modify their own genome and generate subspecies as needed. A tribal..."];
// This is the address of the icon you want to add
var loreimg = ["resources/Antimatter Icon.svg", "resources/Materna Icon.svg", "resources/Madame Martins Icon.svg",
"resources/Faster Than Light Icon.svg", "resources/Akanthe International Park Icon.svg", "resources/Argentimaria Attack Icon.svg",
"resources/Caspia Interactive Icon.svg", "resources/Chassis Icon.svg", "resources/Combat Mages Icon.svg",
"resources/Cosmology Icon.svg", "resources/Ego Icon.svg", "resources/Galactic Commonwealth Icon.svg",
"resources/Human Spells Icon.svg", "resources/Human Thaumatology Icon.svg", "resources/Ikolae Icon.svg",
"resources/International Space Elevator Icon.svg", "resources/Operation Helios Icon.svg", "resources/Kalatari Icon.svg",
"resources/Kalatari Origin Icon.svg", "resources/Karanaan Icon.svg", "resources/Koios Institute Icon.svg",
"resources/Magus Icon.svg", "resources/Metaphysics Icon.svg", "resources/Milky Way Galaxy Icon.svg",
"resources/Nexus Icon.svg", "resources/Saga Icon.svg", "resources/Sharhastians Icon.svg",
"resources/Silver Tower Icon.svg", "resources/Slime Mold Icon.svg", "resources/Talaphrian Order Icon.svg",
"resources/Mithraeho Icon.svg", "resources/Paraphysics Icon.svg", "resources/Paraphysics Division Icon.svg",
"resources/Scribes Consortium Icon.svg", "resources/Silent Elder Icon.svg", "resources/Spell Rifles Icon.svg",
"resources/Tendril Icon.svg"];
// This is the link to the corresponding specific page
// Notice that if the html file is 'lorespecific.html' the entry here is 'lorespecific'
var lorespecificlink = ['antimatter-lore', 'materna-lore', 'madamemartins-lore',
'fasterthanlight-lore', 'akantheinternationalpark-lore', 'argentimariaattack-lore',
'caspiainteractive-lore', 'chassis-lore', 'combatmages-lore',
'cosmology-lore', 'ego-lore', 'galacticcommonwealth-lore',
'humanspells-lore', 'humanthaumatology-lore', 'ikolae-lore',
'internationalspaceelevator-lore', 'operationhelios-lore', 'kalatari-lore',
'kalatariorigin-lore', 'karanaan-lore', 'koiosinstitute-lore',
'magus-lore', 'metaphysics-lore', 'milkywaygalaxy-lore',
'nexus-lore', 'saga-lore', 'sharhastians-lore',
'silvertower-lore', 'slimemold-lore', 'talaphrianorder-lore',
'mithraeho-lore', 'paraphysics-lore', 'paraphysicsdivision-lore',
'scribesconsortium-lore', 'silentelder-lore', 'spellrifles-lore',
'tendril-lore'];

function initloreboxes(indices, feed) {
	var j = 0;
	for (var y = 24.4; true; y += 34) {
		var nxt = Math.min(indices.length-j, 3)-1;
		for (var x = 50-15*nxt; x < 51+15*nxt; x += 30) {
			if (j >= indices.length) break;
			var i = indices[j];
			var div = document.createElement("div");
			div.className = "loreentry";
			div.number = i;
			div.id = "entry" + i;
			div.style.left = x + "vw";
			div.style.top = y + "vw";
			var node = document.createElement("img");
			node.src = loreimg[i];
			node.className = "entryimg";
			div.append(node);
			node = document.createElement("p");
			node.className = "entryheading";
			node.textContent = loreheadings[i];
			div.append(node);
			node = document.createElement("p");
			node.className = "entrytxt";
			node.textContent = loretxt[i];
			div.append(node);
			node = document.createElement("span");
			node.className = "entryfade";
			div.append(node);
			node = document.createElement('a');
			node.className = "entrylink";
			node.href = lorespecificlink[i];
			div.append(node);
			feed.append(div);
			j += 1;
		}
		if (j>=indices.length) {
			feed.style.height = (y+17.6)+'vw';
			break;
		}
	}
}

function initlorepage() {
	var submenu = document.querySelectorAll("a.submenup");
	for (var i = 0; i < submenu.length; i++) {
		submenu[i].category = [lorenames[i], "All"];
		submenu[i].index = 0;
		submenu[i].onclick = function() {
			filter(this.category[this.index]);
		}
	}
	var feed = document.getElementsByClassName("lorefeed")[0];
	var indices = [];
	for (var i = 0; i < loreheadings.length; i++) indices.push(i);
	initloreboxes(indices, feed);
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	if (urlParams.has("filter")) {
		var c = urlParams.get('filter');
		filter(c);
	}
}

function filter(c) {
	var submenus = document.querySelectorAll('a.submenup');
	for (var i = 0; i < submenus.length; i++) {
		if (submenus[i].category[0] == c) {
			submenus[i].className = 'submenup submenuc';
			submenus[i].index=1;
		}
		else {
			submenus[i].className = 'submenup';
			submenus[i].index=0;
		}
	}
	var indices = [];
	for (var i = 0; i < loreimg.length; i++) {
		var div = document.getElementById("entry" + i);
		if (c != 'All' && loretype[i] != c) {
			div.style.opacity='0';
			div.style.left='0';
			div.style.top='0';
		} else {
			indices.push(i);
			div.style.opacity='1';
		}
	}
	var i = 0;
	for (var y = 24.4; true; y += 34) {
		var nxt = Math.min(indices.length-i, 3)-1;
		for (var x = 50-15*nxt; x < 51+15*nxt && i<indices.length; x += 30) {
			var div = document.getElementById("entry" + indices[i]);
			div.style.left = x + "vw";
			div.style.top = y + "vw";
			i += 1;
		}
		if (i >= indices.length) {
			document.getElementsByClassName("lorefeed")[0].style.height = (y+17.6)+'vw';
			break;
		}
	}
}
