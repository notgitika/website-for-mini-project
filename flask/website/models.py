from website import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	subject = db.Column(db.String(200), unique=False, nullable=False)
	message = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"User('{self.name}','{self.email}','{self.subject}','{self.message}')"


class Newsletter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	name = db.Column(db.String(20), unique=False, nullable=False)

	def __repr__(self):
		return f"Newsletter('{self.name}','{self.email}')"
