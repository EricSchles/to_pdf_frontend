import os
from flask import Flask

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

@app.route("/")
def index():
