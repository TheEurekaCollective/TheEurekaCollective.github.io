
var featuredimgname = 'MAGUS';
var featuredimglink = 'artspecific';
var featuredimgsource = 'resources/Magus.png';


var featuredtitles = ['MATERNA', 'MATERNA', 'MATERNA'];
var featurediconsources = ['resources/Materna Icon.svg', 'resources/Materna Icon.svg', 'resources/Materna Icon.svg'];
var featuredlinks = ['lorespecific', 'lorespecific', 'lorespecific'];
var featureddescriptions = ["In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus...",
"In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus...",
"In the Great Cities, it is not uncommon for an aspiring couple to walk into a Materna clinic and request a BioTube reservation. For what you may ask? For a baby! In the 26th century, nearly 93% of all births take place within an artificial uterus..."];


var artnames = ["MAGUS", "THE INFINITE CITY", "SCULPT"];
var artimgsources = ["resources/Magus.png", "resources/Infinite City.jpg", "resources/Morph Small.jpg"];
var artlinks = ['artspecific', 'artspecific', 'artspecific'];


var sponsors = [];



var coords = [99, 193, 295, 399, 649, 10000];
var pos = ['0%', '20%', '40%', '60%', '80%', '100%'];
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

function addborder(div, a, c) {
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
		this.style.transform = 'translate(-50%, -50%) scale(' + (a/c).toPrecision(15) + ')';
	}
	div.onmouseout = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) if (spans[i].className != "entryfade") {
			spans[i].style.boxShadow = "0 0 0px white";
			spans[i].style.backgroundColor = "#777777";
		}
		this.style.transform = 'translate(-50%, -50%) scale(1)';
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
		div.querySelectorAll('img.releaseicon')[0].src = featurediconsources[i-1];
		div.querySelectorAll('p.releaseheading')[0].textContent = featuredtitles[i-1];
		div.querySelectorAll('p.releasebody')[0].textContent = featureddescriptions[i-1];
		div.querySelectorAll('a.coverlink')[0].href = featuredlinks[i-1];
		addborder(div, 29, 28);
	}
	var div = document.querySelectorAll('div.releaseimg')[0];
	div.querySelectorAll('img.releaseimg')[0].src = featuredimgsource;
	div.querySelectorAll('a.coverlink')[0].href = featuredimglink;
	div.querySelectorAll('a.releaselbl')[0].href = featuredimglink;
	div.querySelectorAll('a.releaselbl')[0].textContent = featuredimgname;
	div.onmouseover = function() {
		var a = this.querySelectorAll('a.releaselbl')[0];
		a.style.opacity='1';
	}
	div.onmouseout = function() {
		var a = this.querySelectorAll('a.releaselbl')[0];
		a.style.opacity='0';
	}
}

function setlore() {
	for (var i = 1; i <= 8; i++) {
		var div = document.getElementById("lore" + i);
		addborder(div, 19, 18);
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
		node.href = 'lore?filter=' + lorenames[i-1];
		node.className = 'coverlink';
		div.append(node);
	}
}

var artpos = [[50, 80, 120], [20, 50, 80], [-20, 20, 50]];
var artop = [[1, 0.4, 0], [0.4, 1, 0.4], [0, 0.4, 1]];
var artcoords = [50, 100, 1000];

function initart() {
	document.getElementsByClassName("art")[0].style.height=(250*vh) + "px";
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("art" + i);
		var img = document.createElement('img');
		img.className = 'artimg';
		img.src = artimgsources[i-1];
		div.append(img);
		var covernode = document.createElement('a');
		covernode.className = 'coverlink';
		covernode.href = artlinks[i-1];
		div.append(covernode);
		var node = document.createElement("a");
		node.className = "artlabel";
		node.href = artlinks[i-1];
		node.textContent = artnames[i-1];
		node.style.opacity = "0";
		div.append(node);
		div.onmouseover = function() {
			var a = this.querySelectorAll('a.artlabel')[0];
			a.style.opacity="1";
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
		if (artpos[k][i-1]==50) {
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
	var txt = "<p class='sponsorname' style='left: (LEFT)vw; top: (TOP)vw;' data-aos='fade-up' data-aos-delay='(DELAY)' data-aos-offset='0'>CONTENT</p>";
	var befirst = "<p id='sponsorplaceholder' data-aos='fade-up'>Be the first to donate!</p>";
	var div = document.getElementsByClassName("sponsor")[0];
	if (sponsors.length==0) {
		div.innerHTML += befirst;
		return;
	}
	var node;
	var i = 0;
	for (var h = 13; h < 40 && i<sponsors.length; h += 5) {
		for (var l = 15; l < 90 && i<sponsors.length; l += 15) {
			var delay = Math.round((h+l)/10.0)*50;
			var cpy = txt;
			cpy = cpy.replace("(LEFT)", l.toString());
			cpy = cpy.replace("(TOP)", h.toString());
			cpy = cpy.replace("(DELAY)", delay.toString());
			cpy = cpy.replace("CONTENT", sponsors[i]);
			div.innerHTML += cpy;
			i += 1;
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

var footerlinks = ["https://www.instagram.com/theeurekacollective/", "https://www.facebook.com/eurekacollective/", "https://www.artstation.com/theeurekacollective", "https://www.reddit.com/r/projectanima/", "https://www.patreon.com/eurekacollective", "https://www.buymeacoffee.com/projectanima", "https://ko-fi.com/eurekacollective", "index", "lore", "art", "universe", "aboutus", "privacypolicy", "sitemap"];
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
