# --- IMPORTATION ---
from flask import Flask

# --- APP CREATION ---
app = Flask(__name__) # creation of the Flask object app

#
@app.route("/") # route decorator to tell the url flash should use (INDEX)
def index(): # what inside the page 
    return "Index page " # return the page content

@app.route("/presentation_colloc")
def pres_colloc():
    return "Présentation colloc"
