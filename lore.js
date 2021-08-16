
var defaultinfo = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"];
var imgname = ["resources/Materna Icon.svg"];
var boxinfo = ["CATEGORY--Factions|Human Domain|Corporation|Human|Synthia Faber|September 1st, 2021"];
var article = [`===MATERNA
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
==SECTION TITLE
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
=Paragraph Title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`]



function initlorespecific() {
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	var id = parseInt(urlParams.get('id'));
	document.querySelectorAll("img.infoimg")[0].src=imgname[id];
	// alert(document.querySelectorAll("img.infoimg")[0].src);
	var info = boxinfo[id].split('|');
	for (var i = 0; i < 6; i++) {
		var a = "", b = "";
		var index = info[i].indexOf("--");
		if (index==-1) {
			a=defaultinfo[i];
			b=info[i];
		} else {
			a = info[i].substring(0, index);
			b = info[i].substring(index+2, info[i].length);
		}
		document.getElementById("boxh"+i).textContent = a;
		document.getElementById("boxi"+i).textContent = b;
	}
	var div = document.getElementsByClassName("specificall")[0];
	var text = article[id].split('\n');
	for (var i = 0; i < text.length; i++) {
		if (text[i].length >= 3 && text[i].substring(0, 3)=="===") {
			var node = document.createElement('p');
			node.className = "infoheading";
			node.textContent = text[i].substring(3, text[i].length);
			div.append(node);
			node = document.createElement('span');
			node.className = "underline";
			div.append(node);
		} else if (text[i].length >= 2 && text[i].substring(0, 2)=='==') {
			var node = document.createElement('p');
			node.className = "sectiontitle";
			node.textContent = text[i].substring(2, text[i].length);
			div.append(node);
			node = document.createElement('span');
			node.className = "underline";
			div.append(node);
		} else if (text[i].length >= 1 && text[i].substring(0, 1)=='=') {
			var node = document.createElement('p');
			node.className = "paragraphtitle";
			node.textContent = text[i].substring(1, text[i].length);
			div.append(node);
		} else {
			var node = document.createElement('p');
			node.className = "infoparagraph";
			node.textContent = text[i];
			div.append(node);
		}
	}
}
