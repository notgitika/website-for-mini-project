  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models import User, Newsletter


class ContactForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',validators=[DataRequired(), Length(min=2, max=200)])
    message = StringField('Message',validators=[DataRequired(), Length(min=2, max=2000)])
    sendmessage = SubmitField('Send message')
    

class NewsletterSub(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Thank You')
