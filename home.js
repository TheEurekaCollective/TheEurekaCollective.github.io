
var coords = [115, 230, 400, 600, 800, 1000];
var pos = ["10%", "26%", "42%", "58%", "74%", "90%"];
var ids = ["scroll1", "scroll2", "scroll3", "scroll4", "scroll5", "scroll6"];
var vh = window.innerHeight / 100.0;
var vw = window.innerWidth / 100.0;

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

update();
