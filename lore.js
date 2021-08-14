
var spanclasses = ["h c1", "v c1", "h c2", "v c2", "h c3", "v c3", "h c4", "v c4"];
var defaultinfo = ["CATEGORY", "DOMAIN", "CLASS", "SPECIES", "AUTHOR", "LAST UPDATE"];
var imgname = ["resources/Materna Icon.svg"];

function plainborder(div) {
	var node;
	for (var j = 0; j < 8; j++) {
		node = document.createElement("span");
		node.className = spanclasses[j];
		div.append(node);
	}
}
