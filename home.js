
var coords = [56, 112, 177, 245, 395, 10000];
var pos = ["10%", "26%", "42%", "58%", "74%", "90%"];
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
		var cmp = (coords[i]+1)*vw;
		if (i==4) cmp=258*vw+250*vh;
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
	if (i>0) offset = coords[i-1] * vw + 20;
	if (i==5) offset = 258*vw + 250*vh;
	offset = offset - getY();
	window.scrollBy(0, offset);
	update();
}

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
		for (var i = 0; i < spans.length; i++) {
			spans[i].style.boxShadow = "0 0 5px white";
			spans[i].style.backgroundColor = "#bbbbbb";
		}
		this.style.width= a + "vw";
		this.style.height= b + "vw";
		var lbl = this.getElementsByClassName("lorelbl");
		if (lbl.length>0) lbl[0].style.fontSize = (1.3*ratio)+"vw";
		lbl = this.getElementsByClassName("releasebody");
		if (lbl.length>0) lbl[0].style.fontSize = (1*ratio)+"vw";
		lbl = this.getElementsByClassName("releaseheading");
		if (lbl.length>0) lbl[0].style.fontSize = (1.4*ratio)+"vw";
	}
	div.onmouseout = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) {
			spans[i].style.boxShadow = "0 0 0px white";
			spans[i].style.backgroundColor = "#666666";
		}
		this.style.width= c + "vw";
		this.style.height= d + "vw";
		var lbl = this.getElementsByClassName("lorelbl");
		if (lbl.length>0) lbl[0].style.fontSize = "1.3vw";
		lbl = this.getElementsByClassName("releasebody");
		if (lbl.length>0) lbl[0].style.fontSize = "1vw";
		lbl = this.getElementsByClassName("releaseheading");
		if (lbl.length>0) lbl[0].style.fontSize = "1.4vw";
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
		addborder(div, 16, 22, 15, 21);
		var node;
		node = document.createElement("img");
		node.src = "resources/" + lorenames[i-1] + " Icon.svg";
		node.className = "loreimg";
		div.append(node);
		node = document.createElement("p");
		node.textContent = lorenames[i-1].toUpperCase();
		node.className = "lorelbl";
		div.append(node);
	}
}

var artpos = [[35, 65, 105], [5, 35, 65], [-35, 5, 35]];
var artop = [[1, 0.4, 0], [0.4, 1, 0.4], [0, 0.4, 1]];
var artcoords = [50, 140, 1000];
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

// alert(window.innerWidth / 100.0);
update();
setfeature();
setlore();
initart();
scrollart();
initsponsor();
