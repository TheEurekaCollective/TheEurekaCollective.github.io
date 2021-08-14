var imgs = ["resources/Infinite City.jpg", "resources/Magus.png", "resources/chungus.jpeg"];
var gallerynames = ["THE INFINITE CITY", "MAGUS", "SCUPT"];

function initgallery() {
	var i = 0;
	var div = document.getElementById("artgallery");
	for (var y = 15; true; y += 32) {
		if (i>=imgs.length) break;
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
			div.append(node);
			i += 1;
		}
	}
}
