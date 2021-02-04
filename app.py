from flask import Flask, render_template, request, jsonify
from helpers.bayes import *

app = Flask(__name__,
			template_folder='./templates',
			static_folder='./static')

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.url_map.strict_slashes = False


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		# pocetna stranica
		
		return render_template('index.html')

	# blok koda koji se izvsi kada se se upise nova rijec u pregledniku
	else:

		tekst = request.json

		u = zadnja_dva(tekst)
		print(u)

		if u is not None:
			sugestije = naivni_bayes(prve_dvije(u), ["i", "je"])
			return jsonify(sugestije)
		else:
			return jsonify([])


def zadnja_dva(tekst):
	uvjet = tekst.split(" ")
	uvjet.pop()

	if not len(uvjet) < 2:
		return uvjet[-2:]