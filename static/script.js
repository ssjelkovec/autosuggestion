window.onload = function () {

	var input = document.getElementById('input');

	document.getElementById('s1').addEventListener('click', (event) => { input.value += document.getElementById('s1').textContent });
	document.getElementById('s2').addEventListener('click', (event) => { input.value += document.getElementById('s2').textContent });
	document.getElementById('s3').addEventListener('click', (event) => { input.value += document.getElementById('s3').textContent });

}

function changed() {
	var input = document.getElementById('input');
	var t = input.value
	if (t.charAt(t.length - 1) == ' ') {
		call(input)
	}
}

function call(input) {
	const d = window.location.host

	fetch(`http://${d}`, { method: 'POST' })
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