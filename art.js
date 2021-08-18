var imgs = ["resources/Infinite City.jpg", "resources/Magus.png", "resources/Sculpt.jpeg"];
var gallerynames = ["THE INFINITE CITY", "MAGUS", "SCULPT"];
var artpagelink = ["artspecific.html", "artspecific.html", "artspecific.html"];

function initgallery() {
	var i = 0;
	var div = document.getElementById("artgallery");
	for (var y = 12; true; y += 32) {
		for (var x = 16; x < 100; x += 34) {
			if (i>=imgs.length) break;
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
			lbl.mouseIsOver = false;
			lbl.onmouseover = function() {
				this.style.opacity='1';
				this.mouseIsOver=true;
			}
			lbl.onmouseout = function() {
				this.mouseIsOver=false;
				this.style.opacity='0.4';
			}
			node.append(lbl);
			node.onmouseover = function() {
				var a = this.querySelectorAll('a.gallerylbl')[0];
				if (a.mouseIsOver) return;
				a.style.opacity='0.4';
			}
			node.onmouseout = function() {
				var a = this.querySelectorAll('a.gallerylbl')[0];
				a.style.opacity='0';
			}
			div.append(node);
			i += 1;
		}
		if (i>=imgs.length) {
			div.style.height = (y+12)+'vw';
			break;
		}
	}
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
		this.style.top='48%';
		this.style.width='96%';
		this.style.height='80%';
		this.style.backgroundColor="#00000000";
	}
}
