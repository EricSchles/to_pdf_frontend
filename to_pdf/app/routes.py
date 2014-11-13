import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

def allowed_files(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route("/",methods=['GET','POST'])
def index():
	if request.method == 'POST':
		pdf_file = request.files['file']
		if pdf_file and allowed_file(pdf_file.filename)
		pdf_file.save(os.path.join)