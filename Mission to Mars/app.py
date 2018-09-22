from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
print(app)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
	pass
	return render_template("index.html", )

@app.route("/scrape")
def scrape():
	pass
  return redirect("/", code=302)

if __name__ == "__main__":
	app.run(debug=True)