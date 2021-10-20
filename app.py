# Local Hosting to Mimic GitHub Pages
#   Penn Bauman (pcb8gb@virginia.edu)
import os
from flask import Flask, abort, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/<path:loc>")
def page(loc):
    if os.path.isfile(loc):
        return send_file(loc)
    if os.path.isfile(loc + ".html"):
        return send_file(loc + ".html")
    return abort(404)
