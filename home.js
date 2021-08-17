
var coords = [56, 112, 177, 245, 395, 10000];
var pos = ['0%', '20%', '40%', '60%', '80%', '100%'];
var ids = ["scroll1", "scroll2", "scroll3", "scroll4", "scroll5", "scroll6"];
var vh = window.innerHeight / 100.0;
var vw = window.innerWidth / 100.0;
var lorenames = ["Factions", "Characters", "Items", "Subjects", "Locations", "History", "Stories", "All"];
var spanclasses = ["h c1", "v c1", "h c2", "v c2", "h c3", "v c3", "h c4", "v c4"];

function getY(){
  var top  = window.pageYOffset || document.documentElement.scrollTop;
  return top;
}

function updateSize() {
	vh = window.innerHeight / 100.0;
	vw = window.innerWidth / 100.0;
}

function update(){
	updateSize();
	var y = getY();
	var p = document.getElementById("scrolldot");
	var b = [false,false,false,false,false,false];
	for (var i = 0; i < 6; i++) {
		var cmp = (coords[i])*vw;
		if (i==4) cmp=258*vw+270*vh;
		if (y<=cmp) {
			b[i]=true;
			break;
		}
	}
	for (var i = 0; i < 6; i++) {
		var lab = document.getElementById(ids[i]);
		if (b[i]) {
			p.style.top=pos[i];
			lab.style.fontWeight="700";
		} else {
			lab.style.fontWeight="200";
		}
	}
}

function move(i) {
	var offset = 0;
	if (i>0) offset = coords[i-1] * vw + 10;
	if (i==5) offset = 258*vw + 270*vh + 10;
	offset = offset - getY();
	window.scrollBy(0, offset);
	update();
}

var pclasses = ["lorelbl", "releasebody", "releaseheading", "entryheading", "entrytxt"];
var psizes = [1.2, 1, 1.4, 1.3, 0.95];

function addborder(div, a, b, c, d) {
	var node;
	var ratio = a/c;
	for (var j = 0; j < 8; j++) {
		node = document.createElement("span");
		node.className = spanclasses[j];
		div.append(node);
	}
	div.onmouseover = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) if (spans[i].className != "entryfade") {
			spans[i].style.boxShadow = "0 0 5px white";
			spans[i].style.backgroundColor = "#bbbbbb";
		}
		this.style.width= a + "vw";
		this.style.height= b + "vw";
		var lbl = this.getElementsByTagName("p");
		for (var i = 0; i < lbl.length; i++)
			for (var j = 0; j < psizes.length; j++)
				if (lbl[i].className==pclasses[j])
					lbl[i].style.fontSize = (psizes[j]*ratio).toPrecision(15)+"vw";
	}
	div.onmouseout = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) if (spans[i].className != "entryfade") {
			spans[i].style.boxShadow = "0 0 0px white";
			spans[i].style.backgroundColor = "#777777";
		}
		this.style.width= c + "vw";
		this.style.height= d + "vw";
		var lbl = this.getElementsByTagName("p");
		for (var i = 0; i < lbl.length; i++)
			for (var j = 0; j < psizes.length; j++)
				if (lbl[i].className==pclasses[j])
					lbl[i].style.fontSize = (psizes[j])+"vw";
	}
}

function plainborder(div) {
	var node;
	for (var j = 0; j < 8; j++) {
		node = document.createElement("span");
		node.className = spanclasses[j];
		div.append(node);
	}
}

function setfeature() {
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("release" + i);
		addborder(div, 36, 14, 35, 13);
	}
}

function setlore() {
	for (var i = 1; i <= 8; i++) {
		var div = document.getElementById("lore" + i);
		addborder(div, 15, 21, 14, 20);
		var node;
		node = document.createElement("img");
		node.src = "resources/" + lorenames[i-1] + " Icon.svg";
		node.className = "loreimg";
		div.append(node);
		node = document.createElement("p");
		node.textContent = lorenames[i-1].toUpperCase();
		node.className = "lorelbl";
		div.append(node);
		node = document.createElement('a');
		node.href = 'lore.html?filter=' + lorenames[i-1];
		node.className = 'coverlink';
		div.append(node);
	}
}

var artpos = [[35, 65, 105], [5, 35, 65], [-35, 5, 35]];
var artop = [[1, 0.4, 0], [0.4, 1, 0.4], [0, 0.4, 1]];
var artcoords = [50, 120, 1000];
var artnames = ["MAGUS", "THE INFINITE CITY", "CHUNGUS"];

function initart() {
	document.getElementsByClassName("art")[0].style.height=(13*vw + 270*vh) + "px";
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("art" + i);
		var node = document.createElement("a");
		node.className = "artlabel";
		node.textContent = artnames[i-1];
		node.style.opacity = "0";
		node.mouseIsOver=false;
		node.onmouseover = function() {
			this.style.opacity = "1";
			this.mouseIsOver=true;
		}
		node.onmouseout = function() {
			this.style.opacity = "0.4";
			this.mouseIsOver=false;
		}
		div.append(node);
		div.onmouseover = function() {
			var a = this.getElementsByTagName("a")[0];
			if (a.mouseIsOver) return;
			a.style.opacity="0.4";
		}
		div.onmouseout = function() {
			var a = this.getElementsByTagName('a')[0];
			a.style.opacity="0";
		}
	}
}

function updart(k) {
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("art" + i);
		div.style.left = "" + artpos[k][i-1] + "vw";
		div.style.opacity = "" + artop[k][i-1];
		var lbl = div.getElementsByClassName("artlabel")[0];
		if (artpos[k][i-1]==35) {
			lbl.style.display="initial";
		} else {
			lbl.style.display="none";
			lbl.mouseIsOver=false;
		}
	}
}

function scrollart() {
	var y = getY();
	for (var i = 0; i < 3; i++) {
		if (y <= 258*vw + artcoords[i]*vh) {
			updart(i);
			break;
		}
	}
}

function initsponsor() {
	var txt = "<p class='sponsorname' style='left: (LEFT)vw; top: (TOP)vw;' data-aos='fade-up' data-aos-delay='(DELAY)' data-aos-offset='0'>CONTENT</p>"
	var div = document.getElementsByClassName("sponsor")[0];
	var node;
	for (var h = 13; h < 40; h += 5) {
		for (var l = 15; l < 90; l += 15) {
			var delay = Math.round((h+l)/10.0)*50;
			var cpy = txt;
			cpy = cpy.replace("(LEFT)", l.toString());
			cpy = cpy.replace("(TOP)", h.toString());
			cpy = cpy.replace("(DELAY)", delay.toString());
			cpy = cpy.replace("CONTENT", "Synthia Faber");
			div.innerHTML = div.innerHTML + cpy;
		}
	}
}

function fade() {
	var img = document.getElementById("topimg");
	setTimeout(() => {img.style.transition="1s ease";img.style.opacity='0.4';}, 0);
	var div = document.getElementsByClassName("header")[0];
	div.style.opacity="0";
	setTimeout(() => {div.style.transition="1s ease";div.style.opacity='0.9';}, 500);
	var scroll = document.getElementById("scroll");
	setTimeout(() => {scroll.style.transition="1s ease";scroll.style.opacity='1';}, 500);
	var head1 = document.getElementById("heading1");
	setTimeout(() => {head1.style.transition="0.8s ease";head1.style.opacity='1';}, 1000);
	var head2 = document.getElementById("heading2");
	setTimeout(() => {head2.style.transition="0.8s ease";head2.style.opacity='1';}, 1200);
}

var loretype = ['Items', 'Locations', 'Locations'];
var loreheadings = ["ANTIMATTER", "MATERNA", "MADAME MARTINS"];
var loretxt = ["Antimatter is the primary form of energy storage within the Human Domain. It is used to power almost every form of technology from mages to starships. It is even used as a form of currency. The commodification of antimatter stems from...",
"In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus...",
"Humanity has long mastered the human body. Genetic modification and alteration are the norm. One can get a cell sculpt from the corner store. An entire field of fashion known as fleshcraft sprung from this newfound ability. It..."];
var loreimg = ["resources/Antimatter Icon.svg", "resources/Materna Icon.svg", "resources/Madame Martins Icon.svg"];

function initlorepage() {
	var submenu = document.querySelectorAll("a.submenup");
	for (var i = 0; i < submenu.length; i++) {
		submenu[i].category = lorenames[i];
		submenu[i].onclick = function() {
			filter(this.category);
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
			addborder(div, 26, 31, 25, 30);
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
	// alert(c);
	var submenus = document.querySelectorAll('a.submenup');
	for (var i = 0; i < submenus.length; i++) {
		if (submenus[i].category == c) submenus[i].className = 'submenup submenuc';
		else submenus[i].className = 'submenup';
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
