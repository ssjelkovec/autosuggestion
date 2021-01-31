window.onload = function () {



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
			res.text().then(text => input.value = text)
		})
}