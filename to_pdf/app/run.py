from routes import app, UPLOAD_FOLDER

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.run(
	host="0.0.0.0",
	port=int(5000),
	debug=True
	)
