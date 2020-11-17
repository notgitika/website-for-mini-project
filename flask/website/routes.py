from flask import Flask, render_template, url_for, redirect, flash
from website.forms import ContactForm, NewsletterSub
from website.models import User, Newsletter
from website import app, db

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = ContactForm()
	layout()
	return render_template('index.html', title ='Homepage', form = form)

@app.route("/index", methods = ['GET', 'POST'])
def index():
	form = ContactForm()
	layout()
	return render_template('index.html', title ='Homepage', form = form)

@app.route("/layout", methods = ['GET', 'POST'])
def layout():
	form = ContactForm()
	if form.validate_on_submit():
		user = User(name=form.name.data, email=form.email.data, subject=form.subject.data, message=form.message.data,)
		db.session.add(user)
		db.session.commit()
		return render_template(url_for('home'))
	return render_template('layout.html', form=form)

@app.route("/newsletter", methods=['GET','POST'])
def newsletter():
	form = NewsletterSub()
	if form.validate_on_submit():
		new = Newsletter(email=form.email.data, name=form.name.data)
		db.session.add(new)
		db.session.commit()
		return render_template('newsletter.html', title = 'Newsletter')
	return render_template('newsletter.html', title = 'Newsletter', form = form)

@app.route("/ourwork", methods = ['GET', 'POST'])
def ourwork():
	form = ContactForm()
	layout()
	return render_template('ourwork.html', title = 'Our Work', form = form)

@app.route("/vision", methods = ['GET', 'POST'])
def vision():
	form = ContactForm()
	layout()
	return render_template('vision.html', title = 'Vision and Mission', form = form)

@app.route("/visioners", methods = ['GET', 'POST'])
def visioners():
	form = ContactForm()
	layout()
	return render_template('visioners.html', title = 'Visioners', form = form)

@app.route("/reach", methods = ['GET', 'POST'])
def reach():
	form = ContactForm()
	layout()
	return render_template('reach.html', title = 'Reach', form = form)

@app.route("/impact", methods = ['GET', 'POST'])
def impact():
	form = ContactForm()
	layout()
	return render_template('impact.html', title = "impact", form = form)

@app.route("/partners", methods = ['GET', 'POST'])
def partners():
	form = ContactForm()
	layout()
	return render_template('partners.html', title = "partners", form = form)

@app.route("/gallery", methods = ['GET', 'POST'])
def gallery():
	form = ContactForm()
	layout()
	return render_template('gallery.html', title ='Gallery', form = form)

@app.route("/team", methods = ['GET', 'POST'])
def team():
	form = ContactForm()
	layout()
	return render_template('team.html', title = 'Team', form = form)

@app.route("/contactus", methods = ['GET', 'POST'])
def contactus():
	form = ContactForm()
	layout()
	return render_template('contactus.html', title = 'Contact Us', form=form)

@app.route("/layout2", methods = ['GET', 'POST'])
def layout2():
	form = ContactForm()
	layout()
	return render_template('layout2.html', form = form)
