from flask import *

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static')

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.url_map.strict_slashes = False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    else:
		sugestije = ['ovo', 'je', 'test']
        return jsonify(sugestije)
