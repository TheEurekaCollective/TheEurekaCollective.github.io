
var coords = [115, 230, 361, 494, 715, 10000];
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
	var y = getY() / vh;
	var p = document.getElementById("scrolldot");
	var b = [false,false,false,false,false,false];
	for (var i = 0; i < 6; i++) {
		if (y<=coords[i]+1) {
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
	if (i>0) offset = coords[i-1] * vh + 20;
	offset = offset - getY();
	window.scrollBy(0, offset);
	update();
}

function addborder(div) {
	var node;
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
		this.style.width="16vw";
		this.style.height="22vw";
		this.getElementsByClassName("lorelbl")[0].style.fontSize = "120%";
	}
	div.onmouseout = function() {
		spans = this.getElementsByTagName("span");
		for (var i = 0; i < spans.length; i++) {
			spans[i].style.boxShadow = "0 0 0px white";
			spans[i].style.backgroundColor = "#666666";
		}
		this.style.width="15vw";
		this.style.height="21vw";
		this.getElementsByClassName("lorelbl")[0].style.fontSize = "110%";
	}
}

function setfeature() {
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("release" + i);
		addborder(div);
	}
}

function setlore() {
	for (var i = 1; i <= 8; i++) {
		var div = document.getElementById("lore" + i);
		addborder(div);
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
var artcoords = [568,642, 10000];

function updart(k) {
	for (var i = 1; i <= 3; i++) {
		var div = document.getElementById("art" + i);
		div.style.left = "" + artpos[k][i-1] + "vw";
		div.style.opacity = "" + artop[k][i-1];
	}
}

function scrollart() {
	// alert("doing stuff");
	updateSize();
	var y = getY() / vh;
	for (var i = 0; i < 3; i++) {
		if (y<=artcoords[i]+1) {
			updart(i);
			break;
		}
	}
}

updart(0);
setfeature();
setlore();
update();
