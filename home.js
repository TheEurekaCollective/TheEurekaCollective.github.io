
var coords = [100, 200, 300, 400, 650, 10000];
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
		var cmp = (coords[i])*vh;
		if (y<=cmp) {
			b[i]=true;
			break;
		}
	}
	for (var i = 0; i < 6; i++) {
		var lab = document.getElementById("scroll" + (i+1));
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
	if (i>0) offset = coords[i-1] * vh + 1;
	offset = offset - getY();
	window.scrollBy(0, offset);
	update();
}

var pclasses = ["lorelbl", "releasebody", "releaseheading", "entryheading", "entrytxt"];
var psizes = [1.15, 1, 1.4, 1.3, 0.95];

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
		addborder(div, 36, 13, 35, 12);
	}
}

function setlore() {
	for (var i = 1; i <= 8; i++) {
		var div = document.getElementById("lore" + i);
		addborder(div, 14, 19, 13, 18);
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
var artcoords = [50, 100, 1000];
var artnames = ["MAGUS", "THE INFINITE CITY", "SCULPT"];
var artlinks = ['artspecific.html', 'artspecific.html', 'artspecific.html']

function initart() {
	document.getElementsByClassName("art")[0].style.height=(250*vh) + "px";
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("art" + i);
		var covernode = document.createElement('a');
		covernode.className = 'coverlink';
		covernode.href = artlinks[i-1];
		div.append(covernode);
		var node = document.createElement("a");
		node.className = "artlabel";
		node.href = artlinks[i];
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
			var a = this.querySelectorAll('a.artlabel')[0];
			if (a.mouseIsOver) return;
			a.style.opacity="0.4";
		}
		div.onmouseout = function() {
			var a = this.querySelectorAll('a.artlabel')[0];
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
		if (y <= 400*vh + artcoords[i]*vh) {
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
	setTimeout(() => {img.style.transition="1s ease";img.style.opacity='0.25';}, 0);
	var div = document.getElementsByClassName("header")[0];
	div.style.opacity="0";
	setTimeout(() => {div.style.transition="1s ease";div.style.opacity='0.9';}, 500);
	var scroll = document.getElementById("scroll");
	setTimeout(() => {scroll.style.transition="1s ease";scroll.style.opacity='1';}, 500);
	var head1 = document.getElementById("heading1");
	setTimeout(() => {head1.style.transition="0.8s ease";head1.style.opacity='1';}, 1000);
	var head2 = document.getElementById("heading2");
	setTimeout(() => {head2.style.transition="0.8s ease";head2.style.opacity='1';}, 1200);
	var learn = document.getElementById("learnmore");
	setTimeout(() => {
		learn.style.opacity='0.6';
		learn.onmouseover = function() {this.style.opacity='1'; this.style.fontWeight='400';};
		learn.onmouseout = function() {this.style.opacity='0.6'; this.style.fontWeight='200';}
	}, 1400);
	var a1 = document.getElementById("arrow1");
	setTimeout(() => {a1.style.animation='change 2s ease infinite';}, 1600);
	var a2 = document.getElementById("arrow2");
	setTimeout(() => {a2.style.animation='change 2s ease infinite';}, 1600);
}

var footertxt = `<p class="contactus" style="top:5vw">CONTACT US</p>
	<a href="mailto: theeurekacollective@gmail.com" class="email"> theeurekacollective@gmail.com </a>
	<p class="contactus" style="top:14vw">OR</p>
	<div class="contacticon">
		<a class="contacticon"><i class="fab fa-instagram contacticon" id="contact1"></i></a>
		<a class="contacticon"><i class="fab fa-facebook-f contacticon" id="contact2"></i></a>
		<a class="contacticon"><img alt="art" class="contacticon" id="contact3"></a>
		<a class="contacticon"><i class="fab fa-reddit-alien contacticon" id="contact4"></i></a>
		<a class="contacticon"><img alt="pat" class="contacticon" id="contact5"></a>
		<a class="contacticon"><img alt="buy" class="contacticon" id="contact6"></a>
		<a class="contacticon"><img alt="Kofi" class="contacticon" id="contact7"></a>
	</div>
	<div class="follow">
		<p class="footerheading">FOLLOW</p> <br>
		<a class="footerlink">Instagram</a><br><br>
		<a class="footerlink">Facebook</a><br><br>
		<a class="footerlink">Artstation</a><br><br>
		<a class="footerlink">Reddit</a>
	</div>
	<div class="support">
		<p class="footerheading">SUPPORT US</p> <br>
		<a class="footerlink">Patreon</a><br><br>
		<a class="footerlink">Buy Me a Coffee</a><br><br>
		<a class="footerlink">Ko-fi</a>
	</div>
	<div class="explore">
		<p class="footerheading">EXPLORE</p> <br>
		<a class="footerlink">Home</a><br><br>
		<a class="footerlink">Lore</a><br><br>
		<a class="footerlink">Art</a><br><br>
		<a class="footerlink">Universe</a><br><br>
		<a class="footerlink">About</a>
	</div>
	<div class="more">
		<p class="footerheading">MORE</p> <br>
		<a class="footerlink">Privacy Policy</a><br><br>
		<a class="footerlink">Sitemap</a>
	</div>
	<img src="resources/Eureka Integrated.svg" class="footereureka">
	<span class="footerline" style="left:0"></span>
	<span class="footerline" style="right:0"></span>
	<p class="copyright" style="top: 32vw">Unless otherwise stated, this work is licensed under a <a class="copyright" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.</a></p>
	<p class="copyright" style="top: 35vw">© 2021 Project Anima</p>`;

var footerlinks = ["https://www.instagram.com/theeurekacollective/", "https://www.facebook.com/The-Eureka-Collective-105419318305863", "https://www.artstation.com/theeurekacollective", "https://www.reddit.com/r/projectanima/", "https://www.patreon.com/theeurekacollective", "https://www.buymeacoffee.com/projectanima", "https://ko-fi.com/theeurekacollective", "index.html", "lore.html", "art.html", "universe.html", "aboutus.html", "privacypolicy.html", "sitemap.html"];
var iconsrcs = ['resources/ArtStation-logomark-white.png','resources/Digital-Patreon-Logo_White.png','resources/bmc-logo.svg','resources/Ko-fi_Icon_RGBforDarkBg.png'];

function initfooter() {
	document.getElementsByTagName('footer')[0].innerHTML = footertxt;
	var ftlinks = document.querySelectorAll('a.footerlink');
	for (var i = 0; i < ftlinks.length; i++) {
		ftlinks[i].href = footerlinks[i];
	}
	var cticons = document.querySelectorAll('img.contacticon');
	for (var i = 0; i < cticons.length; i++) {
		cticons[i].src = iconsrcs[i];
	}
	cticons = document.querySelectorAll('a.contacticon');
	for (var i = 0; i < cticons.length; i++) {
		cticons[i].href = footerlinks[i];
	}
}

initfooter();
