window.onload = function () {

	var input = document.getElementById('input');

	document.getElementById('s1').addEventListener('click', () => {
		input.value += document.getElementById('s1').textContent + ' ';
		changed()
	});
	document.getElementById('s2').addEventListener('click', () => {
		input.value += document.getElementById('s2').textContent + ' ';
		changed()
	});
	document.getElementById('s3').addEventListener('click', () => {
		input.value += document.getElementById('s3').textContent + ' ';
		changed()
	});

}

function changed() {
	var input = document.getElementById('input');
	var t = input.value
	if (t.charAt(t.length - 1) == ' ') {
		call(t)
	}
}

function call(input) {
	const d = window.location.host

	fetch(`http://${d}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(input)
	})
		.then(res => {
			res.text().then(text => suggest(text))
		})
}

function suggest(s) {
	const sugestije = JSON.parse(s)
	document.getElementById('s1').textContent = sugestije[0]
	document.getElementById('s2').textContent = sugestije[1]
	document.getElementById('s3').textContent = sugestije[2]

}