from flask import Flask
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
@app.route('/index')
def index():
	t = translator.translate('Hello World', dest='fr')
	return t.text

app.run(debug=True)