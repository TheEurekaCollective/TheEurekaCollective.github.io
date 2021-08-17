var imgs = ["resources/Infinite City.jpg", "resources/Magus.png", "resources/chungus.jpeg"];
var gallerynames = ["THE INFINITE CITY", "MAGUS", "SCULPT"];
var pagelink = ["artspecific.html", "artspecific.html", "artspecific.html"];

function initgallery() {
	var i = 0;
	var div = document.getElementById("artgallery");
	for (var y = 15; true; y += 32) {
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
			var lbl = document.createElement('p');
			lbl.className = 'gallerylbl';
			lbl.textContent = gallerynames[i];
			node.append(lbl);
			var link = document.createElement('a');
			link.className = 'gallerylink';
			link.href = pagelink[i];
			node.append(link);
			div.append(node);
			i += 1;
		}
		if (i>=imgs.length) {
			div.style.height = (y+10)+'vw';
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
