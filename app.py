# --- IMPORTATION ---
from flask import Flask, render_template

# --- APP CREATION ---
app = Flask(__name__) # creation of the Flask object app

#
@app.route("/") # route decorator to tell the url flash should use (INDEX)
def pres_colloc(): # what inside the page
    return render_template("pres_colloc.html")# return the page content

@app.route("/pres_inter") # route decorator to tell the url flash should use (INDEX)
def pres_inter(): # what inside the page
    return render_template("pres_inter.html")# return the page content

@app.route("/links") # route decorator to tell the url flash should use (INDEX)
def links(): # what inside the page
    return render_template("links.html")# return the page content


if __name__ == "__main__":
    app.run(debug=True)

