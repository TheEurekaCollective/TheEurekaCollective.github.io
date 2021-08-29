// don't edit these
var lorenames = ["Factions", "Characters", "Items", "Subjects", "Locations", "History", "Stories", "All"];
// make sure these match exactly the entries in lorenames right above
var loretype = ['Items', 'Locations', 'Locations', 'Subjects'];
// This is the heading that shows up
var loreheadings = ["ANTIMATTER", "MATERNA", "MADAME MARTINS", "FASTER THAN LIGHT"];
// This is the description that shows up, trim it manually
// (the first description is abt as long as it goes, don't go much longer than that)
var loretxt = ["Antimatter is the primary form of energy storage within the Human Domain. It is used to power almost every form of technology from mages to starships. It is even used as a form of currency. The commodification of antimatter stems from...",
"In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus...",
"Humanity has long mastered the human body. Genetic modification and alteration are the norm. One can get a cell sculpt from the corner store. An entire field of fashion known as fleshcraft sprung from this newfound ability. It...",
"Within Project Anima, there have been many methods in which faster-than-light (FTL) is accomplished and utilized. This article is a compendium of all faster than light capable phenomena and applications. It can be noted that many of these systems... "];
// This is the address of the icon you want to add
var loreimg = ["resources/Antimatter Icon.svg", "resources/Materna Icon.svg", "resources/Madame Martins Icon.svg", "resources/Faster Than Light Icon.jpg"];
// This is the link to the corresponding specific page
// Notice that if the html file is 'lorespecific.html' the entry here is 'lorespecific'
var lorespecificlink = ['lorespecific', 'lorespecific', 'lorespecific', 'fasterthanlight-lore'];

function initloreboxes(indices, feed) {
	var j = 0;
	for (var y = 24.4; true; y += 34) {
		for (var x = 20; x < 81; x += 30) {
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
	var i = 0;
	for (var y = 24.4; true; y += 34) {
		for (var x = 20; x < 81; x += 30) {
			while (i<loreimg.length && c != 'All' && loretype[i] != c) {
				var div = document.getElementById("entry" + i)
				div.style.opacity='0';
				div.style.left='0';
				div.style.top='0';
				i += 1;
			}
			if (i >= loreimg.length) break;
			var div = document.getElementById("entry" + i);
			div.style.opacity='1';
			div.style.left = x + "vw";
			div.style.top = y + "vw";
			i += 1;
		}
		if (i >= loreimg.length) {
			document.getElementsByClassName("lorefeed")[0].style.height = (y+17.6)+'vw';
			break;
		}
	}
}
