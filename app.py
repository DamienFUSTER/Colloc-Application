# --- IMPORTATION ---
from flask import Flask, render_template

# --- APP CREATION ---
app = Flask(__name__) # creation of the Flask object app

#
@app.route("/") # route decorator to tell the url flash should use (INDEX)
def index(): # what inside the page 
    return render_template("index.html")# return the page content

@app.route("/presentation_colloc")
def pres_colloc():
    return "Présentation colloc"

if __name__ == "__main__":
    app.run(debug=True)

