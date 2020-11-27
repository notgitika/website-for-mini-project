  
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
    
        # def validate_email(self, email):
    #     user = User.query,filter_by(email = email.data).first()
    #     if user:
    #         raise ValidationError('That email already has already sent an email. Please continue the conversation on email')

class NewsletterSub(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Thank You')

    # def validate_email(self, email):
    #     new = Newsletter.query,filter_by(email = email.data).first()
    #     if new:
    #         raise ValidationError('That email already has already sent an email. Please continue the conversation on email')