import os
from flask import render_template,Flask, request, redirect, url_for, make_response
from werkzeug import secure_filename
import parser
#References:
#http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
#http://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

def allowed_files(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
# 	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/download/<filename>')
def download(filename):
        csv_file = os.path.join(app.config['UPLOAD_FOLDER'],filename)
	with open(csv_file,"r") as f:
                csv = f.read()
        response = make_response(csv)
	response.headers['Content-Disposition'] = "attachment; filename="+filename
	return response


@app.route("/",methods=['GET','POST'])
def index():
	if request.method == 'POST':
		pdf_file = request.files['file']
		if pdf_file and allowed_files(pdf_file.filename):
			filename = secure_filename(pdf_file.filename)
			pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                        parser.main(pdf=filename)
                        if "@" in filename and filename.count(".") == 2:
                                name_csv = filename.split(".")[0]+"."+filename.split(".")[1]+".csv"
                        else:
                                name_csv = filename.split(".")[0]+".csv"
                        
			return redirect(url_for('download',filename=name_csv))
	return render_template("index.html")
