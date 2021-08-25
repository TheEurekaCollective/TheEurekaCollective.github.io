
function universescroll() {
	var div = document.querySelectorAll('div.devlog')[0];
	var totalheight = div.scrollHeight;
	var showheight = div.clientHeight;
	// var showheight = 35 * window.innerWidth / 100.0;
	if (totalheight <= showheight) return;
	var percent = div.scrollTop / (totalheight - showheight);
	document.getElementById('udot').style.top = (100.0 * percent) + '%';
}
