from flask import Flask, render_template, url_for, request
from website.forms import ContactForm, NewsletterSub
from website.models import User, Newsletter
from website import app

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html', title ='Homepage')

@app.route("/index")
def index():
	return render_template('index.html', title ='Homepage')

@app.route("/layout", methods=['GET','POST'])
def layout():
	form = ContactForm()
	if form.validate_on_submit():
		user = User(name = form.name.data, email = form.email.data, subject = form.subject.data, message = form.message.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your message has been sent!','success')
		return redirect(url_for('home'))
	return render_template('index.html')

@app.route("/newsletter", methods=['GET','POST'])
def newsletter():
	form = NewsletterSub()
	if form.validate_on_submit():
		new = Newsletter(email = form.email.data, name=form.name.data)
		db.session.add(new)
		db.session.commit()
		flash(f'You are now subscribed to our newsletter!','success')
		return redirect(url_for('home'))
	return render_template('newsletter.html', title = 'Newsletter', form = form)

@app.route("/ourwork")
def ourwork():
	return render_template('ourwork.html', title = 'Our Work')

@app.route("/vision")
def vision():
	return render_template('vision.html', title = 'Vision and Mission')

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
	return render_template('gallery.html', title ='Gallery')

@app.route("/team")
def team():
	return render_template('team.html', title = 'Team')

@app.route("/contactus" ,methods=['GET','POST'])
def contactus():
	form = ContactForm()
	if form.validate_on_submit():
		user = User(name = form.name.data, email = form.email.data, subject = form.subject.data, message = form.message.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your message has been sent!','success')
		return redirect(url_for('home'))
	return render_template('contactus.html', title = 'Contact Us', form=form)

@app.route("/layout2")
def layout2():
	return render_template('layout2.html')
