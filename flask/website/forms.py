from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ContactForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    subject = StringField('subject',validators=[DataRequired(), Length(min=2, max=200)])
    message = StringField('message',validators=[DataRequired(), Length(min=2, max=2000)])
    sendmessage = SubmitField('Send message')


class Newsletter(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Thank You')
