from flask import Flask
from flask_mail import Mail
from config import Config

mail = Mail()

def create_app():
    
    from .views import view
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mail.init_app(app)
    
    app.register_blueprint(view)
    
    return app