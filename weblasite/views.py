from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mail import Message
from weblasite import mail
from weblasite.forms import ContactForm

# Create a Blueprint object named 'weblasite' with the same name as this file
view = Blueprint('view', __name__, template_folder='templates')

@view.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@view.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        msg = Message(
            'New message from {} <{}>'.format(form.name.data, form.email.data),
            sender='kontakt@webla.se',
            recipients=['kontakt@webla.se']
        )
        msg.body = form.message.data
        mail.send(msg)

        return jsonify({'success': 'Message sent!'})
    
    return jsonify({'error': 'Something went wrong!'})