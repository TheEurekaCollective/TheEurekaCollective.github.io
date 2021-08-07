
var coords = [600, 1200, 1800, 2400, 3000, 3600];
var pos = ["10%", "26%", "42%", "58%", "74%", "90%"];
var ids = ["scroll1", "scroll2", "scroll3", "scroll4", "scroll5", "scroll6"];

function getY(){
  var top  = window.pageYOffset || document.documentElement.scrollTop;
  return top;
}
function update(){
	var y = getY();
	var p = document.getElementById("scrolldot");
	var b = [false,false,false,false,false,false];
	for (var i = 0; i < 6; i++) {
		if (y<coords[i]) {
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

update();
