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
		print(tekst)
		# bayes logika ovdje

		#print(naivni_bayes(L, ["sunny", "cool", "high", "true"]))


		# array sa sugestijama koji se salje browser
		#sugestije = ['ovo', 'je', 'test']
		sugestije = naivni_bayes(L, ["sunny", "cool", "high", "true"])

		return jsonify(sugestije)
