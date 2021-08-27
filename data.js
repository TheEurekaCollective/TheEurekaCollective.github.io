const pagedata = [`MATERNA
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
SECTION TITLE
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Paragraph Title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`,
`AETERNUM
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation ullamco laboris nulla pariatur. Duis nulla pariatur. Duis aute irure dolor in reprehenderit in velit esse cillum dolore eu fugiat quis nostrud exercitation fugiat quis nostrud exercitation ullamco nulla pariatur.`]
const pagetitle = ["MATERNA", "AETERNUM"];
const pagelink = ["lorespecific.html", "artspecific.html"];
const type = ["lore", "art"];
const indices = [1, 0];
var loreindices;
var artindices;

for (var i = 0; i < pagedata.length; i++) {
	pagedata[i] = pagedata[i].toLowerCase();
}

function initresults() {
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	var search = urlParams.get("search");
	loreindices = [];
	artindices = [];
	if (search.length==0) {
		return;
	}
	var tosort = [];
	for (var i = 0; i < pagedata.length; i++) {
		tosort.push([score(i, search), i]);
	}
	tosort.sort(function(a, b) {return a[0]-b[0];});
	tosort.reverse();
	for (var i = 0; i < tosort.length; i++) {
		if (tosort[i][0]>0) {
			var x = tosort[i][1];
			if (type[x] == "lore") {
				loreindices.push(indices[x]);
			} else {
				artindices.push(indices[x]);
			}
		}
	}
}


//shortens document.getElementById
function element(id) { return document.getElementById(id); }

function strcnt(a, b) {
	var r = a.indexOf(b);
	var c = 0;
	while (r != -1) {
		c++;
		r = a.indexOf(b, r + 1);
	}
	return c;
}

function score(p, s) {
	s = s.split(' ');
	var ans = 0;
	for (var i = 0; i < s.length; i++) {
		if (s[i].length==0) return;
		ans += strcnt(pagetitle[p].toLowerCase(), s[i])*s[i].length*s[i].length*10;
		ans += strcnt(pagedata[p], s[i])*s[i].length*s[i].length;
	}
	return ans;
}

//gets each inputs data starting from second input
function getResults() {
	//gets value of input
	let search = document.querySelectorAll('input.menu')[0].value.toLowerCase();
	var tosort = [];
	allSearchData = ""; //clears data for each word typed

	element("search-results").style.display = "none";
	element("search-results").innerHTML = "";

	if (search.length==0) return;
	for (var i = 0; i < pagedata.length; i++) {
		tosort.push([score(i, search), i]);
	}
	tosort.sort(function(a, b) {return a[0]-b[0];});
	tosort.reverse();
	for (var i = 0; i < tosort.length && i < 10; i++) {
		if (tosort[i][0]>0) {
			var x = pagetitle[tosort[i][1]];
			if (x.length>17) x = x.slice(0, 17) + "...";
			element("search-results").innerHTML +=
				"<div class='search-item'><a class='search-item' href='"+pagelink[tosort[i][1]]+"'>" + x + "</a></div>";
		}
	}
	if (tosort[0][0]==0) {
		element("search-results").innerHTML = "<div class='search-item no-results'><a class='search-item no-results'>No Results</a></div>"
	}
	element("search-results").style.display = "block";
}
//gets results after each input
document.querySelectorAll('input.menu')[0].oninput = function() {
	getResults();
};
document.querySelectorAll('input.menu')[0].onblur = function() {
	window.addEventListener("click", function() {
		setTimeout(() => {element("search-results").style.display = "none";}, 10);
	}, {once : true});
};
document.querySelectorAll('input.menu')[0].onfocus = function() {
	getResults();
};
