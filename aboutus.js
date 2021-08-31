var memberpfps = ["Alyssa Choi.PNG", "zaxwellmen.png", "Sirawyn.gif", "Isabelle Lam.jpg", "loy.JPG", "Josephine Lee.jpg", "Doctor Martins.JPG", "TitanAMB.png", "jessica mui.jpg", "Xiaoshen Ma With Flame.jpg", "wajora!.jpg", "Zephyryne.JPG"];
var membernames = ["Alyssa Choi", "Maxwell Zen", "Devin Deng", "bowbow", "Loy", "Josephine Lee", "Dr. Martins", "TitanAMB", "Jessica", "Xiaoshen Ma", "wajora!", "Zephyryne"];
var memberroles = ["Web Developer", "Web Developer", "Founder & Director", "Editor", "Editor", "Editor", "Promoter", "Artist", "Artist", "Artist", "Scribe", "Page"];

function initaboutus() {
	var i = 0;
	var div = document.getElementById('meettheteam');
	for (var y = 7; i < memberpfps.length; y += 19) {
		var nxt = Math.min(memberpfps.length-i, 5)-1;
		for (var x = 50 - 8.5*nxt; x < 51 + 8.5*nxt && i < memberpfps.length; x += 17) {
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
