from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/layout")
def layout():
	return render_template('layout.html')

@app.route("/newsletter")
def newsletter():
	return render_template('newsletter.html')

@app.route("/ourwork")
def ourwork():
	return render_template('ourwork.html')

@app.route("/vision")
def vision():
	return render_template('vision.html')

@app.route("/visioners")
def visioners():
	return render_template('visioners.html')

@app.route("/reach")
def reach():
	return render_template('reach.html')

@app.route("/impact")
def impact():
	return render_template('impact.html')

@app.route("/partners")
def partners():
	return render_template('partners.html')

@app.route("/gallery")
def gallery():
	return render_template('gallery.html')

@app.route("/team")
def team():
	return render_template('team.html')

@app.route("/contactus")
def contactus():
	return render_template('contactus.html')

@app.route("/layout2")
def layout2():
	return render_template('layout2.html')
	
	
if __name__ == '__main__':
	app.run(debug=True)