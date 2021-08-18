var lorenames = ["Factions", "Characters", "Items", "Subjects", "Locations", "History", "Stories", "All"];
var loretype = ['Items', 'Locations', 'Locations'];
var loreheadings = ["ANTIMATTER", "MATERNA", "MADAME MARTINS"];
var loretxt = ["Antimatter is the primary form of energy storage within the Human Domain. It is used to power almost every form of technology from mages to starships. It is even used as a form of currency. The commodification of antimatter stems from...",
"In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus...",
"Humanity has long mastered the human body. Genetic modification and alteration are the norm. One can get a cell sculpt from the corner store. An entire field of fashion known as fleshcraft sprung from this newfound ability. It..."];
var loreimg = ["resources/Antimatter Icon.svg", "resources/Materna Icon.svg", "resources/Madame Martins Icon.svg"];

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
	var i = 0;
	for (var y = 18; true; y += 34) {
		for (var x = 20; x < 81; x += 30) {
			if (i >= loreheadings.length) break;
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
			node.href = "lorespecific.html?id=" + i;
			div.append(node);
			feed.append(div);
			i += 1;
		}
		if (i>=loreheadings.length) {
			feed.style.height = (y+24)+'vw';
			break;
		}
	}
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
	for (var y = 18; true; y += 34) {
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
			document.getElementsByClassName("lorefeed")[0].style.height = (y+24)+'vw';
			break;
		}
	}
}



var defaultinfo = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"];
var imgname = ["resources/Materna Icon.svg"];
var boxinfo = ["CATEGORY--Factions|Human Domain|Corporation|Human|Synthia Faber|September 1st, 2021"];
var article = [`===MATERNA
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
==SECTION TITLE
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
=Paragraph Title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`]



function initlorespecific() {
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	var id = parseInt(urlParams.get('id'));
	document.querySelectorAll("img.infoimg")[0].src=imgname[id];
	// alert(document.querySelectorAll("img.infoimg")[0].src);
	var info = boxinfo[id].split('|');
	for (var i = 0; i < 6; i++) {
		var a = "", b = "";
		var index = info[i].indexOf("--");
		if (index==-1) {
			a=defaultinfo[i];
			b=info[i];
		} else {
			a = info[i].substring(0, index);
			b = info[i].substring(index+2, info[i].length);
		}
		document.getElementById("boxh"+i).textContent = a;
		document.getElementById("boxi"+i).textContent = b;
	}
	var div = document.getElementsByClassName("specificall")[0];
	var text = article[id].split('\n');
	for (var i = 0; i < text.length; i++) {
		if (text[i].length >= 3 && text[i].substring(0, 3)=="===") {
			var node = document.createElement('p');
			node.className = "infoheading";
			node.textContent = text[i].substring(3, text[i].length);
			div.append(node);
			node = document.createElement('span');
			node.className = "underline";
			div.append(node);
		} else if (text[i].length >= 2 && text[i].substring(0, 2)=='==') {
			var node = document.createElement('p');
			node.className = "sectiontitle";
			node.textContent = text[i].substring(2, text[i].length);
			div.append(node);
			node = document.createElement('span');
			node.className = "underline";
			div.append(node);
		} else if (text[i].length >= 1 && text[i].substring(0, 1)=='=') {
			var node = document.createElement('p');
			node.className = "paragraphtitle";
			node.textContent = text[i].substring(1, text[i].length);
			div.append(node);
		} else {
			var node = document.createElement('p');
			node.className = "infoparagraph";
			node.textContent = text[i];
			div.append(node);
		}
	}
}
