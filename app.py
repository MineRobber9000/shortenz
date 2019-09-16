from flask import *
import tsv

app = Flask(__name__)

def get_shortnames():
	if "shortnames" not in g:
		with open("shortnames.tsv") as f:
			g.shortnames = list(tsv.reader(f))
			g.shortnames = {row[0]: row[1] for row in g.shortnames}
	return g.shortnames

@app.route("/")
def home_route():
	shortnames = get_shortnames()
	return redirect(shortnames.get("/*","https://www.google.com/"),code=307)

@app.route("/<path:short>")
def route(short):
	shortnames = get_shortnames()
	return redirect(shortnames.get(short,shortnames.get("/*","https://www.google.com")),code=307)

if __name__=="__main__":
	app.run(port=65010)
