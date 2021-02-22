from flask_wtf import Form
from wtforms.fields import TextField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('E-mail', validators=[DataRequired(), Email()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])
