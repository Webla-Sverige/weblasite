from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextInput, TextArea

class CustomTextInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', 'field w-input')
        kwargs.setdefault('maxlength', 256)
        kwargs.setdefault('data-name', field.label.text)
        kwargs.setdefault('placeholder', '')
        return super(CustomTextInput, self).__call__(field, **kwargs)

class CustomTextArea(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', 'field big w-input')
        kwargs.setdefault('maxlength', 5000)
        kwargs.setdefault('data-name', field.label.text)
        kwargs.setdefault('placeholder', '')
        return super(CustomTextArea, self).__call__(field, **kwargs)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], widget=CustomTextInput())
    email = StringField('Email', validators=[DataRequired(), Email()], widget=CustomTextInput())
    message = TextAreaField('Dina tankar', validators=[DataRequired()], widget=CustomTextArea())