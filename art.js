// address of the art image to be added
var imgs = ["resources/Infinite City.jpg", "resources/Magus.png", "resources/Sculpt.jpeg"];
// name of the image
var gallerynames = ["THE INFINITE CITY", "MAGUS", "SCULPT"];
// link to the specific page
// note that if the html file is 'artspecific.html' the link is 'artspecific'
var artpagelink = ["artspecific", "artspecific", "artspecific"];

function initartboxes(indices, div, start) {
	var j = 0;
	for (var y = start; true; y += 32) {
		var nxt = Math.min(indices.length-j, 3)-1;
		for (var x = 50-12*nxt; x < 51+12*nxt; x += 24) {
			if (j>=indices.length) break;
			var i = indices[j];
			var node = document.createElement('div');
			node.className = 'artdisplay';
			node.style.left = x + '%';
			node.style.top = y + 'vw';
			var img = document.createElement('img');
			img.className = 'galleryimg';
			img.src = imgs[i];
			node.append(img);
			var cvr = document.createElement('a');
			cvr.className = 'coverlink';
			cvr.href = artpagelink[i];
			node.append(cvr);
			var lbl = document.createElement('a');
			lbl.className = 'gallerylbl';
			lbl.textContent = gallerynames[i];
			lbl.href = artpagelink[i];
			node.append(lbl);
			node.onmouseover = function() {
				var a = this.querySelectorAll('a.gallerylbl')[0];
				a.style.opacity='1';
			}
			node.onmouseout = function() {
				var a = this.querySelectorAll('a.gallerylbl')[0];
				a.style.opacity='0';
			}
			div.append(node);
			j += 1;
		}
		if (j>=indices.length) {
			div.style.height = (y+20)+'vw';
			div.myheight = (y+20);
			break;
		}
	}
}

function initgallery() {
	var div = document.getElementById("artgallery");
	var indices = [];
	for (var i = 0; i < imgs.length; i++) indices.push(i);
	initartboxes(indices, div, 22);
	document.getElementById('artcontainer').style.height = document.getElementById('artgallery').style.height;
}

function initspecific() {
	var img = document.querySelectorAll('img.specificimg')[0];
	img.fullscreen = false;
	var fs = document.getElementById('fullscreen');
	fs.onclick = function() {
		var img = document.querySelectorAll('img.specificimg')[0];
		if (img.fullscreen) return;
		img.fullscreen=true;
		img.style.left='50vw';
		img.style.top='50vh';
		img.style.width='100vw';
		img.style.height='100vh';
		img.style.backgroundColor="#000000ff";
	}
	img.onclick = function() {
		if (! this.fullscreen) return;
		this.fullscreen = false;
		this.style.left='50%';
		this.style.top='50%';
		this.style.width='96%';
		this.style.height='75%';
		this.style.backgroundColor="#00000000";
	}
}

var artspanclasses = ["arth c1", "artv c1", "arth c2", "artv c2", "arth c3", "artv c3", "arth c4", "artv c4"];

function fullscreenborder(div, a, b, c, d) {
	var node;
	var ratio = a/c;
	for (var j = 0; j < 8; j++) {
		node = document.createElement("span");
		node.className = artspanclasses[j];
		div.append(node);
	}
	div.onmouseover = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) if (spans[i].className != "entryfade") {
			spans[i].style.boxShadow = "0 0 5px white";
			spans[i].style.backgroundColor = "white";
		}
		this.style.transform = 'translate(-50%, -50%) scale(' + (a/c).toPrecision(15) + ', ' + (b/d).toPrecision(15) + ')';
	}
	div.onmouseout = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) if (spans[i].className != "entryfade") {
			spans[i].style.boxShadow = "0 0 0px white";
			spans[i].style.backgroundColor = "#cccccc";
		}
		this.style.transform = 'translate(-50%, -50%) scale(1)';
	}
}

function specificscroll() {
	var div = document.querySelectorAll('p.gallerytxt')[0];
	var totalheight = div.scrollHeight;
	var showheight = 50 * window.innerHeight / 100.0;
	if (totalheight <= showheight) return;
	var percent = div.scrollTop / (totalheight - showheight);
	document.getElementById('gdot').style.top = (100.0 * percent) + '%';
}
