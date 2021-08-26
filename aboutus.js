var memberpfps = ["Josephine Lee.jpg", "zaxwellmen.png", "Sirawyn.gif", "Isabelle Lam.jpg", "Doctor Martins.JPG", "TitanAMB.png", "jessica mui.jpg", "Xiaoshen Ma With Flame.jpg", "wajora!.jpg", "Zephyryne.JPG"];
var membernames = ["Josephine Lee", "zaxwellmen", "Sirawyn", "bowbow", "Dr. Martins", "TitanAMB", "Jessica", "Xiaoshen Ma", "wajora!", "Zephyryne"];
var memberroles = ["Editor", "Web Developer", "Founder & Director", "Editor", "Promoter", "Artist", "Artist", "Artist", "Scribe", "Page"];

function initaboutus() {
	var i = 0;
	var div = document.getElementById('meettheteam');
	for (var y = 7; i < memberpfps.length; y += 19) {
		for (var x = 16; x < 85 && i < memberpfps.length; x += 17) {
			var node = document.createElement('div');
			node.className = 'teammember';
			node.style.left = x + 'vw';
			node.style.top = y + 'vw';
			var img = document.createElement('img');
			img.className = 'memberpfp';
			img.src = "resources/memberprofiles/" + memberpfps[i];
			node.append(img);
			var user = document.createElement('p');
			user.className = 'memberuser';
			user.textContent = membernames[i];
			node.append(user);
			var role = document.createElement('p');
			role.className = 'memberrole';
			role.textContent = memberroles[i];
			node.append(role);
			div.append(node);
			i += 1;
		}
		if (i >= memberpfps.length) {
			document.getElementById('meettheteam').style.height = (y+24)+'vw';
		}
	}
}
